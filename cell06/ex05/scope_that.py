#!/usr/bin/env python3
def add_one(x):
    return x + 1

num = 2
print(num)

add_one(num)
'''ไม่ได้เอาค่า+1 มาเก็บใน num'''
print(num)

num = add_one(num)
print(num)
