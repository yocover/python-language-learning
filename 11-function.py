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


# 递归函数
def factorial(n):
    """计算阶乘"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("5的阶乘:", factorial(5))


# 9. 生成器函数
print("\n=== 生成器函数 ===")


def fibonacci(n):
    """生成斐波那契数列的生成器"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print("斐波那契数列:")
for num in fibonacci(10):
    print(num, end=" ")
print()

# 10. 闭包
print("\n=== 闭包 ===")


def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = create_counter()
print("计数器:", counter())
print("计数器:", counter())
print("计数器:", counter())

from math import sqrt as sq


def is_prime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(sq(n)) + 1):
        if n % i == 0:
            return False
    return True


print("素数判断:", is_prime(17))

# 位置参数


def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


print("判断三角形:", make_judgement(3, 4, 5))
# 通过位置参数传递参数
print(make_judgement(a=3, c=5, b=4))


# 强制位置参数
def force_position(a, b, /, c):
    """强制使用位置参数"""
    return a + b + c


print("强制位置参数:", force_position(1, 2, 3))
# print(force_position(a=1, b=2, c=3))  # 报错


# 命名关键字参数
def named_keyword(a, *, b, c):
    """使用命名关键字参数"""
    return a + b + c


print("命名关键字参数:", named_keyword(1, b=2, c=3))


# print(named_keyword(1, 2, 3))  # 报错
# 关键字参数
def keyword_args(**kwargs):
    """使用关键字参数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("关键字参数:")
keyword_args(name="张三", age=18)


# 函数的默认参数
def greet(name, message="你好"):
    """使用默认参数"""
    return f"{message}, {name}!"


print("默认参数:", greet("李四"))


# 可变参数
# 所谓可变参数指的是 在调用函数时可以 传入0个或任意多个参数
# 调用函数的时候，传入的n个参数会组装成一个n元组赋值给args
# 如果一个参数都没有传入，那么args就是一个空元组
def sum_numbers(*args):
    """使用可变参数"""
    return sum(args)


print("可变参数:", sum_numbers(1, 2, 3, 4, 5))
print("可变参数:", sum_numbers())


# 参数列表中的 **kwargs 可接收0或者任意多个关键字参数
# 调用函数时传入的关键字会组装成一个字 典赋值给kwargs
def foo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


foo(1, 2, 3, a=1, b=2, age=3)


def foo():
    print("hello, world!")


# 如果函数重名，那么后面的函数会覆盖前面的函数
def foo():
    print("goodbye, world!")


foo()

# 用模块管理函数
# 可以把函数放在一个模块中，然后在其他地方引用这个模块
# 这样可以避免函数名冲突，也可以方便地管理函数
