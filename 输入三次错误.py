c = 0
while c < 3:
    a = input()
    b = input()
    if a == "Kate" and b == "666666":
        print("登陆成功！")
        break
    else:
        c += 1
        if c == 3:
            print("3次用户名或密码均有误，退出程序")