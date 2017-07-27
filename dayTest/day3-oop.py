# 创建类实例
class Student1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

terry = Student1('terry', '98')
terry.print_score()

# 得到get和set方法
class Student2(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name
    def get_score(self):
        return self._score

    def set_name(self, name):
        self._name = name
    def ser_score(self, score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s %s' % (self._name, self._score))

terry = Student2('terry', '98')
terry.print_score()

# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')
    def eat(self, food):
        print('Dog eat %s' % food)


class Cat(Animal):
    def run(self):
        print('Cat is runnning')

Koji = Dog()
Koji.eat('banana')


# 获取对象信息
# type()
t1 = type('123')
t2 = type(Koji.eat)
t3 = type(None)
t4 = type([1, 2, 3])
print('t1=%s t2=%s t3=%s t4=%s' % (t1, t2, t3, t4))

#isinstance
isinstance(Koji, Dog)

# dir() --获取对象的所有属性和方法


# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
#Student
print(Student.name) # 打印类的name属性
#Student
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
#Michael
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
#Student
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#Student
