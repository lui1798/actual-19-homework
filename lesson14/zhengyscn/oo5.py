import random

class Person(object):

    age = 0

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


    # @classmethod
    # def incr_age(cls):  # 类的方法
    #     cls.age += 1

    def incr_age(self):
        self.age += 1


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    @staticmethod
    def random_num():   # 静态方法
        '''
            工具类
        '''
        return random.randint(10, 100)







p = Person('momkey', '140', '200')
p.incr_age()
p.incr_age()
print("p {}".format(p.get_age()))


print(Person.age)
print(p.random_num())


# p1 = Person('momkey', '140', '200')
# print("p1 {}".format(p1.get_age()))