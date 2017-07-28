# err_logging.py    logging日志模块记录

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# logging

# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# pdb

# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# err.py
s = '0'
n = int(s)
print(10 / n)


# pdb.set_trace()

# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，
# 然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：

# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

# 文档注译

def doc():
    '''
    这里一般写程序的调用结果，例如：
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    pass
