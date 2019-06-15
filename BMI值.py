#BMI值#
try:
    s, t = eval(input("请分别输入身高体重用逗号隔开："))
    if s > 100:
        s /= 100
    if t > 85:
        t /= 2
    BMI = t/ s** 2
    a, b = "", ""
    if BMI < 18.5:
        a, b = "偏瘦", "偏瘦"
    elif 18.5 <= BMI < 24:
        a, b = "正常", "正常"
    elif 24 <= BMI < 25:
        a, b = "偏胖", "正常"
    elif 25 <= BMI < 28:
        a, b = "偏胖", "偏胖"
    elif 28 <= BMI < 30:
        a, b = "肥胖", "偏胖"
    elif BMI >= 30:
        a, b = "肥胖", "肥胖"
    print("BMI值为{:.1f}\n国内标准为{}\n国际标准为{}".format(BMI, a, b))
except:
    print("输入格式错误")