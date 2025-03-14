# python中的文件操作


def file_write_demo():
    """文件写入示例"""
    # 打开文件，如果不存在则创建，'w'表示写入模式
    with open("example.txt", "w") as file:
        # 写入内容到文件
        file.write("Hello, World -- 1!\n")
        file.write("This is a sample file.\n")
        file.write("Goodbye!\n")
        # 写入多行数据
        lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
        file.writelines([line + "\n" for line in lines])
    print("File write operation completed.")


def file_read_demo():
    """文件读取示例"""
    # 打开文件，'r'表示读取模式
    with open("example.txt", "r", encoding="utf-8") as file:
        # 逐行读取文件内容
        for line in file:
            print(line.strip())  # 去除行尾的换行符
    print("File read operation completed.")


def file_append_demo():
    """文件追加示例"""
    # 打开文件，'a'表示追加模式
    with open("example.txt", "a") as file:
        # 追加内容到文件

        for i in range(10):
            file.write(f"Line {i + 1}\n")
        file.write("This is a new line.\n")
        file.write("Appended content.\n")
    print("File append operation completed.")


def file_with_position(name: int = 1):
    """文件读取示例"""
    # 打开文件，'r'表示读取模式
    with open("example.txt", "r", encoding="utf-8") as file:
        # 读取前3个字符
        print(file.read(3))
        # 获取当前位置
        print(f"当前位置：{file.tell()}")
        # 移动到文件开头
        file.seek(0)
        # 再次读取
        print(file.read(3))


def binary_file_demo(name: str = "binary"):
    """二进制文件操作示例"""
    # 写入二进制数据
    with open("binary", "wb") as f:
        f.write(b"Hello Binary")

    # 读取二进制数据
    with open("binary", "rb") as f:
        data = f.read()
        print(f"二进制数据：{data.decode()}")


def main():
    # 文件写入示例
    # file_write_demo()
    # 文件读取示例
    # file_read_demo()
    # 文件追加示例
    # file_append_demo()
    # 文件读取示例
    # file_with_position()

    # 二进制文件操作示例
    binary_file_demo()


if __name__ == "__main__":
    main()
