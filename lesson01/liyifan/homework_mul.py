n = 0

while True:
    n += 1
    if n > 9:
        break
    else:
        for m in range(1,n+1):
            f = m * n
            if f < 10:
                space = "   "
            else:
                space = "  "
            print("{} * {} = {}".format(m,n,f),end=space)
        print(" ")
