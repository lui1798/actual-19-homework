import functools

def fxxxx(f):
    def fyyy():
        print("hello")
        f()
        print("world")
    #return fyyy
    return functools.wraps(f)(fyyy)


@fxxxx
def f1():
    print("------- {}".format(f1.__name__))


# @fxxxx
def f2():
    print("------- {}".format(f2.__name__))

'''
def fxxxx():
    def fyyy():
        print("hello")
        print("world")
    return fyyy


func = fxxxx()
func()
'''


# func = fxxxx(f2)
# func()


f1()

f2()








# func = f1
# func()



# print('hello')
# f1()
# print("world")
#
#
# print('hello')
# f2()
# print("world")