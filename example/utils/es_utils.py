from typing import Dict, Any

from elasticsearch import Elasticsearch, AsyncElasticsearch


def get_sync_es_client():
    from config.nacos_config import NACOS_CONFIG

    url = NACOS_CONFIG.es_config.url
    # 将 URL 字符串拆分为列表
    hosts = url.split(",")

    connection_params: Dict[str, Any] = {"hosts": hosts}

    # # CA 证书路径
    # ca_certs = NACOS_CONFIG.es_config.ca_certs
    # if ca_certs is not None and len(ca_certs) > 0:
    #     connection_params["verify_certs"] = True
    #     connection_params["ca_certs"] = ca_certs

    # 认证信息
    username = NACOS_CONFIG.es_config.username
    password = NACOS_CONFIG.es_config.password
    if (
        username is not None
        and len(username) > 0
        and password is not None
        and len(password) > 0
    ):
        connection_params["basic_auth"] = (username, password)

    sync_es_client = Elasticsearch(
        **connection_params,
    )

    sync_es_client.info()  # use sync client so don't have to 'await' to just get info

    return sync_es_client


def get_async_es_client():
    from config.nacos_config import NACOS_CONFIG

    url = NACOS_CONFIG.es_config.url
    # 将 URL 字符串拆分为列表
    hosts = url.split(",")

    connection_params: Dict[str, Any] = {"hosts": hosts}

    # # CA 证书路径
    # ca_certs = NACOS_CONFIG.es_config.ca_certs
    # if ca_certs is not None and len(ca_certs) > 0:
    #     connection_params["verify_certs"] = True
    #     connection_params["ca_certs"] = ca_certs

    # 认证信息
    username = NACOS_CONFIG.es_config.username
    password = NACOS_CONFIG.es_config.password
    if (
        username is not None
        and len(username) > 0
        and password is not None
        and len(password) > 0
    ):
        connection_params["basic_auth"] = (username, password)

    sync_es_client = Elasticsearch(
        **connection_params,
    )

    async_es_client = AsyncElasticsearch(
        **connection_params,
    )

    sync_es_client.info()  # use sync client so don't have to 'await' to just get info

    return async_es_client
