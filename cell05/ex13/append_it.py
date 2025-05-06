#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
    print("none")
else:
    for text in sys.argv[1:]:
        if not text.endswith("ism"):
            print(text + "ism")
