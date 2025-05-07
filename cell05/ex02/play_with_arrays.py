#!/usr/bin/env python3
num =  [2, 8, 9, 48, 8, 22, -12, 2]
newnum = []
for x in num:
    result = x + 2
    if result >= 5 :
        newnum.append(result)
print(num)
print(newnum)
