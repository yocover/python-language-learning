# 分支结构
# 单分支结构
print("-----------单分支结构------------")
age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你已经成年了")
# else:
#     print("你还未成年")

if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")


# if 条件表达式:
#     代码块
# else:
#     代码块

# 多分支结构
print("-----------多分支结构------------")
score = int(input("请输入你的成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 嵌套结构
print("-----------嵌套结构------------")
age = int(input("请输入你的年龄："))
if age >= 18 and age <= 60:
    print("你是一个成年人")
    if age >= 30 and age <= 50:
        print("你是一个中年人")
    else:
        print("你是一个年轻人")
else:
    print("你还未成年")

# BMI 计算器
print("-----------BMI 计算器------------")
height = float(input("请输入你的身高(cm): "))
weight = float(input("请输入你的体重(kg): "))

bmi = weight / (height / 100) ** 2
if 18.5 <= bmi < 24.9:
    print("正常", "bmi:", bmi)
elif 24.9 <= bmi < 29.9:
    print("超重", "bmi:", bmi)
elif bmi >= 29.9:
    print("肥胖", "bmi:", bmi)
else:
    print("体重过轻", "bmi:", bmi)

# elif 条件表达式:
#     代码块
# else:
#     代码块
# if 条件表达式1:
#     代码块1
# elif 条件表达式2:
#     代码块2
# else:
#     代码块3

# match 和 case 结构
print("-----------match 和 case 结构------------")

# 输入一个数字，判断是奇数还是偶数
num = int(input("请输入一个数字："))

# match 和 case 结构
# match 表达式:
#     case 模式1:
#         代码块1
#     case 模式2:
#         代码块2
#     case _:
#         代码块3

match num % 2:
    case 0:
        print("偶数")
    case 1:
        print("奇数")

# python 中没有 switch 结构，但是有 match 结构
# match 结构是 python 3.10 版本引入的
# match 结构是 switch 结构的替代品







