idnum = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
younum = ''
print('请输入前17位数字')
print('12312320190606000')
younum = str(input(''))

num = 0
i = 0
while i < 17:
    num = num + int(younum[i]) * idnum[i]
    i = i + 1

end = num % 11
endnum = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
print('最后一位是：' + str(endnum[end]))
print(str(younum[0:17]) + str(endnum[end]))
#f = open('身份证校验位.txt', 'w')
#f.write('最后一位是：' + str(endnum[end]) + '\n' + str(younum[0:17]) + str(endnum[end]))
#f.close()