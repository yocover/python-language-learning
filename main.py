from typing import Optional, List
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

from example.config.nacos_config import init_nacos_config


# 导入 ES 工具函数
from example.utils.es_utils import get_sync_es_client, get_async_es_client

# 创建 FastAPI 实例
# 创建主 FastAPI 应用
app = FastAPI(
    title="主应用 API", description="主 FastAPI 应用，挂载了 ES 子应用", version="1.0.0"
)
from example.es_demo_pkg.es_demo import app as es_app


# 将 es_demo 应用挂载到主应用的 /es 路径下
app.mount("/es", app=es_app)


# 主应用的路由
@app.get("/")
async def read_root():
    return {"message": "这是主应用", "es_demo": "访问 /es 路径可以使用 ES 相关功能"}


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

    from example.config.nacos_config import NACOS_CONFIG

    # 获取同步客户端
    app.sync_es_client = get_sync_es_client()
    # 获取异步客户端
    app.async_es_client = get_async_es_client()

    print("Elasticsearch 客户端初始化成功")

    config = uvicorn.Config(
        app,
        host=NACOS_CONFIG.application_config.web_host,
        port=NACOS_CONFIG.application_config.web_port,
        reload=True,
    )
    server = uvicorn.Server(config)
    server.run()
