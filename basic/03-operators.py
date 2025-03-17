# 算数运算符
print("-----------算数运算符------------")
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7

# 赋值运算符
print("-----------赋值运算符------------")
a = 10
b = 3
a += b  # a = a + b
print(a)  # 13

# 海像运算符
print("-----------海像运算符------------")

print(a)  # 13
print(a := 10)  # 10 海像运算符

# 比较运算符
print("-----------比较运算符------------")
a = 10
b = 3
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False

# 逻辑运算符
print("-----------逻辑运算符------------")
a = True
b = False
# print(a and b)  # False
# print(a or b)  # True
# print(not a)  # False
# print(not b)  # True

print(a and b)  # False
print(a or b)  # True
print(not a)  # False

# 成员运算符
print("-----------成员运算符------------")
a = "hello"
b = "hello"
c = "he"
print(a in b)  # True

# 解析运行过程
print(a not in b)  # False

print(c not in a)  #

# 身份运算符
print("-----------身份运算符------------")
a = "hello"
b = "hello"
print(a is b)  # True
print(a is not b)  # False

# 位运算符
print("-----------位运算符------------")
a = 10
b = 3
print(a & b)  # 2
print(a | b)  # 11
print(a ^ b)  # 9
print(~a)  # -11
print(a << 1)  # 20
print(a >> 1)  # 5


# 运算符优先级
print("-----------运算符优先级------------")
a = 10
b = 3
c = 2
print(a + b * c)  # 8
print((a + b) * c)  # 36
print(a + (b * c))  # 8

# 索引
print("-----------索引------------")
a = "hello"
a = [1, 2, 3, 4, 5]  # 列表
b = "hello  "  # 字符串
print(a[0])  # 1
print(a[1])  # 2
print(a[2])  # 3
print(a[3])  # 4
print(a[4])  # 5
print(b[0])  # h
print(b[1])  # e
print(b[2])  # l
print(b[3])  # l
print(b[4])  # o

# 切片
print("-----------切片------------")
a = [1, 2, 3, 4, 5]
b = a[0:3]  # 从0开始到3结束
print(b)  # [1, 2, 3]
print(a[1:4])  # [2, 3, 4]
print(a[:3])  # [1, 2, 3]
print(a[3:])  # [4, 5]

# 步长
print("-----------步长------------")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 步长为2
print(a[0:3:2])  # [1, 3] 从0开始到3结束，步长为2
print(a[1:4:2])  # [2, 4] 从1开始到4结束，步长为2
print(a[:3:2])  # [1, 3] 从0开始到3结束，步长为2
print(a[3:])  # [4, 5] 从3开始到结束，步长为2
print(a[::2])  # [1, 3, 5, 7, 9] 从0开始到结束，步长为2

# 列表推导式
print("-----------列表推导式------------")
a = [1, 2, 3, 4, 5]
print([i for i in a])  # [1, 2, 3, 4, 5]
for i in a:
    print(i)

# 字典推导式
print("-----------字典推导式------------")
a = {"a": 1, "b": 2, "c": 3}
print({i: i for i in a})  # {'a': 1, 'b': 2, 'c': 3}

# 示例1 华氏温度转摄氏温度
print("-----------示例1 华氏温度转摄氏温度------------")
f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
# 格式化处理 保留一位小数
print("%.2f华氏度 = %.2f摄氏度" % (f, c))
# %.1f 表示保留一位小数
# %e 表示保留科学计数法
# %g 表示保留科学计数法或保留两位小数
# %s 表示保留字符串
# %c 表示保留字符
# %d 表示保留整数

# 示例2 输入圆的半径计算周长和面积
print("-----------示例2 输入圆的半径计算周长和面积------------")
r = float(input("请输入圆的半径："))
c = 2 * 3.14 * r
s = 3.14 * r * r
print("周长：%.2f" % c)
print("面积：%.2f" % s)

# 使用内置的math
import math

radius = float(input("请输入园的半径: "))

perimeter = 2 * math.pi * radius
# area = math.pi * radius**2  # 平方
area = math.pi * math.pow(radius, 2)  # 平方
print("周长：%.2f" % perimeter)
print("面积：%.2f" % area)

# 使用math.pi
print("-----------使用math.pi------------")
print(math.pi)

# 使用math.pow
print("-----------使用math.pow------------")
print(math.pow(2, 3))  # 2的3次方

# 判断闰年
print("-----------判断闰年------------")
year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")

