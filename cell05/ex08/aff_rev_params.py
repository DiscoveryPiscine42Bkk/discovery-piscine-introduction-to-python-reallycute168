#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    text = sys.argv[1:]
    text.reverse()
    '''.join จะรวมค่าทุกตัวเป็น str ไม่ใส่จะเป็น list[]'''
    print(" ".join(text))
else:
    print("none")
