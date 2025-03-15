from itertools import count, cycle, repeat, accumulate, chain
from itertools import combinations, permutations, product
from itertools import groupby


"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列
itertools.permutations("ABCD")
# 产生ABCDE的五选三组合
itertools.combinations("ABCDE", 3)
# 产生ABCD和123的笛卡尔积
itertools.product("ABCD", "123")
# 产生ABC的无限循环序列
itertools.cycle(("A", "B", "C"))



# 1. 无限迭代器
# count: 从某个数字开始无限计数
for i in count(1):
    if i > 5:
        break
    print(i)  # 输出 1, 2, 3, 4, 5

# cycle: 循环遍历序列
colors = ["red", "green", "blue"]
color_cycle = cycle(colors)
for _ in range(5):
    print(next(color_cycle))  # red, green, blue, red, green

# repeat: 重复某个元素
for x in repeat("hello", 3):
    print(x)  # 输出三次 hello

# 2. 组合和排列
items = ["A", "B", "C"]

# 组合
print("2个元素的组合:", list(combinations(items, 2)))
# 输出: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 排列
print("2个元素的排列:", list(permutations(items, 2)))
# 输出: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 笛卡尔积
print("两个序列的笛卡尔积:", list(product(["X", "Y"], [1, 2])))
# 输出: [('X', 1), ('X', 2), ('Y', 1), ('Y', 2)]

# 3. 数据处理
numbers = [1, 2, 3, 4, 5]

# accumulate: 累积求和
print("累积和:", list(accumulate(numbers)))
# 输出: [1, 3, 6, 10, 15]

# chain: 连接多个迭代器
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print("连接序列:", list(chain(list1, list2)))
# 输出: [1, 2, 3, 'a', 'b', 'c']

# 4. 数据分组
items = ["A1", "A2", "B1", "B2", "A3", "B3"]

# 按首字母分组
for key, group in groupby(sorted(items), key=lambda x: x[0]):
    print(f"{key}: {list(group)}")

# 5. 实际应用示例
# 生成日期序列
from datetime import date, timedelta


def date_range(start_date, days):
    return accumulate(repeat(timedelta(days=1), days), func=lambda a, b: start_date + b)


start = date(2024, 1, 1)
dates = list(date_range(start, 5))
print("日期序列:", dates)

# 生成所有可能的颜色组合
colors = ["红", "绿", "蓝"]
sizes = ["大", "中", "小"]
for c, s in product(colors, sizes):
    print(f"{s}{c}")
