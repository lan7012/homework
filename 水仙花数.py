#水仙花数#
s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]), 3)+ pow(eval(t[1]), 3)+ pow(eval(t[2]), 3) == i:
        s += "{},".format(t)
print(s[: -1])