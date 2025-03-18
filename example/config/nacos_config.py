from typing import Optional
import yaml

from model.config.es_config import ElasticSearchConfig
from model.config.application_config import ApplicationConfig

# 配置信息

# 定义全局变量
NACOS_CONFIG = None


def parse_elasticsearch_config(config_data):
    elasticsearch_config_dict = config_data["elasticsearch"]
    elasticsearch_config = ElasticSearchConfig(
        url=elasticsearch_config_dict["url"],
        username=elasticsearch_config_dict["username"],
        password=elasticsearch_config_dict["password"],
        ca_certs=elasticsearch_config_dict["caCerts"],
    )
    return elasticsearch_config


def parse_application_config(config_data):
    application_config_dict = config_data["application"]
    application_config = ApplicationConfig(
        web_host=application_config_dict["webHost"],
        web_port=application_config_dict["webPort"],
        supported_file_type_list=application_config_dict["supportedFileTypeList"],
        supported_file_suffix_list=application_config_dict["supportedFileSuffixList"],
        file_size_limit=application_config_dict["fileSizeLimit"],
    )
    return application_config


def load_config_from_yaml(yaml_file_path: str):
    """从YAML文件加载配置"""
    with open(yaml_file_path, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)
    return config_data


def init_nacos_config(args):
    global NACOS_CONFIG
    NACOS_CONFIG = NacosConfig(args.config_file)
    NACOS_CONFIG.init_config(args.config_file)


class NacosConfig:

    _group: str
    _environment: str
    config_data: dict
    es_config: Optional[ElasticSearchConfig] = None
    application_config: Optional[ApplicationConfig] = None

    def __init__(self, config_file: Optional[str] = None):
        print("初始化Nacos配置")

    def init_config(self, config_file: str):

        # 加载配置文件
        config_data = load_config_from_yaml(config_file)

        # 通过路径，解析出数据
        self.application_config = parse_application_config(config_data)
        self.es_config = parse_elasticsearch_config(config_data)
