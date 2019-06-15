#天天向上#
def a(b):
    a = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            a = a* (1- 0.01)
        else:
            a = a* (1+ b)
    return a
c = 0.01
while a(c)< 37.78:
    c += 0.001
print("{:.3f}".format(c))