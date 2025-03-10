# python 中的变量
# 变量的定义


# 整形
print("-----------整型------------")
print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)  # 十进制整数
print(0x100)  # 十六进制整数


# 浮点型
print("-----------浮点型------------")
print(123.456)  # 数学写法
print(1.23456e2)  # 科学计数法

# 字符串型
print("-----------字符串------------")
print("hello world")

# 布尔型
print("-----------布尔型------------")
print(True)
print(10 == 2)
print("0" == 0)

"""
使用变量保存数据并进行加减乘除运算
"""
print("-----------运算------------")
a = 45  # 定义变量a，赋值45
b = 12  # 定义变量b，赋值12
print(a, b)  # 45 12
print(a + b)  # 57
print(a - b)  # 33
print(a * b)  # 540
print(a / b)  # 3.75

# 类型检查
print("-----------类型检查------------")
c = "123"
d = 123
e = 12.34
f = True
print(type(a))  # <class 'int'>
print(type(c))  # <class 'str'>
print(type(e))  # <class 'float'>
print(type(f))  # <class 'bool'>

# 类型转换
print("-----------类型转换------------")
print(int(c))  # 123
print(float(d))  # 123.0
print(str(e))  # "12.34"
print(bool(f))  # True

# 类型转换示例
print("-----------类型转换示例------------")
# 1. 整型转换为浮点型
print(float(123))  # 123.0
# 2. 浮点型转换为整型
print(int(123.456))  # 123
# 3. 字符串转换为整型
print(int("123", base=10))  # 123
print(int("123", base=8))  # 83 八进制
print(int("123", base=16))  # 291 十六进制
print(chr(97))  # a 将数字转换为对应的字符
print(ord("a"))  # 97 将字符转换为对应的数字
# 4. 字符串转换为浮点型
print(float("12.34"))  # 12.34
# 5. 字符串转换为布尔型
print(bool("True"))  # True
print(bool("False"))  # True
print(bool(""))  # False
print(bool(0))  # False
print(bool(1))  # True


# 变量命名
print("-----------变量命名------------")
# 1. 变量名只能由数字、字母、下划线组成
# 2. 变量名不能以数字开头
# 3. 变量名不能与关键字重名
# 4. 变量名要具有描述性
# 5. 变量名要区分大小写
# 6. 变量名不能使用中文
# 7. 变量名不能使用特殊字符
# 8. 变量名不能使用空格
# 9. 变量名不能使用运算符
# 10. 变量名不能使用函数名
