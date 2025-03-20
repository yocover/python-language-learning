import logging
import sys
from pathlib import Path
from typing import List, Optional

from llama_index.core import (
    Document,
    Settings,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

def create_ollama_index(
    documents: List[Document],
    model_name: str = "llama2",
    persist_dir: Optional[str] = None,  # 默认不持久化
    force_reload: bool = False,
) -> VectorStoreIndex:
    """
    创建一个使用 Ollama 作为后端的 LlamaIndex。

    Args:
        documents: 要索引的文档列表
        model_name: Ollama 模型名称，默认为 "llama2"
        persist_dir: 索引持久化目录
        force_reload: 是否强制重新加载索引
    """
    try:
        # 配置 Ollama LLM 和 HuggingFace 嵌入模型
        llm = Ollama(model=model_name, request_timeout=30.0)
        embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        Settings.llm = llm
        Settings.embed_model = embed_model
        Settings.chunk_size = 512
        Settings.chunk_overlap = 50

        if persist_dir and Path(persist_dir).exists() and not force_reload:
            logging.info(f"Loading existing index from {persist_dir}")
            storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
            index = load_index_from_storage(storage_context)
        else:
            logging.info("Creating new index")
            if persist_dir:
                Path(persist_dir).mkdir(parents=True, exist_ok=True)
                storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
            else:
                storage_context = None
            
            # 创建向量存储索引
            index = VectorStoreIndex.from_documents(
                documents,
                storage_context=storage_context,
            )

        return index

    except Exception as e:
        logging.error(f"Error creating index: {str(e)}")
        raise

def main():
    # 创建示例文档
    documents = [
        Document(text="LlamaIndex 是一个强大的框架，可以帮助你构建基于 LLM 的应用。"),
        Document(text="Ollama 是一个本地运行 LLM 的工具，支持多种开源模型。"),
        Document(text="通过结合 LlamaIndex 和 Ollama，你可以构建完全本地运行的 AI 应用。")
    ]

    try:
        # 创建索引，不使用持久化
        index = create_ollama_index(documents)
        
        # 创建查询引擎
        query_engine = index.as_query_engine()
        
        # 执行查询
        response = query_engine.query("LlamaIndex 和 Ollama 有什么关系？")
        print("\n查询结果:")
        print(response)

    except Exception as e:
        logging.error(f"Error in main: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 