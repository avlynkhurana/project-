file = open("ipl_data-2022.csv", "r")

lines = file.readlines()

for line in lines:
    print(line)

with open("ipl_data-2022.csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)