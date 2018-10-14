

def wrapper():

    def func():
        print("hello world")
        return 1
        

    return func()



f = wrapper()

f == func()
#f()
print(">> f: ", f)
