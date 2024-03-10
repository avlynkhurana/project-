import datetime

class Customer():
    def _init_(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.age = int(input("Enter age"))
        self.gender = input("Enter Gender:")
        self.address = input("Enter address:")
        self.createdon = datetime.datetime.today()
