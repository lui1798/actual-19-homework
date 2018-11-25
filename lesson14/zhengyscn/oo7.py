class Foo(object):

    def __init__(self,val):
        self.__NAME=val #将所有的数据属性都隐藏起来

    @property
    def name(self):
        return self.__NAME #obj.name访问的是self.__NAME(这也是真实值的存放位置)

    # @name.setter
    def set_name(self,value):
        if not isinstance(value,str):  #在设定值之前进行类型检查
            raise TypeError('%s must be str' %value)
        self.__NAME=value #通过类型检查后,将值value存放到真实的位置self.__NAME





f=Foo('egon')
print(f.name)
f.set_name = '10'
print(f.name)
# f.name=10 #抛出异常'TypeError: 10 must be str'
# del f.name #抛出异常'TypeError: Can not delete'