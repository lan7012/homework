def g():
    t = open("D:\h.txt", "r").read()
    t = t.lower()
    for i in '~!@#$%^&*()_+{}|:"<>?`-=[];,./':
        t = t.replace(i, " ")
    return t
w = g().split()
c = {}
for i in w:
    c[i] = c.get(i, 0)+ 1
items = list(c.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    a, b = items[i]
    print("{:<10}{:>5}".format(a, b))