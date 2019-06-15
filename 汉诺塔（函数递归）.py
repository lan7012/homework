s = 0
def hnt(n, a, c, b):
    global s
    if n == 1:
        print("{}:{}->{}".format(1, a, c))
        s += 1
    else:
        hnt(n- 1, a, b, c)
        print("{}:{}->{}".format(n, a, c))
        s += 1
        hnt(n- 1, b, c, a)
hnt(3, "A", "C", "B")
print(s)