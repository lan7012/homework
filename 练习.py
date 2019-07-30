import random
boy = 0
girl = 0
for a in range(1000):
    i = random.randint(1, 2)
    if i == 1:
        boy += 1
    else:
        girl += 1
print("男孩{}女孩{}".format(boy, girl))