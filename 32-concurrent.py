import threading
import multiprocessing
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


"""
Python 中实现并发编程的三种方案
# 多线程下
# 多进程
# 异步编程 I/O

# 多线程 

Python中有GIL类防止多个线程同时执行本地字节码

这个锁对于CPython 是必须的
因为Cpython的内存管理并不是线程安全的
因为VIL的存在，多线程并不能发挥多核CPU的优势

进程和线程的区别和联系？
进程： 操作系统分配内存的基本单-位，一个进程可以包含一个或者多个线程
线程： 操作系统分配CPU的基本单位，一个线程只能属于一个进程，一个进程可以包含多个线程

多线程的优点：

1. 适合处理I/O密集型任务
2. 共享内存空间，可以方便的进行数据共享
3. 线程间切换开销小，适合处理大量的短任务


"""


# 1. 多线程示例
def thread_task(name, delay):
    print(f"线程 {name} 开始")
    time.sleep(delay)
    print(f"线程 {name} 结束")


def thread_example():
    print("\n=== 多线程示例 ===")
    threads = []
    for i in range(10):
        t = threading.Thread(target=thread_task, args=(f"Thread-{i}", 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# 2. 线程池示例
def pool_task(x):
    time.sleep(1)
    return x * x


def thread_pool_example():
    print("\n=== 线程池示例 ===")
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(pool_task, range(5))
        print(f"结果: {list(results)}")


# 3. 多进程示例
def process_task(name):
    print(f"进程 {name} 开始")
    time.sleep(1)
    print(f"进程 {name} 结束")


def process_example():
    print("\n=== 多进程示例 ===")
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=process_task, args=(f"Process-{i}",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


# 4. 进程池示例
def process_pool_example():
    print("\n=== 进程池示例 ===")
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(pool_task, range(5))
        print(f"结果: {list(results)}")


# 5. 异步编程示例
async def async_task(name, delay):
    print(f"任务 {name} 开始")
    await asyncio.sleep(delay)
    print(f"任务 {name} 结束")
    return f"{name} 完成"


async def main():
    print("\n=== 异步编程示例 ===")
    # 创建多个协程任务
    tasks = [async_task(f"Task-{i}", 1) for i in range(3)]
    # 并发执行所有任务
    results = await asyncio.gather(*tasks)
    print(f"所有任务完成: {results}")


# 6. 实际应用示例：并发下载
import aiohttp


async def download_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def download_example():
    print("\n=== 并发下载示例 ===")
    urls = ["http://example.com", "http://example.org", "http://example.net"]

    async with aiohttp.ClientSession() as session:
        tasks = [download_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        print(f"下载完成，获取了 {len(results)} 个响应")


if __name__ == "__main__":
    # 运行多线程示例
    # thread_example()

    # # 运行线程池示例
    # thread_pool_example()

    # # 运行多进程示例
    # process_example()

    # # 运行进程池示例
    # process_pool_example()

    # # 运行异步示例
    # asyncio.run(main())

    # 运行并发下载示例
    asyncio.run(download_example())  # 需要安装 aiohttp


"""
Python 并发编程的三种主要方式：

1. 多线程（Threading） ：
   
   - 适合 I/O 密集型任务
   - 共享内存空间
   - 受 GIL 限制
2. 多进程（Multiprocessing） ：
   
   - 适合 CPU 密集型任务
   - 独立内存空间
   - 不受 GIL 限制
   - 资源开销较大
3. 异步编程（Asyncio） ：
   
   - 适合 I/O 密集型任务
   - 单线程事件循环
   - 非阻塞操作
   - 需要特殊的 async/await 语法
使用建议：

1. I/O 密集型任务（如网络请求）：使用异步编程或多线程
2. CPU 密集型任务（如计算）：使用多进程
3. 简单并发任务：使用线程池或进程池
4. 大规模并发：考虑异步编程
注意事项：

1. 避免线程间共享可变状态
2. 注意进程间通信的开销
3. 异步编程需要特殊的编程模式
4. 合理使用池化技术避免资源浪费
"""
