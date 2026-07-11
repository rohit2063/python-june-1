# info = {
#     "name" : "Rohit Ghimire",
#     "learning" : ["Python", "java", "C++"],
#     "topics" : ("dic", "set"),
#     "age" : 34.5,
#     "is_adult" : True
# }
# print(type(info))
# print(info[1]) dic don't print the data according to index
# print(info["name"])
# print(info["age"])
# print(info["is_adult"])
# info["name"] = "Rohit"
# info["surname"] = "Ghimire"
# print(info)


# student = {
#     "name" : "Darshan Rokkya",
#     "subjects" :{
#         "phy" : 56,
#         "che" : 88,
#         "math" :67
#     }

# student.update({"name": "Rohit Ghimire", "age": 18})
# print(student)
# print(student["name"] , student["subjects"]["phy"])
# print(len(list(student.values())))
# print(len(student))
# pairs = list(student.items())
# print(pairs)

# print(student["name1"]) # Error
# print(student.get("name")) #no Error

# Set
# nums = set()
# nums.add(1)
# nums.add(2)
# nums.add((1,2,3,4))
# nums.clear()
# nums.remove(3) #Error no key
# print(nums)
# print(type(nums))
# print(len(nums))
# nums.clear()

# collection = {"hello","world","apna ", "college"}
# collection1 = {"hello",1,2,3,4}
# print(collection.union(collection1))
# print(collection.intersection(collection1))

# collection ={
#     "table" : {"a piece of furniture",
#     "list of fact & figures"},
#     "cat" : "a small animal"
# }
# print(collection)

# classroom = ["python","java","C++","python","javascript","java","python","java","C++","C"]
# print(type(classroom))
# # print(len(set(classroom)))
# a = set(classroom)
# print(len(a))

# marks = {}
# b = int(input("Enter your phy marks:"))
# marks.update({"phy" : b})
# d = int(input("Enter your chem marks:"))
# marks.update({"chem" : d})
# f = int(input("Enter your math marks:"))
# marks.update({"math" : f})
# print(marks)

# a = {("float" ,9), ("int" ,9.0)}
# print(a)