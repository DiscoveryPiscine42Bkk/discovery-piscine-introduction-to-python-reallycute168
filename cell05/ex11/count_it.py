#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        text = sys.argv[i]
        print(f"{text}: {len(text)}")
else:
    print("none")
