# 元组的使用场景示例

# 1. 不可变数据的存储
point = (10, 20)  # 二维坐标点
rgb_color = (255, 0, 0)  # 红色的RGB值
print("坐标点:", point)
print("RGB颜色:", rgb_color)

# 2. 作为字典的键
locations = {(39.9, 116.4): "北京", (31.2, 121.5): "上海", (23.1, 113.3): "广州"}
print("\n使用元组作为字典键:")
print("北京的坐标:", [(k, v) for k, v in locations.items() if v == "北京"][0][0])


# 3. 函数的多返回值
def get_user_info():
    return "张三", 25, "北京"


name, age, city = get_user_info()
print("\n函数多返回值:")
print(f"姓名: {name}, 年龄: {age}, 城市: {city}")


# 4. 数据的安全传递
def process_data(data):
    # 如果data是列表，可能会被函数内部修改
    # 如果data是元组，保证不会被修改
    print("处理数据:", data)
    # 尝试修改会报错: data[0] = 100


safe_data = (1, 2, 3, 4, 5)
process_data(safe_data)

# 5. 命名元组
from collections import namedtuple

# 创建一个命名元组类型
Person = namedtuple("Person", ["name", "age", "city"])

# 创建命名元组实例
person1 = Person("李四", 30, "上海")
print("\n命名元组:")
print(f"姓名: {person1.name}, 年龄: {person1.age}, 城市: {person1.city}")
print(f"索引访问: {person1[0]}, {person1[1]}, {person1[2]}")

# 6. 元组的不可变性与嵌套元组
nested_tuple = (1, 2, [3, 4])
print("\n嵌套元组:", nested_tuple)
# 元组本身不可变，但其中的可变元素（如列表）可以修改
nested_tuple[2].append(5)
print("修改后的嵌套元组:", nested_tuple)

# 打包和解包

# 打包
a = 1, 2, 3
b = 4, 5, 6
print("\n打包:", a, b)
print("type(a):", type(a))
print("type(b):", type(b))
print("解包:", *a, *b)

c = *a, *b
print("打包和解包:", c)
print("type(c):", type(c))

# 交换变量的值
print("\n交换变量的值:")
m = 111
n = 222
f = 444
print("初始值:", m, n, f)
m, n, f = n, m, m
print("交换后值:", m, n, f)


# 元组和列表的比较

# 元组是不可变类型，不可变类型适合多线程环境，因为它降低了并发访问变量的
# 同步化开销
# 元素是不可变类型，通常不可变类型，在创建时间上由于对应的可变类型
#

import timeit

print("\n元组和列表的比较:")
print("元组和列表的创建时间:")
print(
    "元组创建时间: %.6f 秒"
    % timeit.timeit(
        "(1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)", number=1000000
    )
)
print(
    "列表创建时间: %.6f 秒"
    % timeit.timeit(
        "[1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]", number=1000000
    )
)
