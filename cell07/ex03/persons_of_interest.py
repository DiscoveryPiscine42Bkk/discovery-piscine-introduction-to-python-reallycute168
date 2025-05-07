#!/usr/bin/env python3

def famous_births(scientist):
    persons = [(keep["name"], int(keep["date_of_birth"]))
        for keep in scientist.values()]
    '''เช็คเพื่อเรียงค่า key(ใช้อะไรเป็นเกณฑ์)'''
    '''lambda x: x[1](ใช้ใช้ ค่าที่ตำแหน่งที่1 ของtuple(x[1]) คล้ายlist แต่เปลี่ยนค่าไม่ได้เป็นตัวจัดเรียง)'''
    persons.sort(key=lambda x: x[1])
    for name, year in persons:
        print(f"{name} is a great scientist born in {year}.") 

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
