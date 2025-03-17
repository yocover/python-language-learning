import time

# 循环结构
# for 循环
# for 变量 in 序列:
#     代码块
# for 变量 in 序列:
#     代码块


for i in range(1, 10):
    print(i)
    time.sleep(0.01)  # 暂停1秒 让程序休眠 0.1秒

# range 的使用
# range(start, stop, step)
# start 是开始值，stop 是结束值，step 是步长
# range(1, 10) 表示从1到9
# range(1, 10, 2) 表示从1到9，每次增加2
# range(10, 0, -1) 表示从10到1，每次减少1

print("-------range(1, 10, 2)-------")
for i in range(1, 10, 2):
    print(i)

print("-------range(10, 0, -1)-------")
for i in range(10, 0, -1):
    print(i)

print("-------range(1, 10,-2)-------")
for i in range(20, 10, -2):  # 步长为负数时，start 必须大于 stop
    print(i)

# 使用 _ 来接收不需要的变量
for _ in range(10):
    print("hello")
    time.sleep(0.01)


# 整数求和
sum = 0
for i in range(1, 101):
    sum += i
print(f"1到100的和是：{sum}")

# 求100-999之间的水仙花数
# 水仙花数是指各位数字的立方和为该数字本身
# 例如：153 = 1^3 + 5^3 + 3^3

for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i)

# 1 - 100 之间的偶数求和

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(f"1-100之间的偶数求和是：{sum}")

sum = 0
for i in range(2, 101, 2):
    sum += i
print(f"1-100之间的偶数求和是：{sum}")


# 1 - 100 之间的奇数求和
sum = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum += i
print(f"1-100之间的奇数求和是：{sum}")


# while 循环
# while 条件:
#     代码块

i = 1
while i <= 10:
    print(i)
    i += 1
    time.sleep(0.1)


# 1 - 100 之间的偶数求和
sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(f"1-100之间的偶数求和是：{sum}")


# 1 - 100 之间的奇数求和
sum = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        sum += i
    i += 1
#  i++  i--  i+=1  i-=1 python 中没有 i++  i--
# i += 1      # 加1
# i -= 1      # 减1
# i *= 2      # 乘2
# i /= 2      # 除2
# i **= 2     # 平方
# i //= 2     # 整除
# i %= 2      # 取余

# break 和 continue
# break 用于终止循环
# continue 用于跳过本次循环

# 打印1-10之间的数字，遇到5时，不打印
print("打印1-10之间的数字，遇到5时，跳出循环")
for i in range(1, 10):
    if i == 5:
        print("遇到5了, 跳出循环")
        break
    print(i)
    time.sleep(0.001)

# 打印1-10之间的数字，遇到5时，不打印
print("打印1-10之间的数字，遇到5时，跳过本次循环")
for i in range(1, 10):
    if i == 5:
        print("遇到5了, 跳过本次循环")
        continue
    print(i)
    time.sleep(0.001)


# 嵌套循环结构
# 外层循环
for i in range(1, 10):
    # 内层循环
    for j in range(1, 10):
        print("内层循环" f"{i} * {j} = {i*j}")
    print("外层循环", i)


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()

# 打印三角形
for i in range(1, 10):
    for j in range(1, i + 1):
        print("*", end="")
    print()


for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print(num)
