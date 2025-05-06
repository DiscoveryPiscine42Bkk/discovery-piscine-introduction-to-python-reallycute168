#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    text = input("What was the parameter? ")
    args = sys.argv[1]
    if text == args:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
