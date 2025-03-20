from functools import lru_cache
import time

def timer(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 执行时间: {(end - start):.4f} 秒")
        return result
    return wrapper

# 使用缓存的函数
@lru_cache(maxsize=128)
def expensive_operation(n: int) -> float:
    """模拟一个耗时的操作"""
    time.sleep(1)  # 模拟耗时操作
    return n ** 2

def main():
    print("=== 函数缓存示例 ===")
    
    # 第一次调用
    print("\n第一次调用 expensive_operation(2):")
    result1 = expensive_operation(2)
    print(f"结果: {result1}")
    print(f"缓存信息: {expensive_operation.cache_info()}")
    
    # 第二次调用（使用缓存）
    print("\n第二次调用 expensive_operation(2):")
    result2 = expensive_operation(2)
    print(f"结果: {result2}")
    print(f"缓存信息: {expensive_operation.cache_info()}")
    
    # 使用不同的参数
    print("\n使用新参数调用 expensive_operation(3):")
    result3 = expensive_operation(3)
    print(f"结果: {result3}")
    print(f"缓存信息: {expensive_operation.cache_info()}")
    
    # 再次使用第一个参数
    print("\n再次使用第一个参数 expensive_operation(2):")
    result4 = expensive_operation(2)
    print(f"结果: {result4}")
    print(f"缓存信息: {expensive_operation.cache_info()}")

if __name__ == "__main__":
    main() 