# age = 20
# if age > 18:
#     print('your age is ',age)
#     print('adult')
# else:
#     print('your age is',age)
#     print('teenager')
#
#
# birth = input('birth:')
# birth = int(birth)
# if birth < 2000:
#     print('90后--')
# elif birth > 2000:
#     print('00后--')
# else:
#     print('10后--')
#
# family = ('terry','jolie','rose')
# for menber in family:
#     print(menber)
#
# sum = 0
# for x in [1,2,3,4,5,6,7,8,9]:
#     sum+=x
# print(sum)
#
# s = list(range(5))
# for x in s:
#     print(x)
#
# ddict = {'terry':23,'jolie':26,'rose':0.3}
# print(ddict['terry'])
# ddict['dalin'] = 22
# print(ddict['dalin'])
# print('client' in ddict)
# print('jolie' in ddict)
# print(ddict.get('terry'))
# print(ddict.get('tom'))


s = {1, 2, 3, 4}
print(s)
s.add('terry')
print(s)
## set是只有key的{}集合，dict是有key-value的{}集合

def my_abs(x):
    if x > 0:
        print(x)
    else:
        print(-x)

my_abs(-7)

def my_empty(x):
    pass

my_empty(1000)

# n=2 是默认参数，当调用是第二个参数没有赋值时，自动填充
def my_power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(my_power(5))

# 默认参数必须是不可变量
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def add_end2(L=[]):
    L.append('END2')
    return L

print(add_end2())
print(add_end())


# 可变参数在参数前面加上 *
def my_calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# print(my_calc([1,2,3,4]))
print(my_calc(1,2,3,4))

numm = {1,2,3}
print(my_calc(*numm))

print('这是个set',numm,'有',len(numm),'个参数')

# 关键字参数在参数前面加上 **
def my_person(name,age,**others):
    print('name:',name,'age:',age,'others:',others)

my_person('terry',22)
my_person('jolie',26,city='changsha')

extra = {'city':'beijing','job':'engineer'}
my_person('jolie',26,**extra)

## 递归调用
def my_fact(n):
    if n == 1:
        return 1
    return n * my_fact(n - 1)

print(my_fact(3))

# 尾递归
def my_fact_iter(num,product):
    if num == 1:
        return product
    return my_fact_iter(num - 1, num * product)

print(my_fact_iter(2,3))