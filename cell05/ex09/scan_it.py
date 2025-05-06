#!/usr/bin/env python3
import sys
if len(sys.argv) == 3:
    text = sys.argv[1]
    text1 = sys.argv[2]
    ans = text1.count(text)
    print(ans)
else:
    print("none")
