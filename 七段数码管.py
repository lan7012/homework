import turtle as t      #海龟画图#
import time             #显示当前系统时间#
def kg():               #每段画线前后存在的间隔#
    t.pu()
    t.fd(5)
def dl(d):              #画每一条线的基础函数#
    kg()
    t.pd() if d else t.pu()
    t.fd(40)
    kg()
    t.right(90)
def dd(s):              #从0-9数字显示的画线#
    dl(True) if s in [2, 3, 4, 5, 6, 8, 9] else dl(False)
    dl(True) if s in [0, 3, 4, 5, 6, 7, 8, 9] else dl(False)
    dl(True) if s in [0, 2, 3, 5, 6, 8, 9] else dl(False)
    dl(True) if s in [0, 1, 2, 6, 8] else dl(False)
    t.left(90)
    dl(True) if s in [0, 1, 4, 5, 6, 8, 9] else dl(False)
    dl(True) if s in [0, 2, 3, 5, 6, 7, 8, 9] else dl(False)
    dl(True) if s in [0, 2, 3, 4, 7, 8, 9] else dl(False)
    t.left(180)
    t.pu()
    t.fd(20)
def ip(sr):             #输入值的提取#
    for i in sr:
        if i in '+':
            t.write('年', font=('Arial',18))     #font设置字体与大小#
            t.fd(40)
        elif i in '-':
            t.write('月', font=('Arial',18))
            t.fd(40)
        elif i in '*':
            t.write('日', font=('Arial',18))
        else:
            dd(eval(i))
def main():             #画图基础设置#
    t.setup(800, 800)
    t.pu()
    t.fd(-300)
    t.pensize(5)
    t.pencolor("white")
    t.bgcolor("black")
    ip(time.strftime('%Y+%m-%d*', time.gmtime()))
    t.hideturtle()
    t.done()
main()                  #执行画图#