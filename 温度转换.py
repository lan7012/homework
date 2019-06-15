#温度转换#
a = input()
if a[-1] in ('f', 'F'):
    C = eval(a[0: -1])/1.8 - 32
    print("{:.2f}C".format(C))
elif a[-1] in ('c', 'C'):
    F = eval(a[0: -1])+ 1
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")