from typing import Optional

from pydantic import BaseModel


class ElasticSearchConfig(BaseModel):
    url: str = "localhost"
    port: int = 9200
    username: Optional[str] = None
    password: Optional[str] = None
