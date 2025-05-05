#!/usr/bin/env python3
import sys
if len(sys.argv) > 1: '''len ไว้นับรายการ'''
    print("none")
else:
    table = 0
    while table <= 10:
        X = f"Table de {table}:" """X เก็บข้อความ ส่วนtableloopเลขเรื่อยๆ"""
        multi = 0
        while multi <= 10:
            X += f"{table * multi}" """คำนวณค่าต่อเข้า X"""
            multi += 1
        print(X)
        table += 1 """กลับไปลูป table <=10 """
