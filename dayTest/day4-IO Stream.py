# Python内置的os模块也可以直接调用操作系统提供的接口函数
import os

print(os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.environ)
# 查看环境变量文件

# 查看当前目录的绝对路径:
os.path.abspath('.')
# '/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')

# 序列化
import pickle

d = dict(name='terry', age=23)
pickle.dumps(d)
# pickle.dumps()方法把任意对象序列化成一个bytes


# Json
import json


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age
    }


stu = Student('terry', 23)

print(json.dumps(stu, default=student2dict))
