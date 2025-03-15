import heapq

# 1. 基本堆操作
numbers = [10, 5, 8, 3, 2, 9, 4]

# 将列表转换为堆
heapq.heapify(numbers)
print("堆化后的列表:", numbers)  # [2, 3, 4, 5, 10, 9, 8]

# 向堆中添加元素
heapq.heappush(numbers, 1)
print("添加元素后:", numbers)

# 从堆中弹出最小元素
smallest = heapq.heappop(numbers)
print("最小元素:", smallest)
print("弹出后的堆:", numbers)

# 2. 获取最大/最小元素
data = [10, 5, 8, 3, 2, 9, 4]

# 获取最小的3个元素
smallest_three = heapq.nsmallest(3, data)
print("最小的三个元素:", smallest_three)

# 获取最大的3个元素
largest_three = heapq.nlargest(3, data)
print("最大的三个元素:", largest_three)


# 3. 使用堆处理复杂对象
class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task({self.priority}, {self.description})"


# 创建任务队列
task_queue: list[Task] = []
heapq.heappush(task_queue, Task(3, "普通任务"))
heapq.heappush(task_queue, Task(1, "紧急任务"))
heapq.heappush(task_queue, Task(2, "重要任务"))

# 按优先级处理任务
while task_queue:
    task = heapq.heappop(task_queue)
    print("处理任务:", task)


# 4. 合并多个有序序列
list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]

merged = list(heapq.merge(list1, list2, list3))
print("合并后的有序序列:", merged)


"""
heapq 的主要特点：

1. 基本操作 ：
   
   - heapify(x) : 将列表转换为堆
   - heappush(heap, item) : 向堆中添加元素
   - heappop(heap) : 弹出最小元素
   - heappushpop(heap, item) : 先推入再弹出
   - heapreplace(heap, item) : 先弹出再推入
2. 实用函数 ：
   
   - nlargest(n, iterable) : 获取最大的 n 个元素
   - nsmallest(n, iterable) : 获取最小的 n 个元素
   - merge(*iterables) : 合并多个有序序列
3. 应用场景 ：
   
   - 优先队列
   - 任务调度
   - 数据流中位数计算
   - Top-K 问题
   - 合并有序序列
4. 注意事项 ：
   
   - Python 的 heapq 实现的是最小堆
   - 如果需要最大堆，可以将元素取反
   - 处理复杂对象时需要实现 __lt__ 方法
"""
