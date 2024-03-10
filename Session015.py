from session15a import *
from session15c import *
import datetime
from session15b import *

def main_menu():
    message = """
    >>Main Menu<<
    1. Manage Customers
    2. Manage Pets
    3. Manage Consultations
    0. Quit
    """

    print(message)
    choice = int(input("Enter your choice:"))

    while True:
        if choice == 1:
            customer_menu()
        elif choice == 2:
            pets_menu()
        elif choice == 3:
            Consultation_menu()
        elif choice == 0:
            break
        else:
            print("Invalid choice")
            break
        print(message)
        choice = int(input("Enter your choice:"))

def main():

    date1 = datetime.datetime.today()

    welcome = """
    -------------------
    Welcome to Vets App
    -------------------
    """
    print(welcome)

    main_menu()

    bye_message = """
    ----------------------------
    Thank you for using Vets App
    ----------------------------
    """
    print(bye_message)

    date2 = datetime.datetime.today()
    print("App Usage:", date2-date1)


if __name__ == "__main__":
    main()