
# def f1(s):
#     return s.upper()
#
#
# s = f1('abc')
# print(s)


# f = lambda s:"---{}".format(s.upper())
# s = f('abc')
# print(s)

def func(x):
    return x[0]

dic = {'a':2, 'c' : 3, 'd' : 1}
print(dic)
sort_dic = sorted(dic.items(), key=func, reverse=False)
sort_dic = sorted(dic.items(), key=lambda x:x[0], reverse=False)
print(sort_dic)


# sorted
    # list
    # dict

# print(dic.items())

# ret_dic = []
# for k, v in dic.items():
#     if (k, v) in ret_dic:
#         idx = ret_dic.index((k, v))
#         if ret_dic[-1][-1] > v:
#             ret_dic.insert(idx+1, (k, v))
#         else:
#             ret_dic.insert(idx, (k, v))
#     else:
#         ret_dic.append((k, v))
#
#
# print(ret_dic)