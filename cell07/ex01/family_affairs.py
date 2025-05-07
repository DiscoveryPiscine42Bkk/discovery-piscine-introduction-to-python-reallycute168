#!/usr/bin/env python3

def find_the_redheads(dupont_family):
    result = []
    '''.item คือ (key , values)'''
    for name, color in dupont_family.items():
        if color == "red":
            result.append(name)
    return result

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
