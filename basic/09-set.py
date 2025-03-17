# python 中的 set 介绍

# 创建 set
# 集合是一个无序的，数据不重复的数据集合
# 集合中的元素必须是不可变类型 数字、字符串、元组

# 创建空集合

print("-------------集合的创建--------------")
set1: set[int] = set()
# empty_set = {} # 空集合不能使用 {} 创建，只能使用 set() 创建
# print(empty_set) # 输出：注意使用 {} 创建的是空字典，不是空集合

print(set1)  # 输出：set()

set2 = {1, 2, 3, 4, 5, 2, 3}  # 自动去重
print("set2:", set2)  # 输出：set2: {1, 2, 3, 4, 5}

# 2. 集合的基本操作
print("\n=== 集合的基本操作 ===")
# 添加元素
set1.add(1)
print("set1.add(1):", set1)

# 移除元素
set1.remove(1)
print("set1.remove(1):", set1)

# 安全的移除元素
set1.discard(2)
print("set1.discard(2):", set1)

# 随机移除元素
for item in range(0, 10):
    set1.add(item)
# end for

popped = set1.pop()
print("随机移除的元素:", popped)
print("移除后的集合:", set1)

# 晴空集合
set1.clear()
print("晴空集合:", set1)

# 3. 集合的数学运算
print("\n=== 集合的数学运算 ===")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 并集
union_AB = A.union(B)
print("并集:", union_AB)
print("A | B:", A | B)

# 交集
intersection_AB = A.intersection(B)
print("交集:", intersection_AB)
print("A & B:", A & B)

# 差集
difference_AB = A.difference(B)
print("差集:", difference_AB)
print("A - B:", A - B)

# 对称差集
symmetric_difference_AB = A.symmetric_difference(B)
print("对称差集:", symmetric_difference_AB)
print("A ^ B:", A ^ B)

# 4. 集合的关系运算
print("\n=== 集合的关系运算 ===")
A = {1, 2}
B = {1, 2, 3, 4, 5}

# issubset() 判断 A 是否是 B 的子集
print("A.issubset(B):", A.issubset(B))
print("A <= B:", A <= B)

# issuperset() 判断 A 是否是 B 的超集
print("A.issuperset(B):", A.issuperset(B))
print("A >= B:", A >= B)

# isdisjoint() 判断 A 和 B 是否是无交集
print("A.isdisjoint(B):", A.isdisjoint(B))
print("A & B:", A & B)

# 5. 集合推导式
print("\n=== 集合推导式 ===")
# 创建一个平方数集合
squares = {x**2 for x in range(10)}
print("平方数集合:", squares)

# 6. 集合的应用场景
print("\n=== 集合的应用场景 ===")
# 去重
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print("列表去重:", unique_numbers)

# 成员检测
fruits = {"apple", "banana", "orange"}
print("'apple'是否在集合中:", "apple" in fruits)

# 数据统计
text = "hello world"
unique_chars = set(text)
print("不重复字符个数:", len(unique_chars))
print("不重复字符:", unique_chars)

# 集合的特点
# 无序性 集合中的元素没有固定顺序
# 唯一性 集合中的元素不能重复
# 可变形 可以添加或者删除元素
# 不可索引 不能通过索引访问元素
# 集合不支持索引运算算
# 集合的成员运算在性能上要优于列表成员的元素安

# 集合的元素
# 需要注意的是 集合的元素必须都是 hashable 的
# 所谓hashable 指的是 能够计算出 哈希码的数据类型
# 通常不可变类型都是 hashable 类型
# 如数字、字符串、元组、布尔值等
# ashable（可哈希）类型

# 示例：可哈希类型和不可哈希类型
print("\n=== 可哈希类型演示 ===")
# 可哈希类型示例
hashable_set = {1, "hello", (1, 2, 3)}
print("可哈希类型集合:", hashable_set)

# 不可哈希类型示例
try:
    unhashable_set = {[1, 2, 3], {"a": 1}}
except TypeError as e:
    print("不可哈希类型集合:", e)

# 验证对象是否克哈希
print("\n=== 验证对象是否可哈希 ===")


def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False


print("1 是否可哈希:", is_hashable(1))
print("'hello' 是否可哈希:", is_hashable("hello"))

# 将 collections 改为 collections.abc
from collections.abc import Hashable


# 验证对象是否可哈希
print("整数是否可哈希:", isinstance(42, Hashable))
print("字符串是否可哈希:", isinstance("hello", Hashable))
print("列表是否可哈希:", isinstance([1, 2, 3], Hashable))

# 不可哈希的类型
# 列表 lsit
# 字典 dict
# 集合 set

# 不可变集合
fset1 = frozenset({1, 2, 3})
fset2 = frozenset(range(1, 20))
print("fset1:", fset1)
print("fset2:", fset2)
