def num():  # 获得用户不定长度的输入#
    n = []
    ip = input("请输入数字，空格结束：")
    while ip != " ":
        n.append(eval(ip))
        ip = input("请输入数字，空格结束：")
    return n

def pjs(nums):  # 计算平均数#
    l = 0.0
    for i in nums:
        l += i
    return l/ len(nums)

def fc(nums, pjs):  # 计算方差#
    s = 0.0
    for i in nums:
        s += (i- pjs) ** 2
    return pow(s/ (len(nums)- 1), 0.5)

def zws(nums):  # 计算中位数#
    sorted(nums)
    size = len(nums)
    if size % 2 == 0:
        z = (nums[size// 2- 1] + nums[size// 2])/ 2
    else:
        z = nums[size// 2]
    return z

a = num()
b = pjs(a)
print("平均数:{},方差:{:.2f},中位数:{}".format(b, fc(a, b), zws(a)))
