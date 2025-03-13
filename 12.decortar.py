# Python中的装饰器示例

# ... 现有代码 ...

# 装饰器详细示例
print("\n=== 装饰器详细示例 ===")


# 1. 基本装饰器
def simple_decorator(func):
    def wrapper():
        print("装饰器：函数执行前")
        func()
        print("装饰器：函数执行后")

    return wrapper


@simple_decorator
def hello():
    print("Hello, World!")


print("基本装饰器示例：")
hello()


quit()


# 2. 带参数的装饰器
def logger(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} 开始执行: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{prefix} 执行完成: {func.__name__}")
            return result

        return wrapper

    return decorator


@logger("DEBUG")
def add_numbers(a, b):
    return a + b


print("\n带参数的装饰器示例：")
print("计算结果:", add_numbers(3, 5))


# 3. 多个装饰器
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"

    return wrapper


def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"

    return wrapper


@bold
@italic
def greet():
    return "Hello, World!"


print("\n多个装饰器示例：")
print(greet())

# 4. 保留原函数信息的装饰器
from functools import wraps


def timing_decorator(func):
    @wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行时间: {end - start:.4f} 秒")
        return result

    return wrapper


@timing_decorator
def slow_function():
    """这是一个耗时的函数"""
    import time

    time.sleep(1)
    return "完成"


print("\n保留函数信息的装饰器示例：")
print(slow_function())
print("函数名称:", slow_function.__name__)
print("函数文档:", slow_function.__doc__)
