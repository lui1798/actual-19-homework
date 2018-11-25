import copy


a1 = [1, 2, 3, ["11", "22", "33"], 4, 5, 6]
a2 = copy.deepcopy(a1)


# a1[-1][-1] = "abc"
a1[3][0] = "abc"
print(a1 == a2)

