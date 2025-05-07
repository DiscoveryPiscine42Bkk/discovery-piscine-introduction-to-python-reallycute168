#!/usr/bin/env python3
import sys

def greetings(name = None):
    if isinstance(name , str):
        if name == "":
            print('Hello, noble stranger')
        else :
            print(f'Hello,{name}')
    elif name is None:
        print('Hello, noble stranger')
    else :
        print('Error! It was not a name.')

greetings('Phachthanasorn')
greetings('Peerawatkul')
greetings()
greetings(42)
