names = "John, Jennie, Jim, Jack, Joe"
print(len(names))
print(names[1])
print(names[len(names)-1])

split_names = names.split(", ")
print(split_names,type(split_names))

s1=names.replace("Jim","Mike")
print("names:",names)
print("s1:",s1)
