from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

# 1. Counter：计数器
# 统计字符出现次数
text = "hello world -----"
char_count = Counter(text)
# print(
#     "字符计数:", char_count
# )  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


# 统计列表中元素出现次数
numbers = [1, 2, 3, 1, 2, 1, 3, 4, 2]
num_count = Counter(numbers)
# print("数字计数:", num_count)  # Counter({1: 3, 2: 3, 3: 2, 4: 1})


# 2. defaultdict：带默认值的字典
# 按首字母对单词分组
words = ["apple", "banana", "cherry", "date", "berry", "apricot"]
word_dict = defaultdict(list)
for word in words:
    word_dict[word[0]].append(word)
# print("单词分组:", dict(word_dict))


# 3. OrderedDict：有序字典（在 Python 3.7+ 中普通字典也是有序的）
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
# print("有序字典:", ordered_dict)


# 4. deque：双端队列
# 创建一个双端队列
queue = deque(["a", "b", "c"])
queue.append("d")  # 在右侧添加
queue.appendleft("e")  # 在左侧添加
print("双端队列:", queue)
print("弹出右侧:", queue.pop())  # 从右侧弹出
print("弹出左侧:", queue.popleft())  # 从左侧弹出
print("处理后的队列:", queue)



# 5. namedtuple：命名元组
# 创建一个表示点的命名元组
Point = namedtuple("Point", ["x", "y"])
p = Point(11, y=22)
print("点的坐标:", p.x, p.y)
print("是否是元组:", isinstance(p, tuple))


# 6. 实际应用示例
# 使用 Counter 进行词频统计
text = """
Python is a great programming language.
Python is easy to learn.
Programming in Python is fun.
"""
words = text.lower().split()
word_count = Counter(words)
print("\n词频统计:")
for word, count in word_count.most_common(3):
    print(f"{word}: {count}")

# 使用 defaultdict 处理复杂数据结构
log_data = [
    ("error", "disk full"),
    ("warning", "memory low"),
    ("error", "cpu overload"),
    ("info", "service started"),
    ("error", "network down"),
]

logs = defaultdict(list)
for level, message in log_data:
    logs[level].append(message)
print("\n日志分类:", dict(logs))

# 使用 deque 实现循环缓冲区
history: deque[int] = deque(maxlen=3)  # 只保留最近3个元素
for i in range(5):
    history.append(i)
print("\n最近的历史记录:", history)
