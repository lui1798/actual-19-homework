

def wrapper():

    def func():
        print("hello world")
        

    return func



f = wrapper()
f()
