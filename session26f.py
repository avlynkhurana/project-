def fetch():
    file = open("ipl-data-2022.csv","r")
    lines = file.readlines()

# y
    for line in lines:
        yield line


result = fetch()
print("result is:",result)

#how to use with loop explore yourself
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result,"no more record"))

while True:
    data = next(result,"Nothing")
    print(data)
    if data == "Nothing":
        break