# 字符串类型介绍
# python中的字符串是一种不可变的序列类型
# 用于存储文本
#

print("字符串的创建")

testStr = "hello world"
print(testStr)
testStr = "hello world"
print(testStr)

# str[1] = "a"  # 字符串是不可变的，不能修改元素 error

# 使用三引号可以包含多行文本
str3 = """字符串
     示例
      多行"""
print(str3)

# 字符串的基本操作
print("字符串的基本操作")

# 字符串的长度
print(len(testStr))

# 字符串的拼接
str1 = "hello"
str2 = "world"
str3 = str1 + " - " + str2
print(str3)

# 字符串重复
repeated = str1 * 3
print("重复:", repeated)

# 字符串索引（从0开始）
full_greeting = str1 + " " + str2 + "!"
print("第一个字符:", full_greeting[0])
print("最后一个字符:", full_greeting[-1])

# 字符串切片 [start:end:step]
print("切片 [0:5]:", full_greeting[0:5])  # 从索引0到4
print("切片 [6:]:", full_greeting[6:])  # 从索引6到结束
print("切片 [:5]:", full_greeting[:5])  # 从开始到索引4
print("切片 [::2]:", full_greeting[::2])  # 步长为2
print("反转字符串:", full_greeting[::-1])  # 步长为-1，反转字符串


# 字符串的常用方法
print("字符串的常用方法")
sample = "  Python Programming Language  "

print("大写:", sample.upper())
print("小写:", sample.lower())
print("首字母大写:", sample.capitalize())
print("所有单词首字母大写:", sample.title())
print("是否以字母开头:", sample.isalpha())
print("是否以数字开头:", sample.isdigit())


# 去除空白
print("去除空白:", sample.strip())
print("去除左空白:", sample.lstrip())
print("去除右空白:", sample.rstrip())

# 查找和替换
print("查找:", sample.find("Programming"))
print("替换:", sample.replace("Programming", "Python"))

# 分割和连接
worlds = sample.split()
print("分割:", worlds)
print("连接:", "*".join(worlds))

# 判断方法
print("是否以字母开头:", sample.strip().startswith("Python"))
print("是否以字母结尾:", sample.strip().endswith("Language"))
print("是否全是字母或数字:", sample.strip().isalnum())
print("是否全是字母:", "Python".isalpha())
print("是否全是数字:", "12345".isdigit())

# 4. 字符串格式化
print("\n=== 字符串格式化 ===")
name = "张三"
age = 25
height = 1.75
print("我的名字是{}, 今年{}岁, 身高{}米".format(name, age, height))


# 使用%操作符（旧式）
old_style = "姓名: %s, 年龄: %d, 身高: %.2f米" % (name, age, height)
print("旧式格式化:", old_style)

# 使用format()方法
format_style = "姓名: {}, 年龄: {}, 身高: {:.2f}米".format(name, age, height)
print("format格式化:", format_style)

# 使用f-string（Python 3.6+）
f_string = f"姓名: {name}, 年龄: {age}, 身高: {height:.2f}米"
print("f-string格式化:", f_string)

# 5. 字符串的转义字符
print("\n=== 字符串的转义字符 ===")
print("换行符: 第一行\\n第二行")
print("制表符: 姓名\\t年龄")
print('引号: 他说:"Python很有趣"')
print("反斜杠: C:\\Users\\Admin")

# 原始字符串（r前缀）
print(r"原始字符串: C:\Users\Admin\Documents")

# 6. 字符串的不可变性
print("\n=== 字符串的不可变性 ===")
s = "hello"
print("原始字符串:", s)
# s[0] = "H"  # 这会引发错误，字符串是不可变的
# 要修改字符串，必须创建一个新的字符串
s = "H" + s[1:]
print("修改后的字符串:", s)


# 7. 字符串编码和解码
print("\n=== 字符串编码和解码 ===")
# 字符串编码为字节
text = "你好，Python"
encoded = text.encode("utf-8")
print("编码后:", encoded)

# 字节解码为字符串
decoded = encoded.decode("utf-8")
print("解码后:", decoded)

# 8. 字符串的内存表示
print("\n=== 字符串的内存表示 ===")
str_a = "hello"
str_b = "hello"
print("str_a的id:", id(str_a))
print("str_b的id:", id(str_b))
print("str_a和str_b是同一对象:", str_a is str_b)  # Python会对相同的字符串进行内存优化


# 9. 字符串与其他类型的转换
print("\n=== 字符串与其他类型的转换 ===")
# 数字转字符串
num_str = str(123)
float_str = str(3.14)
print("数字转字符串:", num_str, type(num_str))
print("浮点数转字符串:", float_str, type(float_str))

# 字符串转数字
try:
    # 字符串转整数
    num = int("123")
    print("字符串转整数:", num, type(num))

    # 字符串转浮点数
    pi = float("3.14")
    print("字符串转浮点数:", pi, type(pi))
except ValueError as e:
    print("转换失败:", e)

# 字符串转数字
num = int("456")
pi = float("3.14159")
print("字符串转数字:", num, pi)

# 列表转字符串，字符串转列表
char_list = list("Python")
print("字符串转列表:", type(char_list), char_list)
print("列表转字符串:", "".join(char_list))
