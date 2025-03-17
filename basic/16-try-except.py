# python中的异常处理机制

file = None


try:
    file = open("test.txt", "r", encoding="utf-8")
    print(file.read())
except FileNotFoundError:
    print("文件不存在")
except LookupError:
    print("未知编码")
except UnicodeDecodeError:
    print("解码错误")
finally:
    if file:
        print("关闭文件")
        file.close()


# 自定义异常
# 使用raise 来引发异常


class InputError(ValueError):
    """输入错误"""

    pass


def fac(num):
    if num < 0:
        raise InputError("输入错误")
    if num == 0:
        return 1
    return num * fac(num - 1)


fac(-1)
