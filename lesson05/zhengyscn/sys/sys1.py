import sys
'''
0 stdin
1 stdout
2 stderr

'''

fd = open("tmp.log", 'a')
sys.stdout = fd
sys.stderr = fd


print("hello world")

print(2 + 3)

print(name)

fd.close()