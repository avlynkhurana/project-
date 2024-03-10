names = "John, Jennie, Jim, Jack, Joe"
#INDEXING
print(len(names))
print(names[1])
print(names[3])
print(names[-1])
print(names[1:5])
new_names = names*2
print(new_names)

names = names+",Kia"
print(names)
print("Kia"in names)
print("George" not in names)