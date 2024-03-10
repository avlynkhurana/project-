def show(func):
    print("Show Executed")
    func()

def hello():
    print("This is hello")
    print("Hello function finished...")

show(hello)

def bye():
    print("This is bye")
    print("Bye function finished...")

show(hello)
print("##################")
show(bye)

