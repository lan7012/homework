txt = '''
一一一一一一一，二二二二二二二。
三三三三三三三，四四四四四四四。
'''
a = ['，', '。']
for b in a:
    c = txt.replace(b,' ')
print(c)