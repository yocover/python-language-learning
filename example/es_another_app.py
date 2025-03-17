from elasticsearch import Elasticsearch

# 连接到同一个 Elasticsearch 服务
es = Elasticsearch(["http://localhost:9200"])

def search_documents(query: str):
    """这是另一个应用程序中的搜索函数"""
    response = es.search(
        index="my_index",  # 可以访问同一个索引
        body={
            "query": {
                "match": {
                    "content": query
                }
            }
        }
    )
    return response["hits"]["hits"]

# 测试代码
if __name__ == "__main__":
    # 搜索之前创建的文档
    results = search_documents("测试")
    for hit in results:
        print(f"文档ID: {hit['_id']}")
        print(f"标题: {hit['_source']['title']}")
        print(f"内容: {hit['_source']['content']}")
        print("---")