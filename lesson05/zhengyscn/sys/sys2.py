import sys

'''
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

'''

def println(value=None, end='\n'):
    if value:
        sys.stdout.write(str(value)+end)
    else:
        sys.stdout.write("\n")

def inputln(prompt=None):
    println(prompt, end="")
    sys.stdout.flush()
    cmd = sys.stdin.readline()
    println(cmd)


def main():
    # println(123, end="")
    inputln("Please input your username: ")

if __name__ == '__main__':
    main()