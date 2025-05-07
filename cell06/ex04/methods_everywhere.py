#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s + "Z" * (8 - len(s)))

args = sys.argv

if len(args) == 1:
    print("none")
else :
    for text in args:
        if len(text) > 8:
            shrink(text)
        elif len(text) < 8 :
            enlarge(text)
        else :
            print(text)
