

class Person(object):
    '''
        Person desc
    '''
    name = ""

    # 类的方法
    @classmethod
    def set_name(cls, value):
        cls.name = value
        return cls.name



'''
p = Person()   # 对Person进行实例化


# 动态添加实例属性
p.name = "monkey"
p.age = 20
p.tel = "132xxxx"


# 实例的属性
print(p.name)
print(p.age)
print(p.tel)

print(Person.name)
'''
'''
# 类的属性
Person.name = "zhengyscn"
Person.age = 20

# 实例访问类的属性
p = Person()
print(p.name)
print(p.age)

Person.height = 200
print(p.height)


p.name = "monkey"
print(Person.name)
print(p.name)




print(dir(p))


    优先找对象 or 实例下的属性， 如果找不到就找类下的属性; 如果还找不到 就报错；
'''


# class Person(object):
#     name = "monkey"
#     age = 20
#
#
# p = Person()
# print(p.name)
# print(p.age)
#
#
# # p.name = "monkey1"
# # print(Person.name)
#
# p.tel = "132xxx"
# print(Person.tel)


p = Person()

# p.name = "xxxx"
p.set_name("xxxx")

print(Person.name)

p1 = Person()
print(p1.name)













