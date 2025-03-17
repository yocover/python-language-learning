# 将一颗色子 投掷6000次，统计每个点数出现的次数

import random

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0


for _ in range(6000):
    face = random.randint(1, 7)
    if face == 1:
        f1 += 1
    if face == 2:
        f2 += 1
    if face == 3:
        f3 += 1
    if face == 4:
        f4 += 1
    if face == 5:
        f5 += 1
    if face == 6:
        f6 += 1

# print(f"1点出现了{f1}次")
# print(f"2点出现了{f2}次")
# print(f"3点出现了{f3}次")
# print(f"4点出现了{f4}次")
# print(f"5点出现了{f5}次")
# print(f"6点出现了{f6}次")


# list 是由一系列元素按照特定顺序构成的数据序列
items1 = ["Python", "Java", "Go", "Kotlin"]  # 列表中的元素可以是不同的数据类型
items2 = list(("Python", "Java", "Go", "Kotlin"))  # 列表中的元素可以是不同的数据类型

# 列表的创建
list1: list[str] = []  # 创建一个空列表
list2: list[int] = list()  # 创建一个空列表
list3 = [1, 2, 3, 4, 5]  # 创建一个包含5个整数的列表
list4 = ["hello"] * 5  # 创建一个包含5个字符串的列表
list5 = [1, 2, 3, 4, 5, "hello", "world"]  # 创建一个包含整数、字符串的列表

# 使用 range
list6 = list(range(1, 20))  # 创建一个包含1到19的列表
list7 = list(range(1, 10, 2))  # 创建一个包含1到9，步长为2的列表
list8 = list(range(10, 0, -2))  # 创建一个包含10到1，步长为-2的列表
list9 = list(range(10))  # 创建一个包含0到9的列表


# 下面两个的区别  list10 是包含"hello"的列表，list11 是包含"hello"的列表
list10 = list("hello")  # 创建一个包含"hello"的列表
list11 = ["hello"]  # 创建一个包含"hello"的列表

print("list1", list1)
print("list2", list2)
print("list3", list3)
print("list4", list4)
print("list5", list5)
print("list6", list6)
print("list7", list7)
print("list8", list8)
print("list9", list9)
print("list10", list10)
print("list11", list11)


# 列表的运算
print("-----------列表的运算-----------")

list12 = [100, 200]
list13 = [6, 7, 8, 9, 10, "hello", "world", True]

# 列表的拼接
print("list12 + list13", list12 + list13)

# 列表的重复
print("list12 * 3", list12 * 3)  # 列表的重复

# 列表的成员运算
print("5 in list12", 5 in list12)
print("5 not in list12", 5 not in list12)
print("100 in list12", 100 in list12)
print("100 not in list12", 100 not in list12)


# 列表的索引
print("-----------列表的索引-----------")
list14 = ["Python", "Java", "Go", "Kotlin"]

# 获取列表中的元素
print("list14[0]", list14[0])
print("list14[1]", list14[1])
print("list14[2]", list14[2])
print("list14[3]", list14[3])

# 列表的索引
print("list14[-1]", list14[-1])
print("list14[-2]", list14[-2])
print("list14[-3]", list14[-3])
print("list14[-4]", list14[-4])

# 列表的方法

print("-----------列表的方法-----------")

# 添加和删除元素

languages = ["Python", "Java", "Go", "Kotlin"]

# 添加元素
languages.append("C++")  # 在列表末尾添加元素
languages.append("1111")  # 在列表末尾添加元素
print("languages", languages)

# 插入元素
languages.insert(0, "C")  # 在指定位置插入元素
languages.insert(2, "C#")  # 在指定位置插入元素
print("languages", languages)

# 删除元素
languages.remove("C++")  # 删除指定元素
print("languages", languages)

# 删除元素
languages.pop()  # 删除最后一个元素
languages.pop(0)  # 删除第一个元素
print("languages", languages)

# 清空列表
languages.clear()
print("languages", languages)

items = ["Python", "Java", "Go", "Kotlin"]
del items[2]  # 删除指定位置的元素
del items[1:3]  # 删除指定位置的元素 1到3
print("items", items)

# 列表的遍历
for item in items:
    print(item)

for index, item in enumerate(items):  # 获取索引和元素
    print(index, item)
    print(items[index])


print("-----------列表的排序-----------")

items = ["Python", "Java", "Go", "Kotlin"]
print("original items", items)
items.reverse()  # 反转列表
print("reverse items", items)

items.sort()  # 排序
print("sort items", items)

items.sort(reverse=True)  # 排序
print("sort items", items)

itmeNumLis = [2, 4, 5, 1, 2, 6]
print("original itmeNumLis", itmeNumLis)
itmeNumLis.sort()
print("sorted itmeNumLis", itmeNumLis)  # 排序

itmeNumLis.sort(reverse=True)  # 降序排序
print("reverse sorted itmeNumLis", itmeNumLis)  # 排序
