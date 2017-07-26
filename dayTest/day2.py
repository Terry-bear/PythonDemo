# 切片
L = {'terry','jolie','rose','jone','candey'}

K = list(range(100))
J = K[0:10]
U = K[-10:]
# 所有数 每5个取一个
O = K[::5]
# 不取值 就是直接复制
P = K[:]
for i in range(10):
    print(J[i])

for i in range(10):
    print(U[i])

for i in range(20):
    print(O[i])

for i in range(100):
    print(P[i])

# tuple也可以用切片操作，只是操作的结果仍是tuple
Y = (0, 1, 2, 3, 4, 5)[:3]

# 迭代
d = {'a':1,'b':2,'c':3,'d':4}
for i in d:
    print('key',i,'----','value',d[i])

for i in d.values():
    print('key',i,'****')

for k,v in d.items():
    print('key',k,'value',v)

for ch in 'abcdefg':
    print(ch)

#判断一个对象是可迭代对象，方法是通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abcdefg',Iterable))
print(isinstance(J,Iterable))
print(isinstance(K,Iterable))
print(isinstance(L,Iterable))
print(isinstance(U,Iterable))
print(isinstance(O,Iterable))
# 整数不可以迭代
print(isinstance(123,Iterable))

# 实现索引-元素对
for i,value in enumerate(['A','B','C']):
    print('i',i,'--->','value',value)


# 列表生成器
listcomp = list(range(1,11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#[1x1, 2x2, 3x3, ..., 10x10]
L= []
for i in listcomp:
    L.append(i*i)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 简化为
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
Lsimp = [x * x for x in range(1, 11)]
# 前面是逻辑条件，后面是筛选条件
Lsimp2 = [x * x for x in range(1,11) if x % 2 == 0]
# 加循环 ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
Lsimp3 = [m + n for m in 'ABC' for n in 'XYZ']
# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os   # 导入os模块
Showdir = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录


# 一边循环一边计算的机制，称为生成器：generator
# 第一种方法，只要把一个列表生成式的[]改成()，就创建了一个generator
gsimp = (x * x for x in range(1,11))
# 通过next()函数获得generator的下一个返回值
# 通过迭代获取是常用方法
for i in gsimp:
    print('生成器demo---',i)

# 斐波那契数列函数
def fib(max):
    n,a,b = 0,1,2
    while n < max:
        print(b)
        a, b = b,a + b
        n = n + 1
    return 'done'

print('fib-->',fib(6))

# 变更上述的print为yield，函数就为generator生成器
def fibToGen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print('fibToGen-->',fibToGen(6))

#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
