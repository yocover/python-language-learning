import threading
import time

from concurrent.futures import ThreadPoolExecutor


"""
多个线程竞争一个资源 - 保护临界资源 - 锁 （Lock 、 RLock）
多个资源竞争多个资源（线程数 > 资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/ 唤醒等待中的线程 - 条件变量（Condition）
"""

from time import sleep


class Account:
    """'银行账户"""

    def __init__(self, balance=0):

        # 初始化账户余额 balance lock condition
        self.balance = balance
        lock = threading.RLock()  # 可重入锁
        self.condition = threading.Condition(lock)  # 条件变量

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                print(f"余额不足，等待...")
                self.condition.wait()  # 等待条件满足
            new_balance = self.balance - money
            print(f"取款{money}元，余额{new_balance}元")
            sleep(0.1)  # 模拟耗时操作
            self.balance = new_balance
            # 这块不需要通知其其

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            print(f"存款{money}元，余额{new_balance}元")
            sleep(0.1)  # 模拟耗时操作
            self.balance = new_balance
            self.condition.notify_all()  # 通知所有等待线程


def add_money(account):
    """存钱"""
    while True:
        money = random.randint(5, 10)
        account.deposit(money)
        print(f"存款{money}元")
        time.sleep(1)  # 模拟耗时操作


def sub_money(account):
    """取钱"""
    while True:
        money = random.randint(5, 10)
        account.withdraw(money)
        print(f"取款{money}元")
        time.sleep(1)  # 模拟耗时操作


# 1. 演示数据竞争问题
class UnsafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        current = self.count
        time.sleep(0.000001)  # 模拟耗时操作
        print(f"线程{threading.current_thread().name}正在执行")
        self.count = current + 1


# 2. 使用锁解决数据竞争
class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:  # 使用锁保护共享资源
            current = self.count
            time.sleep(0.34)  # 模拟耗时操作
            print(f"线程{threading.current_thread().name}正在执行")
            self.count = current + 1


# 测试不安全的计数器
def test_unsafe_counter():
    counter = UnsafeCounter()
    threads = []

    for _ in range(10):
        t = threading.Thread(target=counter.increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"不安全的计数器最终值: {counter.count}")  # 预期是10，但可能小于10


# 测试安全的计数器
def test_safe_counter():
    counter = SafeCounter()
    threads = []

    for _ in range(10):
        t = threading.Thread(target=counter.increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"安全的计数器最终值: {counter.count}")  # 一定是10


# 3. 使用 RLock（可重入锁）示例
class ReentrantLockExample:
    def __init__(self):
        self.lock = threading.RLock()
        self.data = 0

    def outer_method(self):
        with self.lock:
            print("外部方法获得锁")
            self.inner_method()

    def inner_method(self):
        with self.lock:
            print("内部方法获得锁")
            self.data += 1


# 4. 使用条件变量（Condition）示例
class ProducerConsumer:
    def __init__(self):
        self.condition = threading.Condition()
        self.items = []

    def produce(self):
        with self.condition:
            self.items.append("item")
            print("生产了一个项目")
            self.condition.notify()  # 通知消费者

    def consume(self):
        with self.condition:
            while not self.items:
                print("等待项目...")
                self.condition.wait()  # 等待生产者
            item = self.items.pop()
            print("消费了一个项目")


if __name__ == "__main__":
    print("=== 测试数据竞争问题 ===")
    # test_unsafe_counter()
    # test_safe_counter()

    # print("\n=== 测试可重入锁 ===")
    # rl = ReentrantLockExample()
    # rl.outer_method()

    # print("\n=== 测试生产者消费者 ===")
    # pc = ProducerConsumer()
    # producer = threading.Thread(target=pc.produce)
    # consumer = threading.Thread(target=pc.consume)

    # consumer.start()  # 消费者先等待
    # time.sleep(1)  # 稍等片刻
    # producer.start()  # 生产者生产

    # producer.join()
    # consumer.join()

    # 5. 线程池示例
    account = Account()
    with ThreadPoolExecutor(max_workers=15) as executor:
        for i in range(10):
            executor.submit(add_money, account)
        for i in range(5):
            executor.submit(sub_money, account)
