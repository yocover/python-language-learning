from pymilvus import connections, Collection
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import random

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

# 查看所有集合
def list_all_collections():
    from pymilvus import utility
    print("\n所有可用集合:")
    collections = utility.list_collections()
    for i, name in enumerate(collections):
        print(f"{i+1}. {name}")
    return collections

# 获取 AnythingLLM 集合中的数据
def get_anythingllm_data(get_vectors=False):
    # 打开集合
    collection_name = "anythingllm_my_workspace"
    collection = Collection(name=collection_name)
    
    # 加载集合到内存
    collection.load()
    
    # 获取集合信息
    print(f"集合名称: {collection_name}")
    print(f"实体数量: {collection.num_entities}")
    
    # 确定输出字段
    output_fields = ["id", "metadata"]
    if get_vectors:
        output_fields.append("vector")
    
    # 获取集合中的所有数据
    results = collection.query(expr="id != ''", output_fields=output_fields)
    
    # 处理和显示结果
    print(f"\n找到 {len(results)} 条记录:")
    for i, item in enumerate(results):
        print(f"\n记录 {i+1}:")
        print(f"  ID: {item['id']}")
        
        # 处理元数据
        metadata = item['metadata']
        if isinstance(metadata, str):
            try:
                metadata = json.loads(metadata)
            except:
                print(f"  无法解析元数据: {metadata}")
                continue
                
        if isinstance(metadata, dict):
            # 提取重要信息
            title = metadata.get('title', 'N/A')
            description = metadata.get('description', 'N/A')
            word_count = metadata.get('word_count', 'N/A')
            print(f"  标题: {title}")
            print(f"  描述: {description[:100] + '...' if len(str(description)) > 100 else description}")
            print(f"  字数: {word_count}")
    
    # 如果请求向量数据，则返回结果
    result_data = None
    if get_vectors:
        result_data = results
    
    # 完成后卸载集合以释放内存
    collection.release()
    
    return result_data

# 分析向量数据
def analyze_vectors(vectors_data):
    if not vectors_data or len(vectors_data) == 0:
        print("没有可分析的向量数据")
        return
        
    print("\n=== 向量分析 ===")
    
    # 提取向量
    vectors = [item['vector'] for item in vectors_data if 'vector' in item]
    
    if len(vectors) == 0:
        print("没有找到向量数据")
        return
        
    # 转换为numpy数组
    vectors_np = np.array(vectors)
    
    # 基本统计信息
    print(f"向量数量: {len(vectors)}")
    print(f"向量维度: {len(vectors[0])}")
    
    # 计算向量统计数据
    print("\n向量统计:")
    mean_values = np.mean(vectors_np, axis=0)
    std_values = np.std(vectors_np, axis=0)
    min_values = np.min(vectors_np, axis=0)
    max_values = np.max(vectors_np, axis=0)
    
    print(f"  均值范围: {np.min(mean_values):.4f} 到 {np.max(mean_values):.4f}")
    print(f"  标准差范围: {np.min(std_values):.4f} 到 {np.max(std_values):.4f}")
    print(f"  最小值范围: {np.min(min_values):.4f} 到 {np.max(min_values):.4f}")
    print(f"  最大值范围: {np.min(max_values):.4f} 到 {np.max(max_values):.4f}")
    
    # 绘制向量值的直方图
    try:
        plt.figure(figsize=(10, 6))
        # 取第一个向量的所有值绘制直方图
        plt.hist(vectors[0], bins=50)
        plt.title('第一个向量的值分布')
        plt.xlabel('向量值')
        plt.ylabel('频率')
        plt.savefig('vector_histogram.png')
        print("\n已保存向量直方图到 vector_histogram.png")
    except Exception as e:
        print(f"绘制直方图时出错: {e}")

# 执行相似性搜索
def similarity_search(collection_name="anythingllm_my_workspace", search_text=None, top_k=3):
    print("\n=== 相似性搜索 ===")
    
    collection = Collection(name=collection_name)
    collection.load()
    
    # 获取向量维度
    schema = collection.schema
    vector_field = None
    vector_dim = 0
    
    for field in schema.fields:
        if field.dtype == 101:  # 向量数据类型
            vector_field = field.name
            vector_dim = field.params.get('dim')
            break
    
    if not vector_field:
        print("没有找到向量字段")
        collection.release()
        return
    
    print(f"向量字段: {vector_field}")
    print(f"向量维度: {vector_dim}")
    
    # 生成查询向量
    query_vector = None
    if search_text:
        print(f"为搜索文本生成向量: '{search_text}' (此处为占位符)")
        # 在实际应用中，此处应该调用嵌入模型生成向量
        # query_vector = embedding_model.encode(search_text)
        
        # 这里我们只是随机生成一个向量作为示例
        query_vector = np.random.rand(vector_dim).tolist()
    else:
        print("使用随机向量进行搜索")
        query_vector = np.random.rand(vector_dim).tolist()
    
    # 执行搜索
    search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
    results = collection.search(
        data=[query_vector], 
        anns_field=vector_field,
        param=search_params,
        limit=top_k,
        output_fields=["id", "metadata"]
    )
    
    # 处理搜索结果
    print(f"\n搜索结果 (前 {top_k} 条):")
    for i, hits in enumerate(results):
        for j, hit in enumerate(hits):
            print(f"\n结果 {j+1}:")
            print(f"  ID: {hit.id}")
            print(f"  距离: {hit.distance:.4f}")
            
            # 处理元数据
            metadata = hit.entity.get('metadata')
            if isinstance(metadata, str):
                try:
                    metadata = json.loads(metadata)
                except:
                    print(f"  无法解析元数据: {metadata}")
                    continue
                    
            if isinstance(metadata, dict):
                # 提取重要信息
                title = metadata.get('title', 'N/A')
                print(f"  标题: {title}")
    
    # 完成后卸载集合以释放内存
    collection.release()

if __name__ == "__main__":
    if connect_to_milvus():
        # 列出所有集合
        collections = list_all_collections()
        
        # 获取 AnythingLLM 数据，包括向量
        try:
            print("\n获取数据（包括向量）...")
            vector_data = get_anythingllm_data(get_vectors=True)
            
            # 分析向量
            if vector_data:
                analyze_vectors(vector_data)
                
            # 执行相似性搜索
            similarity_search()
            
        except Exception as e:
            print(f"处理数据时出错: {e}")
        
        # 断开连接
        connections.disconnect("default")
        print("\n已断开与 Milvus 的连接")
