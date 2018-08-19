

str_exp = "abcdefabc"
pos_n = str_exp.index("ab", str_exp.index("ab") + 1)
print(pos_n)
pos_n1 = str_exp.find("z")
print(pos_n1)
def index_of_str(s1, s2):
    lt=s1.split(s2,1)
    print (lt)
    if len(lt)==1:
        return -1
    return len(lt[0])
print(index_of_str('12abc34de5f', 'c34'))
