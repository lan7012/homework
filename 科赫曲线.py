import turtle as t
def kh(s, n):
    if n == 0:
        t.fd(s)
    else:
        for a in [0, 60, -120, 60]:
            t.left(a)
            kh(s/ 3, n- 1)
def main():
    t.pu()
    t.goto(-200, 100)
    t.pd()
    t.hideturtle()
    t.pensize(3)
    t.pencolor("white")
    t.bgcolor("black")
    t.begin_fill()
    t.color("white")
    for i in range(3):
        t.seth(-120* i)
        kh(300, 3)
    t.end_fill()
    t.done()
main()