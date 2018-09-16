import sys

def exit():
    sys.exit(0)

mapFunc = {'exit' : exit}
while 1:
    mapFunc['exit']()
