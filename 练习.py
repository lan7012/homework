for i in [-5.0, -3.0, 1.0, 2.0, 2.5, 3.0, 5.0]:
    x = i
    if x<0 and x!=-3:
        y = x**2 + x + 6
    elif 0<=x<5 and x!=-3 and x!=2:
        y = x**2 - 5 * x + 6
    else:
        y = x**2 - x - 1
    print(y, end=",")