from typing import Optional, List
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

from config.nacos_config import init_nacos_config

# 创建 FastAPI 实例
app = FastAPI()


# 定义数据模型
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# 基本路由
@app.get("/")
async def read_root():
    return {"Hello": "World", "Name": "FastAPI", "Version": "0.1.0"}


# 路径参数
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# POST 请求处理
@app.post("/items/")
async def create_item(item: Item):
    return item


# 查询参数验证
@app.get("/products/")
async def read_products(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    return {"skip": skip, "limit": limit}


# 请求体和路径参数组合
@app.put("/items/{item_id}")
async def update_item(item_id: int = Path(..., ge=0), item: Item = Body(...)):
    return {"item_id": item_id, "item": item}


# 处理表单数据
from fastapi import Form


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


# 文件上传
from fastapi import File, UploadFile


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


# 添加配置类
class ApplicationConfig:
    def __init__(self):
        self.web_host = "0.0.0.0"
        self.web_port = 8000


# 添加启动代码
if __name__ == "__main__":
    import uvicorn
    import os
    from types import SimpleNamespace

    # 获取当前文件夹所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建配置文件的绝对路径
    config_path = os.path.join(current_dir, "config", "config.yml")

    # 使用 SimpleNamespace 创建一个类似对象
    args = SimpleNamespace(config_file=config_path)

    init_nacos_config(args)

    from config.nacos_config import NACOS_CONFIG, NacosConfig

    config = uvicorn.Config(
        app,
        host=NACOS_CONFIG.application_config.web_host,
        port=NACOS_CONFIG.application_config.web_port,
        reload=True,
    )
    server = uvicorn.Server(config)
    server.run()
