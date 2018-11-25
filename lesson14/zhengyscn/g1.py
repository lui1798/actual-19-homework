
'''
    游戏： 人狗大战

'''

import random

class NewPerson(object):

    def __init__(self, name, age, life_value):
        self.name = name
        self.theage = age
        self.life_value = life_value
        self.aggr = random.randint(5, 10)

    def attack(self, obj):
        print('%s攻击了%s'%(self.name, obj.name))
        obj.life_value -= self.aggr



class Dog(object):

    def __init__(self, name, type):
        self.name       = name
        self.dog_type   = type
        self.aggr       = random.randint(5, 10)
        self.life_value = 2000

    def bite(self, obj):
        print('%s咬了%s'%(self.name, obj.name))
        obj.life_value -= self.aggr



'''

pp = Person('pp', 38, 1000)
dog = Dog('egon', '二哈')


while True:
    dog.bite(pp)
    print("人的生命值：{}".format(pp.life_value))
    pp.attack(dog)
    print("狗的生命值：{}".format(dog.life_value))

    if pp.life_value <= 0 or dog.life_value <=0:
        print("Game Over.")
        break

    print("--------------------------")
    import time
    time.sleep(2)
'''


class Animal(object):
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;

    def eat(self):
        print('%s is eating'% self.name)



class Person(Animal):

    def __init__(self, name, aggressivity, life_value, tel):
        super(Person, self).__init__(name, aggressivity, life_value)
        self.tel = tel

    def get_tel(self):
        return self.tel

p = Person('monkey', '20', '1000', '132xx11x')
p.eat()

print(p.get_tel())


































