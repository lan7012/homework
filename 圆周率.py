#圆周率#
from random import *
from time import *
s = 1000000
start = perf_counter()
yn = 0
for i in range(s+ 1):
    x, y = random(), random()
    l = (x** 2+ y** 2)** 0.5
    if l <= 1:
        yn += 1
pi = 4* (yn/ s)
print("圆周率为:{}\n运行时间为:{:.2f}".format(pi, perf_counter()- start))