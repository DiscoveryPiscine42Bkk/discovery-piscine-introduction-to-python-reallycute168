#!/usr/bin/env python3
num =  [2, 8, 9, 48, 8, 22, -12, 2]
print(num)
newnum = []
for x in num:
    '''append(data)'''
    if x >= 5 :
        newnum.append(x + 2)
'''set ลบค่าซ้ำ'''
newnum2 = set(newnum)
print(newnum2)
