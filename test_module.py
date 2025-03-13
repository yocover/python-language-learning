import module1 as m1
import module2 as m2


# module1.foo()
# module2.foo()
m1.foo()
m2.foo()

# from module1 import foo
# foo()

# from module2 import foo
# foo()


from module1 import foo as f1
from module2 import foo as f2
f1()
f2()

# python 标准库的模块和函数


# python中的函数是一等函数
# 所谓一等函数
# 1. 函数可以赋值变量
# 2. 函数可以作为函数的参数
# 3. 函数哦也可以作为函数的返回值
# 4. 把一个函数作为其他函数的参数或者返回值的用法， 我们通常称之为高阶函数


