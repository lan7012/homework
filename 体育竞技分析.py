import random as r
def printtip():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1的小数表示）")

def gameover(a, b):
    return a == 15 or b == 15

def ip():
    a = eval(input("请输入A选手的能力值："))
    b = eval(input("请输入B选手的能力值："))
    n = eval(input("清输入场次数："))
    return a, b, n

def printend(vA, vB):
    n = vA + vB
    print("共模拟{}场比赛".format(n))
    print("A获胜{}场比赛，占比{:0.1%}".format(vA, vA / n))
    print("B获胜{}场比赛，占比{:0.1%}".format(vB, vB / n))

def OG(powerA, powerB):
    fsA, fsB = 0, 0
    up = "A"
    while not gameover(fsA, fsB):
        if up == "A":
            if r.random() < powerA:
                fsA += 1
            else:
                up = "B"
        else:
            if r.random() < powerB:
                fsB += 1
            else:
                up = "A"
    return fsA, fsB

def NG(n, powerA, powerB):
    vA, vB = 0, 0
    for i in range(n):
        fsA, fsB = OG(powerA, powerB)
        if fsA > fsB:
            vA += 1
        else:
            vB += 1
    return vA, vB

def main():
    printtip()
    powerA, powerB, n = ip()
    vA, vB = NG(n, powerA, powerB)
    printend(vA, vB)

main()