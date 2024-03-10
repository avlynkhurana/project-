from session16 import *
from new2 import DBHelper
from session15c import *
from new import Customer

def Consultation_menu():
    message = """
        1: Add Consultation
        2: Update Consultation
        3: Delete Consultation
        4: View all Consultation
        5: View Consultations by Date
        6: View Consultations Pets Consul12tation
        0: Quit
"""
    print(message)
    choice = int(input("Enter your choice:"))

    pet = Pet()
    customer = Customer()
    consultation = Consultation()
    db = DBHelper()

    while True:
        if choice == 1:
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

            if len(rows) == 0:
                print("Please add Pet first....")
                break
            if len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                pet.pid = int(input("Enter Pet ID:"))

            consultation.cid = customer.cid
            consultation.pid = pet.pid
            consultation.read_consultation_data()

            print(vars(consultation))

            sql = consultation.get_insert_consultation_sql_query()
            db.execute_sql(sql)
            print("Consultation Added Successfully......")

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
            print("Pet Updating :)")

            pet.breed = pet_fetched[4]

            print("Pet Updating :)")
            pet.gender = pet_fetched[5]
            pet.cid = pet_fetched[6]
            pet.createdon = pet_fetched[7]

            print("Pet Updating :)")
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
            pet.pid = int(input("Enter Pet id"))
            pet.cid = customer.cid
            delete_choice = input("Are You Sure to Delete ? (yes/no): ")

            if delete_choice == "yes":
                sql = pet.get_delete_pet__sql_query()
                db.execute_sql(sql)
                print("Pet Deleted...")

        elif choice == 4:
            sql = pet.get_pet_sql_query()
            rows = db.execute_select_sql(sql)
            print(">>PETS<<")
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns))

        elif choice == 5:
            phone = input("Enter Phone:")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)

            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns))
        elif choice ==0:
            break
        else:
            print("Invalid choice")
            break

        print(message)
        choice = int(input("Enter your choice:"))