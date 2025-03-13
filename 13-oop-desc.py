# python 面向对象编程

import time


class Student:

    # 类属性 这样外部就不可以动态添加其他属性
    # 表明该类的对象只能有name 和 age 两个属性
    __slots__ = ("name", "__age")

    def __init__(self, name, age):
        print("__init__ 被调用")

        # 公有属性
        self.name = name

        # 私有属性
        self.__age = age

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")

    def play(self):
        print(f"{self.name}正在玩游戏")


# 类方法和静态方法以及对象方法
# 类方法
# 类方法的第一个参数是cls 表示类本身

# 静态方法
# 静态方法的参数没有要求

# 对象方法
# 对象方法的第一个参数是self 表示对象本身


class Trangle:

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b
    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(静态方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property # 把一个方法变成属性
    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


def main():
    # stu1 = Student("张三", 23)  # 构造函数
    # stu1.study("python")
    # time.sleep(1)
    # stu1.play()

    # # stu1.sex = "男"

    # stu2 = Student("李四", 32)
    # stu2.study("java")

    # print(stu1)
    # print(stu2)
    # print(hex(id(stu1)), hex(id(stu2)))

    # stu3 = stu1
    # print(stu3)

    # # 通过类.方法调用方法
    # # 第一个参数是接收消息的对象
    # # 第二个参数是函数的参数
    # Student.play(stu1)

    # # print(stu1.__age)
    # # print(stu1.sex)

    trangle = Trangle(3, 4, 5)
    print(trangle.perimeter())
    # print(trangle.area())

    print(trangle.area)

    valid = Trangle.is_valid(3, 4, 5)
    print(valid)


if __name__ == "__main__":
    main()
