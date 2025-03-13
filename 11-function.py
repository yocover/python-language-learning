# 函数
# 函数的定义
print("函数的定义:")


def greet(name):
    # 函数文档
    """简单的问候函数"""
    # 函数体 (函数体缩进) f 为函数返回值
    return f"你好, {name}!"


print(greet("张三"))
# 查看函数文档
print(greet.__doc__)


# 参数类型
print("参数类型:")


def add(a, b):
    """加法函数"""
    return a + b


num = add(1, 2)
print(num)

import math


# 单个返回值
def square(n):
    return math.pow(n, 2)


print(square(2))


# 返回多个值
def get_coordinates():
    return 1, 2, 3


x, y, z = get_coordinates()
print(x, y, z)


# 返回None
def do_nothing():
    pass


print(do_nothing())


# 作用域
print("作用域:")
global_var = "全局变量"


def scope_test():

    # 在使用全局ote之前，必须先声明变量为global
    global global_var

    local_var = "局部变量"
    print("在函数内部:", local_var)
    print("在函数内部:", global_var)

    # 修改全局变量

    global_var = "修改后的全局变量"


scope_test()
# print("在函数外部:", local_var)  # 报错
print("在函数外部:", global_var)

# 函数作为对象
print("函数作为对象:")
# 把函数赋值给变量
func1 = greet
print("函数赋值给变量:", func1("张三"))


# 函数作为参数
def apply_operation(func, x):
    return func(x)


def double(n):
    return n * 2


print("函数作为参数:", apply_operation(double, 3))  # 6

# 匿名函数
print("匿名函数:")
square = lambda x: x * x
print("匿名函数:", square(3))  # 9

# 在列表排序中使用lambda
students = [("张三", 85), ("李四", 92), ("王五", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("使用lambda排序:", sorted_students)


# 装饰器
print("装饰器:")


def log_function(func):
    def wrapper(*args, **kwargs):
        print("调用函数:", func.__name__)
        result = func(*args, *kwargs)
        print("函数执行完毕")
        return result

    return wrapper


@log_function
def calculate_sum(a, b):
    return a + b

print("装饰器示例")
print(calculate_sum(1, 2))


