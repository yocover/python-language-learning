# 元组数据结构介绍

# 元组是多个元素按照一定顺序构成的序列
# 和list 的不同是，元组是不可变类型，一旦创建，元素不能被修改

# 元组的创建
# 创建元组
tuple1 = ()
tuple2: tuple = tuple()
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ("hello", "world", "python")
tuple5 = (1, 2, 3, 4, 5, "hello", "world")

print("tuple1", tuple1)
print("tuple2", tuple2)
print("tuple3", tuple3)
print("tuple4", tuple4)
print("tuple5", tuple5)

# 使用range创建元组
tuple6 = tuple(range(10))
tuple7 = tuple(range(1, 10, 2))
tuple8 = tuple(range(10, 0, -2))
tuple9 = tuple(range(10))

# 元组中只包含一个元素时，需要在元素后面添加逗号
tuple10 = (1,)

# 元组中只包含一个元素时，需要在元素后面添加逗号
tuple11 = 1


# 元组的方法
print("元组的方法")
tuple12 = (1, 2, 3, 4, 5, 2)
print("tuple12", tuple12)
# count 方法，统计元组中某个元素出现的次数
print("tuple12.count(2)", tuple12.count(2))
# index 方法，查找某个元素在元组中的位置
print("tuple12.index(2)", tuple12.index(2))
# len 方法，返回元组的长度
print("len(tuple12)", len(tuple12))


# 元组的操作
print("\n元组的操作:")
# 1. 元组的索引和切片（与列表相同）
print("tuple3[0]:", tuple12[0])  # 输出第一个元素
print("tuple3[-1]:", tuple12[-1])  # 输出最后一个元素
print("tuple3[1:3]:", tuple12[1:3])  # 切片操作

# 2. 元组的拼接
tuple13 = tuple3 + tuple4
print("tuple3 + tuple4:", tuple13)

# 3. 元组的重复
tuple14 = tuple3 * 2
print("tuple3 * 2:", tuple14)


# 4. 元组的解包
a, b, c = (1, 2, 3)
print("解包后: a =", a, "b =", b, "c =", c)

# 5. 使用*进行解包
first, *rest = tuple3
print("first:", first, "rest:", rest)  # rest会变成列表

# 6. 元组的遍历
print("\n元组的遍历:")
for i in tuple3:
    print(i)

# 7. 检查元素是否在元组中
print("\n检查元素:")
print("'hello' in tuple4:", "hello" in tuple4)
print("'python' in tuple5:", "python" in tuple5)

# 8. 元组与列表的转换
list_from_tuple = list(tuple3)
tuple_from_list = tuple(list_from_tuple)
print("\n转换:", list_from_tuple, tuple_from_list)
