
import datetime

"""
    create table Consultation (
        cnid int primary key auto_increment,
        cid int,
        pid int,
        problem text,
        heartrate int,
        temperature float,
        medicines text,
        createdon datetime
        );
"""
class Consultation:

    def __init__(self):
        self.cnid = 0
        self.cid = 0
        self.pid = 0
        self.problem = ""
        self.heartrate = 0
        self.temperature = 98.4
        self.medicines = 0
        self.createdon = ""

    def read_consultation_data(self):
        self.problem = input("Enter Problem:")
        self.heartrate = input("Enter Heartrate:")
        self.temperature = float(input("Enter Temperature:"))
        self.medicines = input("Enter Medicines:")
        # get the date and time
        self.createdon = str(datetime.datetime.today())
        # eliminate milli seconds
        self.createdon = self.createdon[:self.createdon.rindex(".")]

    def get_insert_consultation_sql_query(self):
        sql = "insert into Consultation values(null, {cid}, {pid}, '{problem}', '{heartrate}', {temperature}, '{medicines}', " \
              "'{createdon}')".format_map(vars(self))
        return sql

    def get_consultation_sql_query(self, cid="", pid=""):
        sql = "select * from Consultation"
        if len(cid) != 0:
            sql = "select * from Consultation where cid = {}".format(cid)
        if len(pid) != 0:
            sql = "select * from Consultation where pid = {}".format(pid)
        return sql

    def get_delete_sql_query(self):
        sql = "delete from Consultation where cnid = {}".format(self.cnid)
        return sql
