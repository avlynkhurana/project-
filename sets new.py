john_followers = {"fionna","jack","kim","george","joe"}
print("john_followers:",type(john_followers))

numbers = list(range(10,101,10))
print("numbers:",type(numbers))

numbers = set(numbers)
print("numbers now:",numbers)

numbers.add(10)
numbers.add(110)
numbers.add(20)
numbers.add(220)
print("numbers after add:",numbers)
#explore how duplicate elements can be removed without functions
numbers.pop()
numbers.pop()
print("numbers after pop:",numbers)

numbers.remove(50)
numbers.discard(30)
print("numbers after remove:",numbers)

john_followers = {"fionna","jack","kim","george","joe"}
jack_followers = {"leo","anna","harry","mike","joe"}
fionna_followers = {"sia","joe"}
print("john_followers:",john_followers)
print("jack_followers:",jack_followers)
print("fionna_followers:",fionna_followers)
followers = john_followers.intersection(jack_followers)
print("followers:",followers)

print(fionna_followers.issubset(john_followers))
print(fionna_followers.issuperset(john_followers))
print("issubset:",fionna_followers.issubset(john_followers))
print("issuperset:",john_followers.issubset(fionna_followers))

A={1,2,3,4,5}
B={4,5,6,7,8}

C=A-B
print("C is:",C)

D=A&B
print("D is:",D)

E=A^B
print("E is:",E)

F=A|B
print("F is:",F)

#IMP FOR INTERVIEW
G=A.symmetric_difference(B)
print("G is:",G)

