# 高阶函数
def highfun(x, y, z):
    return z(x) + z(y)
highfun(5, -5, abs)

def ff(x):
    return x * x
rr = map(ff, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def addNum(x, y):
    return x + y

reduce(addNum, [1, 2, 3, 4, 5])

# 把序列[1, 3, 5, 7, 9]变换成整数13579
from functools import reduce
def getNum(x, y):
    return x * 10 + y

reduce(getNum, [1, 2, 3])

# 结合map和reduce将str转化成int
def str2int(s):
    def addNum(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(char2num, map(addNum, s))


# filter
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(x):
    return x % 2 == 1

list(filter(is_odd, [1, 2, 3, 4, 5]))

def del_empty(s):
    return s and s.strip()

list(filter(del_empty, ['3', '', 'A', '', 'VFd']))

# sort
# sorted([36, 5, -12, 9, -21], key=abs)
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list
# key 处理但并不修改sort排序的值

# 返回函数
# 实现一个可变参数的求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + args
    return ax

# 不需要立刻求和时，可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 得到的backfunc1是一个函数,调用变量时才求值
backfunc1 = lazy_sum(1, 2, 3, 4, 5)

print('func--->\n', backfunc1,'\n value--->\n', backfunc1())

# 闭包    返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
# 修改
def count_mod():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

# 装饰圈
# 函数对象有一个__name__属性，可以拿到函数的名字
def myName():
    return myName.__name__

# 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return  wrapper

# @log 放在now上相当于 now = log(now)
@log
def now():
    print('2017-07-26')

# 完整的装饰器还要保证__name__的指向正确，所以在用装饰器的时候还要导入
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

# 偏函数
# functools.partial 将函数中可以参数的值固定，简化函数重复操作
import functools
int2 = functools.partial(int, base=2)

