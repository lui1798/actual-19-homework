



class Person(object):
    name = "ccc"

    @classmethod  # 类的方法
    def set_name(cls, value):
        '''
        cls -> Person
        '''
        print("cls")
        # cls.name = value
        # return cls.name
        Person.name = value
        return Person.name


    def set_name(self, value):   # 对象 or 实例的方法
        '''
        self --> p
        '''
        print("self")
        self.name = value
        return self.name




p = Person()
p.set_name("monkey")
print(p.name)



# p1 = Person()
# p1.name = "xxx"
# p1.age = 20
#
#
# Person.tel = "132xxx"
# print(p1.tel)
