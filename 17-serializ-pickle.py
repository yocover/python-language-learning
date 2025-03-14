# python 中的序列化和反序列化操作


# 使用内置的pickle 实现
import pickle


class Person:
    """用于演示序列化的类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


def serialization_demo():
    person = Person("张三", 18)

    # 序列化道文件
    try:
        with open("person.pkl", "wb") as f:
            pickle.dump(person, f)
            print("序列化成功")
    except Exception as e:
        print("序列化失败", e)

    # 序列化道字节串
    try:
        person_bytes = pickle.dumps(person)
        print(f"序列化后的字节串: {person_bytes}")

        # 从字节串反序列化
        restored_person = pickle.loads(person_bytes)
        print(f"从字节串反序列化的对象: {restored_person}")
    except Exception as e:
        raise e
    # end try


if __name__ == "__main__":
    serialization_demo()
