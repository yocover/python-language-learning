from pymilvus import connections, Collection, utility
import random
import numpy as np

# 连接到 Milvus 服务
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

# 创建集合
def create_collection(collection_name, dim):
    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)
        print(f"删除已存在的集合: {collection_name}")
    
    from pymilvus import CollectionSchema, FieldSchema, DataType
    
    # 定义集合字段
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=dim),
        FieldSchema(name="color", dtype=DataType.VARCHAR, max_length=10)
    ]
    
    # 创建集合
    schema = CollectionSchema(fields=fields, description=f"Test collection with {dim}-dimensional vectors")
    collection = Collection(name=collection_name, schema=schema)
    
    # 创建索引
    index_params = {
        "metric_type": "L2",  # 欧氏距离
        "index_type": "IVF_FLAT",  # 索引类型
        "params": {"nlist": 128}  # 索引参数
    }
    collection.create_index(field_name="vector", index_params=index_params)
    
    print(f"创建集合 '{collection_name}' 并建立索引")
    return collection

# 插入数据
def insert_data(collection, num_entities=10, dim=128):
    colors = ["red", "green", "blue", "yellow", "purple"]
    entities = [
        # 随机向量
        [np.random.random([dim]).astype(np.float32) for _ in range(num_entities)],
        # 随机颜色
        [random.choice(colors) for _ in range(num_entities)]
    ]
    
    collection.insert([entities[0], entities[1]])
    collection.flush()
    print(f"插入了 {num_entities} 条向量数据")

# 搜索向量
def search_vectors(collection, dim=128, top_k=3):
    collection.load()
    
    # 生成随机搜索向量
    search_vectors = [np.random.random([dim]).astype(np.float32)]
    
    # 搜索参数
    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10}  # 搜索时使用的聚类数
    }
    
    # 执行搜索
    results = collection.search(
        data=search_vectors,
        anns_field="vector",
        param=search_params,
        limit=top_k,
        expr=None
    )
    
    # 打印结果
    print(f"\n搜索结果 (top {top_k}):")
    for i, result in enumerate(results):
        print(f"搜索向量 {i}:")
        for j, entity in enumerate(result):
            print(f"  {j}. ID: {entity.id}, 距离: {entity.distance}")

if __name__ == "__main__":
    # 参数设置
    COLLECTION_NAME = "test_collection"
    DIMENSION = 128  # 向量维度
    
    # 连接到 Milvus
    if connect_to_milvus():
        # 创建集合
        collection = create_collection(COLLECTION_NAME, DIMENSION)
        
        # 插入数据
        insert_data(collection, num_entities=20, dim=DIMENSION)
        
        # 搜索
        search_vectors(collection, dim=DIMENSION, top_k=5)
        
        # 显示集合统计信息
        print(f"\n集合统计: {collection.num_entities} 实体")
    else:
        print("无法连接到 Milvus 服务，请检查服务是否运行。") 