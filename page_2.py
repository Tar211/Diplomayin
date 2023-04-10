import main
from main import *
from datetime import datetime, time , date
import mysql.connector
from mysql.connector import Error
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow ,QTableWidgetItem,QLineEdit,QDateEdit,QRadioButton,QVBoxLayout,QTimeEdit,QScrollArea,QWidget,QTextEdit,QPushButton,QStackedWidget,QHBoxLayout,QTableWidget,QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore

import sys
from DB_actions import *

class Window_2(QMainWindow):
    def __init__(self,existing_window):
        super(Window_2,self).__init__()
        from DB_actions import DbActions
        from main import Window

        self.db = DbActions()
        self.existing_window = existing_window

        # self.main_min = QMainWindow()
        # self.ui = Window()
        # self.ui.setupUi(self.main_min)

        self.setWindowTitle("Best Life")
        self.setGeometry(0, 0, 1920, 1890)
        self.setWindowIcon(QtGui.QIcon("icon.png"))




        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.widget.resize(1920, 4130)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)






        self.nkar = QtWidgets.QLabel(self.widget)
        self.logo = QPixmap('nkar.png')
        self.nkar.setPixmap(self.logo)
        self.nkar.move(770, 15)
        # self.nkar.setGeometry(770,15, 500, 500)
        self.nkar.adjustSize()


        import DB_actions

        self.nerbernel = QPushButton("Ներբեռնել",self.widget)
        self.nerbernel.setFont(QFont("Arial latarm", 16))
        self.nerbernel.move(300, 200)
        self.nerbernel.resize(300, 50)
        self.nerbernel.clicked.connect(lambda: DbActions.load_data(self))



        self.jnjel = QPushButton("Ջնջել",self.widget)
        self.jnjel.setFont(QFont("Arial latarm", 16))
        self.jnjel.move(1200, 200)
        self.jnjel.resize(300, 50)
        self.jnjel.clicked.connect(lambda :DbActions.delete_data(self))



#################################################################################################################
###### TABLE
#################################################################################################################

        self.table = QTableWidget(self.widget)
        self.table.setFixedWidth(1840)
        self.table.setFixedHeight(2000)
        self.table.move(30, 300)



        self.table.setColumnCount(3)
        self.table.setRowCount(1000)

        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 1200)
        self.table.setColumnWidth(2, 419)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setWeight(QtGui.QFont.Bold)

        self.table.setHorizontalHeaderLabels([" ID ", " Անուն Ազգանուն Հայրանուն  ", " Հեռ․ համար "])
        self.table.horizontalHeaderItem(0).setFont(font)
        self.table.horizontalHeaderItem(1).setFont(font)
        self.table.horizontalHeaderItem(2).setFont(font)
        self.table.horizontalHeaderItem(0).setToolTip(" ID ")
        self.table.horizontalHeaderItem(1).setToolTip(" Անուն Ազգանուն Հայրանուն  ")
        self.table.horizontalHeaderItem(2).setToolTip(" Հեռ․ համար ")

        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)




        self.table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.get_data)








        self.btn2 = QtWidgets.QPushButton("Անկետա", self.widget)
        self.btn2.setGeometry(0, 0, 175, 33)
        self.btn2.setFont(QFont("Arial latarm", 12))
        self.btn2.clicked.connect(self.switchToPage1)





        self.showMaximized()






    def switchToPage1(self):
        self.hide()
        self.window.show()




    def get_data(self):

        connection = mysql.connector.connect(host='localhost', user='root', password='7777', database='data')

        cur = connection.cursor()

        self.index = self.table.selectedItems()


        querys = "SELECT ID, name_surname , phone_number, first_date,srtaban,id_pasport,gender,birth_date, age_pacient, child_num, country, region, city, street, home, building, Apartment, home_Pnumber, job_Place, ux_bujhast,Rb_group2,time_of_reception,SIH_kayun,SIH_ankayun,srt_anbav,srt_infarkt,kard_shok,aritmia,N_axtoroshum,N_axtoroshum_text,Ux_hivandutyunner,nersrtayin_mij_1,nersrtayin_mij_2,nersrtayin_mij_3,nersrtayin_mij_4,nersrtayin_mij_5,nersrtayin_mij_6,Elq FROM pacient_data WHERE ID = %s "
        valuess = (self.index[0].text(),)


        cur.execute(querys,valuess)

        row = cur.fetchone()



        if row:
            self.window.id_pacient.setText(str(row[0]))
            self.window.AAH.setText(row[1])
            self.window.job_Pnumber.setText(str(row[2]))
            self.window.first_date.setDate(QDate.fromString(str(row[3]), 'yyyy-MM-dd'))
            self.window.srtaban.setText(row[4])
            self.window.id_pasport.setText(str(row[5]))

            if row[6] == "Արական":
                self.window.male.setChecked(True)
            elif row[6] == "Իգական":
                self.window.female.setChecked(True)

            self.window.birth_date.setDate(QDate.fromString(str(row[7]), 'yyyy-MM-dd'))
            self.window.age_pacient.setText(str(row[8]))
            self.window.child_num.setText(str(row[9]))
            self.window.country.setText(str(row[10]))
            self.window.region.setText(str(row[11]))
            self.window.city.setText(str(row[12]))
            self.window.street.setText(str(row[13]))
            self.window.home.setText(str(row[14]))
            self.window.building.setText(str(row[15]))
            self.window.Apartment.setText(str(row[16]))
            self.window.home_Pnumber.setText(str(row[17]))
            self.window.job_Place.setText(str(row[18]))
            self.window.ux_bujhast.setText(str(row[19]))

            if row[20] == ".":
                self.window.Ux_bujhastatutyun.setChecked(True)
            elif row[20] == "Դիմել է ինքնուրույն":
                self.window.dimel_e.setChecked(True)
            elif row[20] == "Շտապ ցուցումով":
                self.window.shtap_cucumov.setChecked(True)

            timee = str(row[21])
            time_update = timee.replace(":00", "")
            hour, minute = time_update.split(':')
            if len(hour) == 1:
                hour = '0' + hour
            formatted_time = hour + ':' + minute
            self.window.time_of_reception.setTime(QTime.fromString(formatted_time , "hh:mm"))


            if row[22] == 'Ⅰ':
                self.window.SIH_kayun_1.setChecked(True)
            elif row[22] == 'Ⅱ':
                self.window.SIH_kayun_2.setChecked(True)
            elif row[22] == 'Ⅲ':
                self.window.SIH_kayun_3.setChecked(True)
            elif row[22] == 'Ⅳ':
                self.window.SIH_kayun_4.setChecked(True)

            if row[23] == 'Class Ⅰ':
                self.window.SIH_ankayun_1.setChecked(True)
            elif row[23] == 'Class Ⅱ':
                self.window.SIH_ankayun_2.setChecked(True)
            elif row[23] == 'Class Ⅲ':
                self.window.SIH_ankayun_3.setChecked(True)
            elif row[23] == 'Non-QMI':
                self.window.SIH_ankayun_4.setChecked(True)
            elif row[23] == 'Variant':
                self.window.SIH_ankayun_5.setChecked(True)
            elif row[23] == 'Post MI':
                self.window.SIH_ankayun_6.setChecked(True)


            if row[24] == '0':
                self.window.srt_anbav_1.setChecked(True)
            elif row[24] == 'Ⅱ':
                self.window.srt_anbav_2.setChecked(True)
            elif row[24] == 'Ⅲ':
                self.window.srt_anbav_3.setChecked(True)
            elif row[24] == 'Ⅳ':
                self.window.srt_anbav_4.setChecked(True)


            if row[25] == '< 6Ժ':
                self.window.srt_infarkt_1.setChecked(True)
            elif row[25] == '6-12Ժ':
                self.window.srt_infarkt_2.setChecked(True)
            elif row[25] == '12-24Ժ':
                self.window.srt_infarkt_3.setChecked(True)
            elif row[25] == '> 24Ժ':
                self.window.srt_infarkt_4.setChecked(True)


            if row[26] == 'Ոչ':
                self.window.kard_shok_1.setChecked(True)
            elif row[26] == 'Այո':
                self.window.kard_shok_2.setChecked(True)
            elif row[26] == 'Հեմոդինամիկ անկայուն':
                self.window.kard_shok_3.setChecked(True)
            elif row[26] == 'Ռեֆռակտեր շոկ':
                self.window.kard_shok_4.setChecked(True)


            if row[27] == 'Sust VT/VF':
                self.window.aritmia_1.setChecked(True)
            elif row[27] == 'Heart Block':
                self.window.aritmia_2.setChecked(True)
            elif row[27] == 'AF/Flutter':
                self.window.aritmia_3.setChecked(True)

            self.window.N_axtoroshum.setDate(QDate.fromString(str(row[28]), 'yyyy-MM-dd'))
            self.window.N_axtoroshum_text.setText(str(row[29]))
            self.window.Ux_hivandutyunner.setText(str(row[30]))
            self.window.nersrtayin_mij_1.setText(str(row[31]))
            self.window.nersrtayin_mij_2.setText(str(row[32]))
            self.window.nersrtayin_mij_3.setText(str(row[33]))
            self.window.nersrtayin_mij_4.setText(str(row[34]))
            self.window.nersrtayin_mij_5.setText(str(row[35]))
            self.window.nersrtayin_mij_6.setText(str(row[36]))


            if row[37] == ' Առողջացում':
                self.window.elq_1.setChecked(True)
            elif row[37] == ' Լավացում':
                self.window.elq_2.setChecked(True)
            elif row[37] == ' Անփոփոխ':
                self.window.elq_3.setChecked(True)
            elif row[37] == ' Վատացում':
                self.window.elq_4.setChecked(True)














