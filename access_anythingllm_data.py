from pymilvus import connections, Collection
import json

# 连接到 Milvus
def connect_to_milvus():
    try:
        connections.connect(
            alias="default", 
            host="localhost", 
            port="19530"
        )
        print("成功连接到 Milvus")
        return True
    except Exception as e:
        print(f"连接 Milvus 失败: {e}")
        return False

# 获取 AnythingLLM 集合中的数据
def get_anythingllm_data():
    # 打开集合
    collection_name = "anythingllm_my_workspace"
    collection = Collection(name=collection_name)
    
    # 加载集合到内存
    collection.load()
    
    # 获取集合信息
    print(f"集合名称: {collection_name}")
    print(f"实体数量: {collection.num_entities}")
    
    # 获取集合中的所有数据
    results = collection.query(expr="id != ''", output_fields=["id", "metadata"])
    
    # 处理和显示结果
    print(f"\n找到 {len(results)} 条记录:")
    for i, item in enumerate(results):
        print(f"\n记录 {i+1}:")
        print(f"  ID: {item['id']}")
        
        # 解析 JSON 元数据
        try:
            metadata = json.loads(item['metadata']) if item['metadata'] else {}
            # 提取重要信息
            title = metadata.get('title', 'N/A')
            description = metadata.get('description', 'N/A')
            word_count = metadata.get('wordCount', 'N/A')
            
            print(f"  标题: {title}")
            print(f"  描述: {description}")
            print(f"  字数: {word_count}")
            
            # 如果需要查看完整元数据，可以取消下面的注释
            # print(f"  完整元数据: {json.dumps(metadata, ensure_ascii=False, indent=2)}")
            
            # 显示文本片段
            if 'text' in metadata:
                text = metadata['text']
                print(f"  文本片段: {text[:150]}...")
        except Exception as e:
            print(f"  解析元数据时出错: {e}")
            print(f"  原始元数据: {item['metadata']}")
    
    # 示例：搜索相似向量
    search_vectors = [[0.1] * 768]  # 创建一个示例向量用于搜索
    search_params = {
        "metric_type": "COSINE",  # 使用余弦相似度
        "params": {"nprobe": 10}  # 搜索参数
    }
    
    print("\n执行相似性搜索:")
    try:
        results = collection.search(
            data=search_vectors,
            anns_field="vector",
            param=search_params,
            limit=3,  # 返回前3个最相似的结果
            output_fields=["id", "metadata"]
        )
        
        # 显示搜索结果
        for i, hits in enumerate(results):
            print(f"搜索向量 {i+1} 的结果:")
            for j, hit in enumerate(hits):
                print(f"  {j+1}. ID: {hit.id}, 距离: {hit.distance}")
                
                # 安全地获取和解析元数据
                if hasattr(hit, 'entity'):
                    try:
                        metadata_str = hit.entity.get('metadata', '{}')
                        metadata = json.loads(metadata_str) if metadata_str else {}
                        title = metadata.get('title', 'N/A')
                        print(f"     标题: {title}")
                    except Exception as e:
                        print(f"     解析元数据时出错: {e}")
    except Exception as e:
        print(f"搜索时出错: {e}")
    
    # 完成后卸载集合以释放内存
    collection.release()

# 查看所有集合
def list_all_collections():
    from pymilvus import utility
    print("\n所有可用集合:")
    collections = utility.list_collections()
    for i, name in enumerate(collections):
        print(f"{i+1}. {name}")

# 检索特定文本
def search_text(text_query):
    collection_name = "anythingllm_my_workspace"
    collection = Collection(name=collection_name)
    collection.load()
    
    print(f"\n在元数据中搜索: '{text_query}'")
    try:
        # 在元数据中搜索包含指定文本的记录
        results = collection.query(
            expr=f"metadata like '%{text_query}%'", 
            output_fields=["id", "metadata"]
        )
        
        print(f"找到 {len(results)} 条匹配记录")
        for i, item in enumerate(results):
            print(f"\n匹配记录 {i+1}:")
            print(f"  ID: {item['id']}")
            
            try:
                metadata = json.loads(item['metadata']) if item['metadata'] else {}
                title = metadata.get('title', 'N/A')
                print(f"  标题: {title}")
                
                # 提取包含查询文本的上下文
                if 'text' in metadata:
                    text = metadata['text']
                    if text_query.lower() in text.lower():
                        start = max(0, text.lower().find(text_query.lower()) - 50)
                        end = min(len(text), text.lower().find(text_query.lower()) + len(text_query) + 50)
                        context = text[start:end]
                        print(f"  上下文: ...{context}...")
            except Exception as e:
                print(f"  解析元数据时出错: {e}")
    except Exception as e:
        print(f"文本搜索时出错: {e}")
    
    collection.release()

if __name__ == "__main__":
    if connect_to_milvus():
        # 列出所有集合
        list_all_collections()
        
        # 获取 AnythingLLM 数据
        try:
            get_anythingllm_data()
            
            # 示例：搜索特定文本
            search_text("房屋")
        except Exception as e:
            print(f"访问 AnythingLLM 集合时出错: {e}")
        
        # 断开连接
        connections.disconnect("default")
        print("\n已断开与 Milvus 的连接") 