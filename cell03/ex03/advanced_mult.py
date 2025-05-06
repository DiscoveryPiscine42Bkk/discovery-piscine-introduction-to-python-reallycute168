#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    print("none")
else:
    table = 0
    while table <= 10:
        X = f"Table de {table}:"
        multi = 0
        while multi <= 10:
            X += f" {table * multi}"
            multi += 1
        print(X)
        table += 1
