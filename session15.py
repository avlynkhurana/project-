"""
Pet : pid, name, age, weight, breed, gender, cid, createdon
    create table Pet(
        pid int primary key auto_increment,
        name text,
        age int,
        weight int,
        breed text,
        gender text,
        cid int,
        createdon datetime,
        FOREIGN KEY (cid) REFERENCES Customer(cid)
        );
"""
import datetime


class Pet:

    def _init_(self):
        self.pid = 0
        self.name = ""
        self.age = 0
        self.weight = 0
        self.breed = ""
        self.gender = ""
        self.cid = 0
        self.createdon = ""

    def read_pet_data(self):
        self.name = input("Enter Pet name:")
        self.age = input("Enter Pet age:")
        self.weight = input("Enter pet weight:")
        self.breed = input("Enter pet breed:")
        self.gender = input("Enter pet gender (male/female):").lower()

        self.createdon = str(datetime.datetime.today())

        self.createdon = self.createdon[:self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into Pet values(null, '{name}', {age}, {weight}, '{breed}', '{gender}', '{cid}', " \
              "'{createdon}')".format_map(vars(self))

        return sql

    def get_pet_sql_query(self, cid=""):
        if len(cid) == 0:

            sql = "select * from Pet"
        else:
            sql = "select * from Pet where cid = {}".format(cid)
        return sql

    def get_delete_pet__sql_query(self):
        sql = "delete from Customer where cid = {}".format(self.cid)

        return sql

    def get_pet_update_sql_query(self):
        sql = "update pet set name='{}', age={}, weight={}, breed='{}', gender='{}' where cid={}".format_map((self))
        return sql
 # "update pet set name='{}', age={}, weight={}, breed='{}', gender='{}' where cid={}".format_map((self))
