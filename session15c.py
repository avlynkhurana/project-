from tabulate import tabulate
from new2 import DBHelper
from session15 import Pet
from new import *

def pets_menu():

    db = DBHelper()
    message = """
         >>>Pets Menu<<<
        1: Add Pets
        2: Update Pets
        3: Delete Pets
        4: View All Pets
        5: View Pets by Phone
        0: Quit
"""
    print(message)
    choice = int(input("Enter your choice:"))

    pet = Pet()
    customer = Customer()

    while True:
        if choice == 1:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            pet.cid = customer.cid

            pet.read_pet_data()
            print(vars(pet))

            sql = pet.get_insert_sql_query()
            db.execute_sql(sql)
            print("Pet Added Successfully......")
        elif choice == 2:
            phone = input("Enter Phone")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns))

            customer_fetched = rows[0]

            print(customer_fetched)
            customer.cid = customer_fetched[0]
            print(customer.cid)
            # cid = str(pet.cid)
            pet.cid = customer.cid
            sql = pet.get_pet_sql_query(str(pet.cid))

            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns))

            pet_fetched = rows[0]
            pet.cid = pet_fetched[0]

            if len(rows) == 0:
                print("NO PET")
            elif len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                pet.pid = int(input("Enter pet ID:"))

            pet.name = input("Enter name:")
            if len(pet.name) == 0:
                pet.name = pet_fetched[1]

            pet.age = int(input("Enter age:"))
            if pet.age == 0:
                pet.age = pet_fetched[2]
            else:
                pet.age = int(pet.age)

            pet.weight = input("Enter weight:")
            if len(pet.weight) == 0:
                pet.weight = pet_fetched[3]

            pet.breed = pet_fetched[4]

            pet.gender = pet_fetched[5]
            pet.cid = pet_fetched[6]
            pet.createdon = pet_fetched[7]

            sql = pet.get_pet_update_sql_query()
            db.execute_sql(sql)
            print("Pet Updated :)")
        elif choice == 3:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            pet.pid = int(input("Enter Pet Id:"))
            delete_choice = input("Are You Sure to Delete ? (yes/no): ")

            if delete_choice == "yes":
                sql = pet.get_delete_pet_sql_query()
                db.execute_sql(sql)
                print("Pet Deleted...")

        elif choice == 4:
            sql = pet.get_pet_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("Invalid choice")
            break
        print(message)
        choice = int(input("Enter your choice:"))