import datetime

def show():
    print("This is show")
    print("Today is:",datetime.datetime.today())

hello = show

print("show is:",show)
print("hello is:",hello)

