class Employee(object):
    pass

# 动态绑定属性
e = Employee()
e.name = 'terry'
print(e.name)

# 动态绑定方法
from types import MethodType
def set_salary(self, salary):
    self.salary = salary


e.set_salary = MethodType(set_salary, e)
e.set_salary(2500)
print(e.salary)

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：



# @property装饰器就是负责把一个方法变成属性调用的
class Student2(object):
    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score is not int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self.score = value


# __getAttr__ 动态返回一个属性
class Student3(object):
    def __getattr__(self, item):
        if item == 'haha':
            return 'xixi'
        if item == 'func':
            return lambda : 'this is function'
        return 'shabi'

stu3 = Student3()
print(stu3.haha, stu3.func())

# __call__ 动态调用
class Student4(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student4('Michael')
s()


# 定义枚举类
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 元类
a = 1
print(type(a),'------',a.__class__,'---------',a.__class__.__class__)
# __metaclass__     写一个类的时候为其添加__metaclass__属性
class Foo(object):
    # Python就会用元类来创建类Foo
    # 可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。
    # 那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。
    # __metaclass__
    pass

