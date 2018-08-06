# -*- coding: utf-8 -*-
for m in range(1, 10):
    for n in range(1, m + 1):
        outcome = m * n
        print("{} * {} = {}".format(m, n, outcome), end=' ')
    print()
