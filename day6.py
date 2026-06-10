a = {
    "name":"Rohit",
    "age":11,
    "isactive":True
}

print(type(a))

print(a)

print(a["name"])
# print(a["names"]) Key error there is no names key in a
a = {
    "name":"Rohit",
    "age":11,
    "isactive":True,
    "name":"Rohan",
    "data":11
}
print(a)
print(len(a))
print(a.keys())
print(a.values())
print(a.items())
#print(aa["ages"])
print(a.get('age'))
print(a.get('ages',False))

a = {
    "name":"Boardway",
    "address":"Nepal"

}
a['address']="kathmandu"
a["number"]=984432

print(a)
print("\n \n")
print("--------Update---------")
a = {
    "name":"Boardway",
    "address":"Nepal" 
}
print(a)
a.update({
    "name":"Mr Rohit",
    "age":18,
    "number":9767957691
})
print(a)
print("-------------"*4)
a = {
    "name":"Rohit",
    "age":13,
    "number":13332,
    "address":"ktm",
    "level":"hard",
    "role":"developer"

}
del a['name']
print(a)

#pop
result=a.pop("level")
print(a)

print(result)

result = a.popitem()
print(a)
print(result)

# Nested Distionaries
info = {
    "name":"boardway",
    "phone":{
        "temp":123,
        "per":5666
    }
}
print(info["phone"]["temp"])

user_info = {
    "name":"Rohit",
    "number":[
        {
            "type":"jio",
            "number":98443
},
         {
            "type":"ncell",
            "number":98345
         }

    ]
}
# Output
'''
Rohit jio number is 9844,
Rohit ncell number is 98345
'''

print(user_info["name"], user_info["number"][0]["type"], "number is",user_info["number"][0]["number"])
print(user_info["name"], user_info["number"][1]["type"], "number is",user_info["number"][1]["number"])