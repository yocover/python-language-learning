# Python 一等函数示例

# 1. 函数可以赋值给变量
def greet(name):
    return f"你好, {name}!"

# 将函数赋值给变量
my_function = greet
print("函数赋值示例:", my_function("张三"))

# 2. 函数可以作为参数传递
def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x * x

# 函数作为参数使用
print("\n函数作为参数示例:")
print("双倍:", apply_operation(double, 5))
print("平方:", apply_operation(square, 5))

# 3. 函数可以作为返回值
def get_operation(operation_type):
    def add(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y
    
    if operation_type == "add":
        return add
    else:
        return multiply

# 获取并使用返回的函数
add_func = get_operation("add")
mult_func = get_operation("multiply")
print("\n函数作为返回值示例:")
print("加法:", add_func(3, 4))
print("乘法:", mult_func(3, 4))

# 4. 高阶函数示例
# 示例1：map 函数
numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print("\n高阶函数 map 示例:")
print("原列表:", numbers)
print("加倍后:", doubled)

# 示例2：filter 函数
def is_even(n):
    return n % 2 == 0

filtered = list(filter(is_even, numbers))
print("\n高阶函数 filter 示例:")
print("原列表:", numbers)
print("偶数:", filtered)

# 示例3：自定义高阶函数
def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

# 组合两个函数
double_then_square = compose(square, double)
print("\n函数组合示例:")
print("先加倍再平方:", double_then_square(3))  # (3*2)^2 = 36

# 示例4：装饰器（高阶函数的常见应用）
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数返回: {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y

print("\n装饰器示例:")
add(5, 3)

# 示例5：带参数的高阶函数
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"你好, {name}!")
    return "完成"

print("\n带参数的高阶函数示例:")
greet("李四")

# 示例6：函数作为数据结构中的元素
function_list = [double, square, lambda x: x + 1]
print("\n函数列表示例:")
for func in function_list:
    print(f"{func.__name__ if hasattr(func, '__name__') else 'lambda'} 的结果:", func(5))