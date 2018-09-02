import os
import time

# try:
#     os.mkdir("/tmp/123dir")
# except FileExistsError:
#     pass
#
# os.rmdir("/tmp/123dir")

# os.mkdir("/tmp/123dir/345dir")
# os.makedirs("/tmp/123dir/345dir", exist_ok=True)

print(os.getpid(), os.getppid())
print(1)
pid = os.fork()

print(2)
if pid == 0:
    print("child>>> ", os.getpid(), os.getppid())
    time.sleep(10)
    print("child")
else:
    print("hello world")
    print("parent>>> ", os.getpid(), os.getppid())
    os.wait()
    print("parent end")


print(os.getpid(), os.getppid())