# Python中的装饰器示例


# 详细解释
# 装饰器是一个函数，它接收一个函数作为参数，并返回一个新函数
# 可以在不修改原函数代码的情况下 增加新功能

# 常见用途
# 日志记录
# 性能分析
# 缓存
# 权限验证
# 输入验证
# 数据转换
# 重试机制
# 同步异步转换
# 单元测试
# 插件系统
# 框架扩展
# 代码生成
# 代码重构


# 使用场景
# web框架中的路由装饰器
# 身份验证
# 日志系统
# 性能监控
# 缓存机制
# 装饰器是python 中 非常强大的特性，它允许我们以一种优雅的方式扩展和修改函数的行为
# 而不需要直接修改函数的源代码


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
