import re

# 1. 基本匹配
text = "Python是一门很棒的编程语言，发布于1991年"
# 查找所有数字
numbers = re.findall(r'\d+', text)
print("数字:", numbers)  # 输出: ['1991']

# 2. 匹配模式
phone = "13812345678"
# 匹配手机号码格式
is_phone = re.match(r'^1[3-9]\d{9}$', phone)
print("是否是手机号:", bool(is_phone))  # 输出: True

# 3. 替换文本
text = "我的邮箱是 example@gmail.com 和 test@qq.com"
# 替换邮箱为 [邮箱]
new_text = re.sub(r'[\w\.-]+@[\w\.-]+', '[邮箱]', text)
print("替换后:", new_text)

# 4. 分割文本
text = "Python;Java,C++|JavaScript"
# 使用多个分隔符分割
languages = re.split(r'[;,|]', text)
print("编程语言:", languages)

# 5. 常用正则表达式模式
patterns = {
    '邮箱': r'^[\w\.-]+@[\w\.-]+\.\w+$',
    '手机号': r'^1[3-9]\d{9}$',
    '日期': r'\d{4}-\d{1,2}-\d{1,2}',
    'URL': r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s]*',
    '中文字符': r'[\u4e00-\u9fa5]+'
}

# 测试文本
test_text = """
电话: 13812345678
邮箱: test@example.com
网址: https://www.python.org
日期: 2024-01-15
中文: 你好，Python！
"""

# 使用不同模式进行匹配
for name, pattern in patterns.items():
    matches = re.findall(pattern, test_text)
    print(f"{name}匹配结果:", matches)