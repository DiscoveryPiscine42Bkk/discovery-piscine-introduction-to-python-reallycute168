#!/usr/bin/env python3

def array_of_names(persons):
    result = []
    '''.item คือ (key , values)'''
    for first, last in persons.items():
        full = f"{first.capitalize()} {last.capitalize()}"
        result.append(full)
    return result

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))
