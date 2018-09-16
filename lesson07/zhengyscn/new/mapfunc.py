def add(name):
    return "add" + name

def sub(name):
    return 'sub func'

def mul(name):
    return 'mul func'

def div(name):
    return 'div func'

funcMap = {
        'add' : add,
        'sub' : sub,
        'mul' : mul,
        'div' : div,
    }



if __name__ == '__main__':
    op = input("Please input your action: ")
    # add = funcMap['add']
    # add()
    name = input("Please input your name: ")
    print(funcMap[op](name))