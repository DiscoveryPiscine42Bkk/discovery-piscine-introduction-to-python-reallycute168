#!/usr/bin/env python3
import sys

def downcase(text):
    return text.lower()

if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        print(downcase(x))
else:
    print("none")
