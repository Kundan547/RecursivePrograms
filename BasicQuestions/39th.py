demo = {"Name":"Arshan",
         "Age": 21,
         "location":"Delhi"
        }
demo2 = {"Number":123456,
         "Goal":"Killthemall",
         "DOB":2002
}

dict = {**demo, **demo2}

print(dict)

SET = set(dict)
print(SET)

List = list(SET)
print(List)

Tuple = tuple(List)
print(Tuple)