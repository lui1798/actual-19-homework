

class Person(object):
    '''
        类的属性
    '''
    name = "monkey"
    age = 20
    tel = "132xxx"




class NewPerson(object):
    '''
        实例的属性
    '''
    def __init__(self, name, age, tel):  # 构造函数
        self.name = name
        self.age = age
        self.tel = tel

    # 实例的方法
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def incr_age(self):
        self.age += 1


p = NewPerson(name="monkey", age=20, tel="132xxx")
# print(p.name, p.age, p.tel)

p.incr_age()
p.incr_age()
print(p.get_age())
