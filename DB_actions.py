import mysql.connector
from mysql.connector import Error
from main import Window
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from page_2 import *


class DbActions():
    def __init__(self):
        pass
        # super(DbActions, self).__init__()
        # self.setupUI()

        # self.mutqagrel.clicked.connect(self.add_data())


    def add_data(self):
        connection = mysql.connector.connect(host='localhost', database='data', user='root', password='7777')


        ID = self.id_pacient.text()
        name_surname = self.AAH.text()
        phone_number = self.job_Pnumber.text()
        first_date = self.first_date.text()
        srtaban = self.srtaban.text()
        id_pasport = self.id_pasport.text()
        Rb_group1 = self.RB_group_1.checkedButton().text()
        birth_date =self.birth_date.text()
        age_pacient = self.age_pacient.text()
        child_num = self.child_num.text()
        country = self.country.text()
        region = self.region.text()
        city = self.city.text()
        street = self.street.text()
        home = self.home.text()
        building = self.building.text()
        apartment = self.Apartment.text()
        home_Pnumber = self.home_Pnumber.text()
        job_place = self.job_Place.text()
        ux_bujhast = self.ux_bujhast.text()
        Rb_group2 =  self.RB_group_2.checkedButton().text()

        cur = connection.cursor()
        insertq = "INSERT INTO pacient_data (ID, name_surname , phone_number, first_date, srtaban, id_pasport, gender, birth_date, age_pacient, child_num, country, region, city, street, home, building, Apartment, home_Pnumber, job_Place, ux_bujhast, Rb_group2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (ID , name_surname,phone_number,first_date,srtaban,id_pasport, Rb_group1,birth_date,age_pacient, child_num,country,region,city,street,home,building,apartment,home_Pnumber,job_place,ux_bujhast,Rb_group2 )




        cur.execute(insertq, values)
        connection.commit()


        cur.close()
        connection.close()




    def load_data(self):

        connection = mysql.connector.connect(host='localhost', user='root', password='7777', database='data')

        query = "SELECT ID , name_surname , phone_number FROM pacient_data"

        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()


        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

        cur.close()
        connection.close()


    def delete_data(self):

        connection = mysql.connector.connect(host='localhost', user='root', password='7777', database='data')
        cur = connection.cursor()

        self.item = self.table.selectedItems()
        deleteq = "DELETE FROM pacient_data WHERE ID = %s"
        valuesq = (self.item[0].text(),)

        cur.execute(deleteq, valuesq)
        # self.table.clear()

        # Close the cursor and connection
        cur.close()
        connection.close()





# def connect():
#     pass
    # try:
    #
    #     conn = mysql.connector.connect(host = 'localhost', database = "data" ,  user ='root', password = '7777')
    #     if conn.is_connected():
    #         print("connected to mysql database")
    # except Error as e:
    #     print(e)
    #
    # finally:
    #     conn.close()
    #
    # print(conn)
    #


