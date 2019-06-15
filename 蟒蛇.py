#海龟画蟒蛇#
from turtle import *
setup(800, 800, 200, 200)
pu()
fd(-200)
pd()
pencolor("pink")
bgcolor("black")
pensize(25)
seth(-40)
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/ 2)
fd(40)
circle(40/ 2, 180)
fd(40* 2/ 3)
done()