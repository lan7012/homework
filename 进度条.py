#文本进度条#
from time import *
s = 50
start = perf_counter()
print("执行开始".center(s, '-'))
for i in range(s+ 1):
    a = '*'* i
    b = '-'* (s- i)
    c = (i/ s)* 100
    d = perf_counter()- start
    sleep(0.1)
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, d), end="")
print("\n"+ "执行结束".center(s, '-'))