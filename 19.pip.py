# 包管理工具 pip 的使用
# 安装类型提示包
# pip install types-requests
import requests

# Type-annotated response
resp: requests.Response = requests.get(
    "http://api.tianapi.com/guonei/?key=APIKey&num=10"
)
if resp.status_code == 200:
    print(resp.json())
