

class Person(object):

    def __init__(self, name, age):
        self.__name = name  # 私有属性 private
        self.age = age      # 共有属性 public

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value):
        self.__name = value





p = Person('monkey', 20)
print(p.name)

p.set_name = "xxx"
print(p.name)
