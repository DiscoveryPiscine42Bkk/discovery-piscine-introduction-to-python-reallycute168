#!/usr/bin/env python3
import sys
if len(sys.argv) != 3:
    print("none")
else:
    num = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(list(range(num, num2 + 1)))
    