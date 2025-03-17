# 字典类型
# 键值对形式的存储
# 字典是一种可变的、无序的简直对集合
# 字典的键必须是不可变类型（可哈希的），而值可是任意的类型

# 字典创建
print("字典的创建")
# 1. 使用花括号创建字典
dict1 = {"name": "张三", "age": 18, "gender": "男"}
print("dict1: ", dict1)
# 2. 使用dict()函数创建字典
dict2 = dict(name="李四", age=20, gender="女")
print("dict2: ", dict2)
# 3. 使用zip()函数创建字典
dict3 = dict(zip(["name", "age", "gender"], ["王五", 22, "男"]))
print("dict3: ", dict3)
# 4. 使用fromkeys()函数创建字典
dict4 = dict.fromkeys(["name", "age", "gender"], "未知")
print("dict4: ", dict4)
# 5. 使用字典推导式创建字典
dict5 = {x: x**2 for x in range(1, 10)}
print("dict5: ", dict5)
# 6. 使用简直对的列表创建字典
dict6 = dict([("name", "张三"), ("age", 18), ("gender", "男")])
print("dict6: ", dict6)

# 创建空字典
dict7 = {}
dict8 = dict()
print("dict7: ", dict7)
print("dict8: ", dict8)

# 字典的基本操作
print("字典的基本操作")
# 1. 访问字典中的值
print("dict1['name']: ", dict1["name"])
print("dict1.get('name'): ", dict1.get("name"))
# 可以设置默认值
print("dict1.get('name1', '张三'): ", dict1.get("name1", "张三---"))
print("dict1.get('name1'): ", dict1.get("name1"))
print(dict1)


# 添加和修改
print("添加和修改")
dict1["name"] = "李四"  # 修改已存在的键的值
dict1["height"] = 180  # 添加新的键值对
print("更新后的 ditc1: ", dict1)

# 删除
print("删除")
del dict1["name"]  # 删除指定键的键值对
print("删除后的 dict1: ", dict1)

# 字典的常用方法
print("字典的常用方法")

score = {
    "语文": 90,
    "数学": 80,
    "英语": 70,
}
student = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "score": score,
    "hobby": ["唱歌", "跳舞", "游泳"],
    "address": {"province": "北京", "city": "北京", "district": "朝阳区"},
}
print("student: ", student)

# # 获取所有键
# print("获取所有键")
# print("student.keys(): ", student.keys())
# # 获取所有值
# print("获取所有值")
# print("student.values(): ", student.values())
# # 获取所有键值对
# print("获取所有键值对")
# print("student.items(): ", student.items())

score["语文"] = 100  # 修改值
student["score"]["数学"] = 90  # 修改值
print("student: ", student)

# 5. 字典的嵌套
print("\n=== 字典的嵌套 ===")
school = {
    "class1": {"name": "一班", "students": ["张三", "李四"]},
    "class2": {"name": "二班", "students": ["王五", "赵六"]},
}
print("一班学生:", school["class1"]["students"])


# 6. 实际应用场景示例
print("\n=== 实际应用场景 ===")

# 配置信息存储
config = {
    "database": {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
    },
    "server": {"host": "0.0.0.0", "port": 8080},
}
print("配置信息:", config)

# 数据缓存
cache = {}


def get_user_info(user_id):
    if user_id in cache:
        return cache[user_id]
    # 模拟数据库查询
    user_info = {"id": user_id, "name": f"用户{user_id}", "age": 20}
    cache[user_id] = user_info
    return user_info


print("用户信息:", get_user_info(1001))
print("用户信息:", get_user_info(1034))
print(cache)


# 计数器
word_count = {}
text = "hello world hello python python world"
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("词频统计:", word_count)

# 状态机
state_machine = {
    "idle": {"start": "running", "stop": "idle"},
    "running": {"pause": "paused", "stop": "idle"},
    "paused": {"resume": "running", "stop": "idle"},
}
current_state = "idle"
print("当前状态:", current_state)
# 状态转换
current_state = state_machine[current_state]["start"]
print("转换状态:", current_state)

# 7. 字典的性能特点
print("\n=== 字典的性能特点 ===")
# 检查键是否存在
print("'name' in student:", "name" in student)  # O(1) 时间复杂度


# 8. 字典的限制
print("\n=== 字典的限制 ===")
# 键必须是不可变类型
try:
    invalid_dict = {[1, 2]: "value"}  # 这会引发错误
except TypeError as e:
    print("不可使用可变类型作为键:", e)

"""
## 字典的主要使用场景：
1. 配置信息管理 ：
   
   - 存储程序配置
   - 环境变量管理
   - 用户设置存储
2. 缓存实现 ：
   
   - 数据缓存
   - 计算结果缓存
   - 会话信息存储
3. 数据统计 ：
   
   - 频率统计
   - 计数器实现
   - 数据分组
4. 数据映射 ：
   
   - 键值对应关系
   - 状态转换表
   - 路由表
5. JSON 数据处理 ：
   
   - API 数据处理
   - 配置文件解析
   - 数据序列化
6. 图结构实现 ：
   
   - 邻接表表示
   - 权重图实现
   - 树形结构存储
"""


# 可以通过Python内置函数zip 压缩两个序列并创建字典
print("压缩序列 zip function")
item1 = dict(zip("abcde", "12345"))
print(item1)
item2 = dict(zip("ABCED", range(1, 20)))
print(item2)
print(len(item1))
