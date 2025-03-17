from typing import List

from pydantic import BaseModel


class ApplicationConfig(BaseModel):
    web_host: str
    web_port: int
    supported_file_type_list: List[str]
    supported_file_suffix_list: List[str]
    file_size_limit: int
