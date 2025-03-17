# python 中的序列化和反序列化操作

import json


class Person:
    """用于演示序列化的类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


def serialization_demo():
    person = Person("张三", 18)

    # JSON 序列化（仅支持基本数据类型）
    data = {"name": "张三", "age": 25, "scores": [90, 85, 95]}

    # 序列化到 JSON 字符串
    json_str = json.dumps(data, ensure_ascii=False)
    print(f"JSON 字符串: {json_str}")

    # 从 JSON 字符串反序列化
    restored_data = json.loads(json_str)
    print("反序列化后的数据:", restored_data)

    # # 序列化到文件
    # with open("data.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    # 从文件反序列化
    with open("data.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    print(f"从文件加载的数据: {loaded_data}")


# pickle 和json 的主要区别
# 1. pickle 可以序列化所有的 Python 对象，而 json 只能序列化基本数据类型
# 2. pickle 序列化后的数据是二进制的，而 json 序列化后的数据是字符串
# 3. pickle 序列化后的数据是不可读的，而 json 序列化后的数据是可读的
# json 更安全， pickle 可能有安全隐患

# 根据实际需求选择合适的序列化方式：

# - 如果是 Python 程序内部使用，可以用 pickle
# - 如果需要与其他语言交互，建议用 json
# - 如果数据量很大，可以考虑用 msgpack 等第三方库


if __name__ == "__main__":
    serialization_demo()
