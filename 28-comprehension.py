# 1. 列表推导式
numbers = [1, 2, 3, 4, 5]
# 生成所有数字的平方
squares = [x * x for x in numbers]
print("平方数:", squares)  # [1, 4, 9, 16, 25]

# 带条件的列表推导式
even_squares = [x * x for x in numbers if x % 2 == 0]
print("偶数的平方:", even_squares)  # [4, 16]

# 2. 字典推导式
# 创建数字及其平方的映射
square_dict = {x: x * x for x in numbers}
print("数字平方字典:", square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 3. 集合推导式
# 生成所有数字的平方，去除重复
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x * x for x in numbers}
print("唯一平方数:", unique_squares)  # {1, 4, 9, 16}

# 4. 生成器表达式
# 使用()代替[]创建生成器对象
squares_gen = (x * x for x in numbers)
print("生成器对象:", squares_gen)
print("生成器内容:", list(squares_gen))

# 5. 嵌套推导式
# 创建3x3矩阵
matrix = [[i + j for j in range(3)] for i in range(0, 9, 3)]
print("矩阵:", matrix)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 6. 实际应用示例
# 文件处理
files = ['test.py', 'data.csv', 'image.jpg', 'doc.pdf']
python_files = [f for f in files if f.endswith('.py')]
print("Python文件:", python_files)

# 数据转换
data = {'a': 1, 'b': 2, 'c': 3}
doubled = {k: v * 2 for k, v in data.items()}
print("值翻倍的字典:", doubled)

# 字符串处理
text = "Hello World"
char_count = {char: text.count(char) for char in set(text)}
print("字符计数:", char_count)