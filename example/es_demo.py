from fastapi import FastAPI, HTTPException
from elasticsearch import Elasticsearch, NotFoundError
from pydantic import BaseModel

app = FastAPI()

# 添加错误处理的ES连接
try:
    es = Elasticsearch(
        ["http://localhost:9200"],
        retry_on_timeout=True,  # 超时重试
        max_retries=3,  # 最大重试次数
    )
    # 验证连接
    if not es.ping():
        raise ValueError("连接到 Elasticsearch 失败")
except Exception as e:
    print(f"Elasticsearch 连接错误: {e}")
    # 当连接失败时，创建一个空的Elasticsearch实例
    es = Elasticsearch()


# 添加健康检查接口
@app.get("/health")
async def health_check():
    if es and es.ping():
        # 获取集群健康状态
        health = es.cluster.health()
        # 获取索引信息
        indices = es.indices.get_alias()
        return {
            "status": "healthy",
            "cluster_health": health,
            "indices": list(indices.keys()),
        }
    return {"status": "unhealthy", "message": "Elasticsearch 未连接"}


class Document(BaseModel):
    title: str
    content: str


@app.post("/documents/")
async def create_document(doc: Document):
    # 创建文档
    response = es.index(
        index="my_index", document={"title": doc.title, "content": doc.content}
    )
    return response


@app.get("/search/")
async def search_documents(query: str):
    # 搜索文档
    response = es.search(
        index="my_index",
        body={
            "query": {"multi_match": {"query": query, "fields": ["title", "content"]}}
        },
    )
    return response["hits"]["hits"]


# 添加一个新的路由来获取所有文档
@app.get("/documents/")
async def get_all_documents():
    response = es.search(
        index="my_index", body={"query": {"match_all": {}}}  # 匹配所有文档
    )
    return response["hits"]["hits"]


# 添加一个路由来获取指定ID的文档
@app.get("/documents/{doc_id}")
async def get_document(doc_id: str):
    try:
        response = es.get(index="my_index", id=doc_id)
        return response["_source"]
    except Exception as e:
        return {"error": f"Document not found: {str(e)}"}


@app.get("/search/exact/")
async def exact_search(query: str):
    """精确匹配搜索"""
    response = es.search(
        index="my_index",
        body={
            "query": {
                "term": {
                    "title.keyword": query  # 精确匹配标题
                }
            }
        }
    )
    return response["hits"]["hits"]

@app.get("/search/fuzzy/")
async def fuzzy_search(query: str):
    """模糊搜索"""
    response = es.search(
        index="my_index",
        body={
            "query": {
                "fuzzy": {
                    "title": {
                        "value": query,
                        "fuzziness": "AUTO"  # 自动确定模糊度
                    }
                }
            }
        }
    )
    return response["hits"]["hits"]

@app.get("/search/wildcard/")
async def wildcard_search(query: str):
    """通配符搜索"""
    response = es.search(
        index="my_index",
        body={
            "query": {
                "wildcard": {
                    "title": f"*{query}*"  # 包含查询词的内容
                }
            }
        }
    )
    return response["hits"]["hits"]

@app.get("/search/advanced/")
async def advanced_search(query: str, min_score: float = 0.5):
    """高级搜索"""
    response = es.search(
        index="my_index",
        body={
            "query": {
                "bool": {
                    "should": [
                        {"match": {"title": query}},
                        {"match": {"content": query}},
                        {"fuzzy": {"title": {"value": query, "fuzziness": "AUTO"}}},
                    ],
                    "minimum_should_match": 1
                }
            },
            "min_score": min_score
        }
    )
    return response["hits"]["hits"]
