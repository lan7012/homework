import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
t.hideturtle()
#数据读取
sj = []
f = open("D:/data.txt")
for line in f:
    line = line.replace("\n", " ")
    sj.append(list(map(eval, line.split(","))))
f.close()
#自动绘制
for i in range(len(sj)):
    t.pencolor(sj[i][3], sj[i][4], sj[i][5])
    t.fd(sj[i][0])
    if sj[i][1]:
        t.right(sj[i][2])
    else:
        t.left(sj[i][2])
t.done()