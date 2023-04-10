import mysql.connector
from mysql.connector import Error
from main import Window
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from page_2 import *


class DbActions():
    def __init__(self):
        pass



    def add_data(self):
        connection = mysql.connector.connect(host='localhost', database='data', user='root', password='7777')
        print("skizb")

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
        time_of_reception = self.time_of_reception.text()
        Rb_group3 = self.RB_group_3.checkedButton().text()
        Rb_group4 = self.RB_group_4.checkedButton().text()
        Rb_group5 = self.RB_group_5.checkedButton().text()
        Rb_group6 = self.RB_group_6.checkedButton().text()
        Rb_group7 = self.RB_group_7.checkedButton().text()
        Rb_group8 = self.RB_group_8.checkedButton().text()
        N_axtoroshum = self.N_axtoroshum.text()
        print("stage1")
        N_axtoroshum_text = self.N_axtoroshum_text.toPlainText()
        print("stage1.5")
        Ux_hivandutyunner = self.Ux_hivandutyunner.toPlainText()
        print("stage2")
        nersrtayin_mij_1 = self.nersrtayin_mij_1.text()
        nersrtayin_mij_2 = self.nersrtayin_mij_2.text()
        nersrtayin_mij_3 = self.nersrtayin_mij_3.text()
        nersrtayin_mij_4 = self.nersrtayin_mij_4.text()
        nersrtayin_mij_5 = self.nersrtayin_mij_5.text()
        nersrtayin_mij_6 = self.nersrtayin_mij_6.text()
        Rb_group9 = self.RB_group_9.checkedButton().text()
        print("begin")
        cur = connection.cursor()
        insertq = "INSERT INTO pacient_data (ID, name_surname , phone_number, first_date, srtaban, id_pasport, gender, birth_date, age_pacient, child_num, country, region, city, street, home, building, Apartment, home_Pnumber, job_Place, ux_bujhast, Rb_group2,time_of_reception,SIH_kayun,SIH_ankayun,srt_anbav,srt_infarkt,kard_shok,aritmia,N_axtoroshum,N_axtoroshum_text,Ux_hivandutyunner,nersrtayin_mij_1,nersrtayin_mij_2,nersrtayin_mij_3,nersrtayin_mij_4,nersrtayin_mij_5,nersrtayin_mij_6,Elq) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (ID , name_surname,phone_number,first_date,srtaban,id_pasport,Rb_group1,birth_date,age_pacient, child_num,country,region,city,street,home,building,apartment,home_Pnumber,job_place,ux_bujhast,Rb_group2,time_of_reception,Rb_group3,Rb_group4,Rb_group5,Rb_group6,Rb_group7,Rb_group8,N_axtoroshum,N_axtoroshum_text,Ux_hivandutyunner,nersrtayin_mij_1,nersrtayin_mij_2,nersrtayin_mij_3,nersrtayin_mij_4,nersrtayin_mij_5,nersrtayin_mij_6,Rb_group9)

        print("imsert")


        cur.execute(insertq, values)
        connection.commit()

        print("succesfully added")

        cur.close()
        connection.close()




    def load_data(self):

        connection = mysql.connector.connect(host='localhost', user='root', password='7777', database='data')

        query = "SELECT ID , name_surname , phone_number FROM pacient_data"

        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setWeight(2)

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                item.setFont(font)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                # item.setTextAlignment(Qt.AlignJustify | Qt.AlignVCenter)
                self.table.setItem(row_number,column_number,item)

        cur.close()
        connection.close()


    def delete_data(self):
        selected = self.table.selectedItems()
        if selected:
            rows = set(item.row() for item in selected)
            for row in sorted(rows, reverse=True):
                ID = self.table.item(row, 0).text()
                connection = mysql.connector.connect(host='localhost', user='root', password='7777', database='data')
                cur = connection.cursor()
                sql_delete_query = """DELETE FROM pacient_data WHERE ID = %s"""
                cur.execute(sql_delete_query, (ID,))
                connection.commit()
                cur.close()
                connection.close()
                self.table.removeRow(row)





