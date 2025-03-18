from llama_index.core import SimpleDirectoryReader, Settings, Document, ServiceContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import (
    TitleExtractor,
    KeywordExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.llms import OpenAI
from typing import List, Callable
import logging
import os

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 设置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # 替换为你的API密钥

# 配置LLM
llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)

class DocumentPipeline:
    def __init__(self):
        self.steps: List[Callable] = []
        
    def add_step(self, step: Callable):
        """添加处理步骤到管道"""
        self.steps.append(step)
        return self
        
    def process(self, documents: List[Document]) -> List[Document]:
        """执行管道中的所有处理步骤"""
        result = documents
        for step in self.steps:
            logger.info(f"执行处理步骤: {step.__name__}")
            result = step(result)
        return result

def load_documents(directory: str) -> List[Document]:
    """从目录加载文档"""
    reader = SimpleDirectoryReader(input_dir=directory)
    return reader.load_data()

def split_documents(documents: List[Document]) -> List[Document]:
    """将文档分割成句子"""
    splitter = SentenceSplitter(chunk_size=1024)
    split_docs = []
    for doc in documents:
        splits = splitter.split_text(doc.text)
        split_docs.extend([Document(text=split) for split in splits])
    return split_docs

def extract_metadata(documents: List[Document]) -> List[Document]:
    """提取文档元数据（标题、关键词等）"""
    try:
        extractors = [
            TitleExtractor(nodes=5),
            KeywordExtractor(keywords=10),
            QuestionsAnsweredExtractor(questions=3)
        ]
        
        for doc in documents:
            # 基本元数据提取（不依赖LLM）
            doc.metadata["length"] = len(doc.text)
            doc.metadata["word_count"] = len(doc.text.split())
            
            # LLM-based 元数据提取
            if os.getenv("OPENAI_API_KEY"):
                for extractor in extractors:
                    try:
                        metadata = extractor.extract([doc])[0]
                        doc.metadata.update(metadata)
                    except Exception as e:
                        logger.warning(f"提取元数据时出错: {str(e)}")
            else:
                logger.warning("未设置OPENAI_API_KEY，跳过LLM-based元数据提取")
                
    except Exception as e:
        logger.error(f"元数据提取过程出错: {str(e)}")
        
    return documents

def filter_documents(min_length: int = 50) -> Callable:
    """创建一个文档过滤器，去除过短的文档"""
    def filter_step(documents: List[Document]) -> List[Document]:
        return [doc for doc in documents if len(doc.text) >= min_length]
    filter_step.__name__ = "filter_documents"
    return filter_step

def basic_metadata_extraction(documents: List[Document]) -> List[Document]:
    """基本的元数据提取（不使用LLM）"""
    for doc in documents:
        # 提取文本的第一行作为标题
        lines = doc.text.split('\n')
        doc.metadata["title"] = lines[0] if lines else "No title"
        
        # 计算基本统计信息
        doc.metadata["length"] = len(doc.text)
        doc.metadata["word_count"] = len(doc.text.split())
        
        # 简单的关键词提取（基于词频）
        words = doc.text.lower().split()
        word_freq = {}
        for word in words:
            if len(word) > 3:  # 忽略短词
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # 获取出现频率最高的10个词作为关键词
        keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        doc.metadata["keywords"] = [word for word, _ in keywords]
        
    return documents

if __name__ == "__main__":
    # 创建文档处理管道
    pipeline = DocumentPipeline()
    
    # 添加处理步骤
    pipeline.add_step(split_documents)
    pipeline.add_step(filter_documents(min_length=100))
    
    # 根据是否有OpenAI API密钥选择元数据提取方法
    if os.getenv("OPENAI_API_KEY"):
        pipeline.add_step(extract_metadata)
    else:
        logger.info("使用基本元数据提取方法（不使用LLM）")
        pipeline.add_step(basic_metadata_extraction)
    
    try:
        # 加载文档
        docs = load_documents("./data")
        logger.info(f"加载了 {len(docs)} 个文档")
        
        # 处理文档
        processed_docs = pipeline.process(docs)
        logger.info(f"处理完成，得到 {len(processed_docs)} 个文档")
        
        # 显示处理结果
        for i, doc in enumerate(processed_docs[:3], 1):
            print(f"\n文档 {i}:")
            print(f"文本长度: {len(doc.text)}")
            print(f"字数: {doc.metadata.get('word_count', 'N/A')}")
            print(f"标题: {doc.metadata.get('title', 'N/A')}")
            print(f"关键词: {doc.metadata.get('keywords', [])}")
            if os.getenv("OPENAI_API_KEY"):
                print(f"可回答的问题: {doc.metadata.get('questions_answered', [])}")
            
    except Exception as e:
        logger.error(f"处理文档时出错: {str(e)}") 