from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLineEdit,QDateEdit,QRadioButton,QVBoxLayout,QTimeEdit,QScrollArea,QWidget,QTextEdit,QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *


import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setWindowTitle("Best Life")
        self.setGeometry(0,0,1920,1890)

        self.setWindowIcon(QtGui.QIcon("icon.png"))


        #Scroll bar
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.widget.resize(1920, 4130)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)




        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setText("ԲԵՍԹ ԼԱՅՖ ՍԻՐՏ-ԱՆՈԹԱՅԻՆ  ")
        self.label1.move(30,50)
        self.label1.setFont(QFont("Arial latarm", 19))
        self.label1.setStyleSheet("font-weight: bold")
        self.label1.adjustSize()

        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setText("ԲԺՇԿԱԿԱՆ ԿԵՆՏՐՈՆ  ")
        self.label2.move(90, 125)
        self.label2.setFont(QFont("Arial latarm", 19))
        self.label2.setStyleSheet("font-weight: bold")
        self.label2.adjustSize()


        self.nkar = QtWidgets.QLabel(self.widget)
        self.logo=QPixmap('nkar.png')
        self.nkar.setPixmap(self.logo)
        self.nkar.move(770,15)
        # self.nkar.setGeometry(770,15, 500, 500)
        self.nkar.adjustSize()
        # self.nkar.resize(self.logo.width(),self.logo.height())


        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setText("ՀԻՎԱՆԴԻ ԱՆՁՆԱԿԱՆ ՔԱՐՏ ")
        self.label3.move(1250, 50)
        self.label3.setFont(QFont("Arial latarm", 20))
        self.label3.setStyleSheet("font-weight: bold")
        self.label3.adjustSize()



        self.label4 = QtWidgets.QLabel(self.widget)
        self.label4.setText("№ ")
        self.label4.move(1350, 150)
        self.label4.setFont(QFont("Arial latarm", 20))
        self.label4.setStyleSheet("font-weight: bold")
        self.label4.adjustSize()

        self.id_pacient = QLineEdit(self.widget)
        self.id_pacient.move(1420, 155)
        self.id_pacient.resize(200, 32)
        self.id_pacient.setValidator(QIntValidator())
        self.id_pacient.setMaxLength(10)
        self.id_pacient.setFont(QFont("Arial", 20))



        self.label5 = QtWidgets.QLabel(self.widget)
        self.label5.setText("Անկետային տվյալներ՝  ")
        self.label5.move(80, 325)
        # self.label5.setStyleSheet("font-weight: bold")
        self.label5.setStyleSheet("QLabel{font-size: 18pt;}")
        self.underline = QFont()
        self.underline.setUnderline(True)
        self.label5.setFont(self.underline)
        self.label5.adjustSize()



        self.label6 = QtWidgets.QLabel(self.widget)
        self.label6.setText("Առաջին այցի ամսաթիվ՝ ")
        self.label6.move(80, 425)
        self.label6.setFont(QFont("Arial latarm", 15))
        self.label6.adjustSize()

        self.first_date = QDateEdit(self.widget)
        self.first_date.setGeometry(410, 425, 200, 37)
        self.first_date.setFont(QFont("Arial latarm", 14))
        self.d = QDate(2020, 6, 10)
        self.first_date.setDate(self.d)



        self.label7 = QtWidgets.QLabel(self.widget)
        self.label7.setText("Սրտաբան՝ ")
        self.label7.move(780, 425)
        self.label7.setFont(QFont("Arial latarm", 15))
        self.label7.adjustSize()

        self.srtaban = QLineEdit(self.widget)
        self.srtaban.move(930, 425)
        self.srtaban.resize(200, 32)
        self.srtaban.setFont(QFont("Arial latarm", 15))



        self.label8 = QtWidgets.QLabel(self.widget)
        self.label8.setText("Անձնագիր №՝ ")
        self.label8.move(1290, 425)
        self.label8.setFont(QFont("Arial latarm", 15))
        self.label8.adjustSize()

        self.id_pasport = QLineEdit(self.widget)
        self.id_pasport.move(1480, 425)
        self.id_pasport.resize(200, 32)
        self.id_pasport.setFont(QFont("Arial", 20))



        self.label9 = QtWidgets.QLabel(self.widget)
        self.label9.setText("Հիվանդի Ա․Ա․Հ՝ ")
        self.label9.move(80, 545)
        self.label9.setFont(QFont("Arial latarm", 15))
        self.label9.adjustSize()

        self.AAH = QLineEdit(self.widget)
        self.AAH.move(320, 545)
        self.AAH.resize(810, 32)
        self.AAH.setFont(QFont("Arial latarm", 15))



        self.label10 = QtWidgets.QLabel(self.widget)
        self.label10.setText("Ծննդյան ամսաթիվ՝ ")
        self.label10.move(80, 645)
        self.label10.setFont(QFont("Arial latarm", 15))
        self.label10.adjustSize()

        self.birth_date = QDateEdit(self.widget)
        self.birth_date.setGeometry(370, 640, 200, 37)
        self.birth_date.setFont(QFont("Arial latarm", 14))
        self.d = QDate(2020, 6, 10)
        self.birth_date.setDate(self.d)




        self.label11 = QtWidgets.QLabel(self.widget)
        self.label11.setText("Տարիք՝ ")
        self.label11.move(700, 645)
        self.label11.setFont(QFont("Arial latarm", 15))
        self.label11.adjustSize()

        self.age_pacient = QLineEdit(self.widget)
        self.age_pacient.move(810, 645)
        self.age_pacient.resize(70, 32)
        self.age_pacient.setValidator(QIntValidator())
        self.age_pacient.setMaxLength(3)
        self.age_pacient.setFont(QFont("Arial", 20))

        self.label12 = QtWidgets.QLabel(self.widget)
        self.label12.setText("Սեռ՝ ")
        self.label12.move(1190, 545)
        self.label12.setFont(QFont("Arial latarm", 15))
        self.label12.adjustSize()



        #radio buttons
        #https://www.pythontutorial.net/pyqt/pyqt-qradiobutton/
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.male = QRadioButton('Արական', self.widget)
        self.male.toggled.connect(self.update)
        self.male.move(1280, 545)
        self.male.setFont(QFont("Arial latarm", 15))
        self.male.adjustSize()

        self.female = QRadioButton('Իգական', self.widget)
        self.female.toggled.connect(self.update)
        self.female.move(1440, 545)
        self.female.setFont(QFont("Arial latarm", 15))
        self.female.adjustSize()

        self.layout.addWidget(self.male)
        self.layout.addWidget(self.female)

        self.RB_group_1 =QtWidgets.QButtonGroup()
        self.RB_group_1.addButton(self.male)
        self.RB_group_1.addButton(self.female)
        # self.RB_group_1.buttonClicked.connect(print("RB 1 is clicked"))
        #    https://www.youtube.com/watch?v=s2VWoo4sAng&ab_channel=TrevorPayne

        # def update(self):
        #     # get the radio button the send the signal
        #     rb = self.sender()
        #
        #     # check if the radio button is checked
        #     if rb.isChecked():
        #         self.result_label.setText(f'You selected {rb.text()}')




        self.label13 = QtWidgets.QLabel(self.widget)
        self.label13.setText("Երեխաների քանակը՝ ")
        self.label13.move(990, 645)
        self.label13.setFont(QFont("Arial latarm", 15))
        self.label13.adjustSize()

        self.child_num = QLineEdit(self.widget)
        self.child_num.move(1270, 645)
        self.child_num.resize(70, 32)
        self.child_num.setValidator(QIntValidator())
        self.child_num.setMaxLength(2)
        self.child_num.setFont(QFont("Arial", 20))



        self.label14 = QtWidgets.QLabel(self.widget)
        self.label14.setText("Երկիր՝ ")
        self.label14.move(80, 745)
        self.label14.setFont(QFont("Arial latarm", 15))
        self.label14.adjustSize()

        self.country = QLineEdit(self.widget)
        self.country.move(190, 745)
        self.country.resize(200, 32)
        self.country.setFont(QFont("Arial latarm", 15))




        self.label15 = QtWidgets.QLabel(self.widget)
        self.label15.setText("Մարզ՝ ")
        self.label15.move(480, 745)
        self.label15.setFont(QFont("Arial latarm", 15))
        self.label15.adjustSize()

        self.region = QLineEdit(self.widget)
        self.region.move(590, 745)
        self.region.resize(200, 32)
        self.region.setFont(QFont("Arial latarm", 15))




        self.label16 = QtWidgets.QLabel(self.widget)
        self.label16.setText("Քաղաք / Գյուղ՝ ")
        self.label16.move(880, 745)
        self.label16.setFont(QFont("Arial latarm", 15))
        self.label16.adjustSize()

        self.city = QLineEdit(self.widget)
        self.city.move(1090, 745)
        self.city.resize(300, 32)
        self.city.setFont(QFont("Arial latarm", 15))



        self.label17 = QtWidgets.QLabel(self.widget)
        self.label17.setText("Փողոց՝ ")
        self.label17.move(1440, 745)
        self.label17.setFont(QFont("Arial latarm", 15))
        self.label17.adjustSize()

        self.street = QLineEdit(self.widget)
        self.street.move(1540, 745)
        self.street.resize(300, 32)
        self.street.setFont(QFont("Arial latarm", 15))



        self.label18 = QtWidgets.QLabel(self.widget)
        self.label18.setText("Տուն՝ ")
        self.label18.move(80, 845)
        self.label18.setFont(QFont("Arial latarm", 15))
        self.label18.adjustSize()

        self.home = QLineEdit(self.widget)
        self.home.move(190, 845)
        self.home.resize(100, 32)
        self.home.setFont(QFont("Arial latarm", 15))



        self.label19 = QtWidgets.QLabel(self.widget)
        self.label19.setText("Շենք՝ ")
        self.label19.move(390, 845)
        self.label19.setFont(QFont("Arial latarm", 15))
        self.label19.adjustSize()

        self.building = QLineEdit(self.widget)
        self.building.move(490, 845)
        self.building.resize(100, 32)
        self.building.setValidator(QIntValidator())
        self.building.setMaxLength(5)
        self.building.setFont(QFont("Arial latarm", 15))



        self.label20 = QtWidgets.QLabel(self.widget)
        self.label20.setText("Բնակարան՝ ")
        self.label20.move(690, 845)
        self.label20.setFont(QFont("Arial latarm", 15))
        self.label20.adjustSize()

        self.Apartment = QLineEdit(self.widget)
        self.Apartment.move(890, 845)
        self.Apartment.resize(100, 32)
        self.Apartment.setValidator(QIntValidator())
        self.Apartment.setMaxLength(5)
        self.Apartment.setFont(QFont("Arial latarm", 15))



        self.label21 = QtWidgets.QLabel(self.widget)
        self.label21.setText("Տան հեռ․ № ՝ ")
        self.label21.move(1110, 845)
        self.label21.setFont(QFont("Arial latarm", 15))
        self.label21.adjustSize()

        self.home_Pnumber = QLineEdit(self.widget)
        self.home_Pnumber.move(1310, 845)
        self.home_Pnumber.resize(300, 32)
        self.home_Pnumber.setValidator(QIntValidator())
        self.home_Pnumber.setMaxLength(9)
        self.home_Pnumber.setFont(QFont("Arial latarm", 15))





        self.label22 = QtWidgets.QLabel(self.widget)
        self.label22.setText("Աշխատանքի վայր՝ ")
        self.label22.move(80, 945)
        self.label22.setFont(QFont("Arial latarm", 15))
        self.label22.adjustSize()


        self.job_Place = QLineEdit(self.widget)
        self.job_Place.move(360, 945)
        self.job_Place.resize(700, 32)
        self.job_Place.setFont(QFont("Arial latarm", 15))





        self.label23 = QtWidgets.QLabel(self.widget)
        self.label23.setText("Հեռ․ № ՝ ")
        self.label23.move(1140, 945)
        self.label23.setFont(QFont("Arial latarm", 15))
        self.label23.adjustSize()

        self.job_Pnumber = QLineEdit(self.widget)
        self.job_Pnumber.move(1270, 945)
        self.job_Pnumber.resize(300, 32)
        self.job_Pnumber.setValidator(QIntValidator())
        self.job_Pnumber.setMaxLength(9)
        self.job_Pnumber.setFont(QFont("Arial latarm", 15))





        self.label24 = QtWidgets.QLabel(self.widget)
        self.label24.setText("Ուղեգրող բուժ․ հաստատություն՝ ")
        self.label24.move(80, 1045)
        self.label24.setFont(QFont("Arial latarm", 15))
        self.label24.adjustSize()



        self.layout2 = QVBoxLayout()
        self.setLayout(self.layout2)

        self.Ux_bujhastatutyun = QRadioButton('', self.widget)
        self.Ux_bujhastatutyun.toggled.connect(self.update_ubh)
        self.Ux_bujhastatutyun.move(500, 1050)
        self.Ux_bujhastatutyun.setFont(QFont("Arial latarm", 15))
        self.Ux_bujhastatutyun.adjustSize()

        self.ux_bujhast = QLineEdit(self.widget)
        self.ux_bujhast.move(560, 1045)
        self.ux_bujhast.resize(300, 32)
        self.ux_bujhast.setFont(QFont("Arial latarm", 15))

        self.dimel_e = QRadioButton('Դիմել է ինքնուրույն', self.widget)
        self.dimel_e.toggled.connect(self.update_ubh)
        self.dimel_e.move(950, 1045)
        self.dimel_e.setFont(QFont("Arial latarm", 15))
        self.dimel_e.adjustSize()

        self.shtap_cucumov = QRadioButton('Շտապ ցուցումով', self.widget)
        self.shtap_cucumov.toggled.connect(self.update_ubh)
        self.shtap_cucumov.move(1300, 1045)
        self.shtap_cucumov.setFont(QFont("Arial latarm", 15))
        self.shtap_cucumov.adjustSize()

        self.layout2.addWidget(self.ux_bujhast)
        self.layout2.addWidget(self.dimel_e)
        self.layout2.addWidget(self.shtap_cucumov)


        self.RB_group_2 = QtWidgets.QButtonGroup()
        self.RB_group_2.addButton(self.Ux_bujhastatutyun)
        self.RB_group_2.addButton(self.dimel_e)
        self.RB_group_2.addButton(self.shtap_cucumov)

        # self.RB_group_2.buttonClicked.connect(print("RB 1 is clicked"))





        self.label25 = QtWidgets.QLabel(self.widget)
        self.label25.setText("Ընդունման ժամ՝ ")
        self.label25.move(80, 1145)
        self.label25.setFont(QFont("Arial latarm", 15))
        self.label25.adjustSize()

        self.timeedit = QTimeEdit(self.widget)
        self.timeedit.setGeometry(320, 1145, 130, 40)
        self.timeedit.setFont(QFont("Arial latarm", 15))
        self.timeedit.setTime(QTime.currentTime())
        self.timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        self.timeedit.setDisplayFormat('hh:mm')





        self.label25 = QtWidgets.QLabel(self.widget)
        self.label25.setText("ՍԻՀ, կայուն ստենոկարդիա՝ ")
        self.label25.move(80, 1290)
        self.label25.setFont(QFont("Arial latarm", 15))
        self.label25.adjustSize()

        self.layout3 = QVBoxLayout()
        self.setLayout(self.layout3)

        self.SIH_kayun_1 = QRadioButton('Ⅰ', self.widget)
        self.SIH_kayun_1.toggled.connect(self.update_ubh)
        self.SIH_kayun_1.move(550, 1290)
        self.SIH_kayun_1.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_kayun_1.setFont(QFont("Arial latarm", 21))
        self.SIH_kayun_1.adjustSize()

        self.SIH_kayun_2 = QRadioButton('Ⅱ', self.widget)
        self.SIH_kayun_2.toggled.connect(self.update_ubh)
        self.SIH_kayun_2.move(750, 1290)
        self.SIH_kayun_2.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_kayun_2.setFont(QFont("Arial latarm", 21))
        self.SIH_kayun_2.adjustSize()

        self.SIH_kayun_3 = QRadioButton('Ⅲ', self.widget)
        self.SIH_kayun_3.toggled.connect(self.update_ubh)
        self.SIH_kayun_3.move(950, 1290)
        self.SIH_kayun_3.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_kayun_3.setFont(QFont("Arial latarm", 21))
        self.SIH_kayun_3.adjustSize()

        self.SIH_kayun_4 = QRadioButton('Ⅳ', self.widget)
        self.SIH_kayun_4.toggled.connect(self.update_ubh)
        self.SIH_kayun_4.move(1150, 1290)
        self.SIH_kayun_4.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_kayun_4.setFont(QFont("Arial latarm", 21))
        self.SIH_kayun_4.adjustSize()

        self.layout3.addWidget(self.SIH_kayun_1)
        self.layout3.addWidget(self.SIH_kayun_2)
        self.layout3.addWidget(self.SIH_kayun_3)
        self.layout3.addWidget(self.SIH_kayun_4)

        self.RB_group_3 = QtWidgets.QButtonGroup()
        self.RB_group_3.addButton(self.SIH_kayun_1)
        self.RB_group_3.addButton(self.SIH_kayun_2)
        self.RB_group_3.addButton(self.SIH_kayun_3)
        self.RB_group_3.addButton(self.SIH_kayun_4)











        self.label26 = QtWidgets.QLabel(self.widget)
        self.label26.setText("ՍԻՀ, անկայուն ստենոկարդիա՝ ")
        self.label26.move(80, 1440)
        self.label26.setFont(QFont("Arial latarm", 15))
        self.label26.adjustSize()

        self.layout4 = QVBoxLayout()
        self.setLayout(self.layout4)

        self.SIH_ankayun_1 = QRadioButton('Class Ⅰ', self.widget)
        self.SIH_ankayun_1.toggled.connect(self.update_ubh)
        self.SIH_ankayun_1.move(550, 1440)
        self.SIH_ankayun_1.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_ankayun_1.setFont(QFont("Arial latarm", 17))
        self.SIH_ankayun_1.adjustSize()

        self.SIH_ankayun_2 = QRadioButton('Class Ⅱ', self.widget)
        self.SIH_ankayun_2.toggled.connect(self.update_ubh)
        self.SIH_ankayun_2.move(750, 1440)
        self.SIH_ankayun_2.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_ankayun_2.setFont(QFont("Arial latarm", 17))
        self.SIH_ankayun_2.adjustSize()

        self.SIH_ankayun_3 = QRadioButton('Class Ⅲ', self.widget)
        self.SIH_ankayun_3.toggled.connect(self.update_ubh)
        self.SIH_ankayun_3.move(950, 1440)
        self.SIH_ankayun_3.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_ankayun_3.setFont(QFont("Arial latarm", 17))
        self.SIH_ankayun_3.adjustSize()

        self.SIH_ankayun_4 = QRadioButton('Non-QMI', self.widget)
        self.SIH_ankayun_4.toggled.connect(self.update_ubh)
        self.SIH_ankayun_4.move(1150, 1440)
        self.SIH_ankayun_4.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_ankayun_4.setFont(QFont("Arial latarm", 17))
        self.SIH_ankayun_4.adjustSize()

        self.SIH_ankayun_5 = QRadioButton('Variant', self.widget)
        self.SIH_ankayun_5.toggled.connect(self.update_ubh)
        self.SIH_ankayun_5.move(1350, 1440)
        self.SIH_ankayun_5.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_ankayun_5.setFont(QFont("Arial latarm", 17))
        self.SIH_ankayun_5.adjustSize()

        self.SIH_ankayun_6 = QRadioButton('Post MI', self.widget)
        self.SIH_ankayun_6.toggled.connect(self.update_ubh)
        self.SIH_ankayun_6.move(1550, 1440)
        self.SIH_ankayun_6.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.SIH_ankayun_6.setFont(QFont("Arial latarm", 17))
        self.SIH_ankayun_6.adjustSize()

        self.layout4.addWidget(self.SIH_ankayun_1)
        self.layout4.addWidget(self.SIH_ankayun_2)
        self.layout4.addWidget(self.SIH_ankayun_3)
        self.layout4.addWidget(self.SIH_ankayun_4)
        self.layout4.addWidget(self.SIH_ankayun_5)
        self.layout4.addWidget(self.SIH_ankayun_6)

        self.RB_group_4 = QtWidgets.QButtonGroup()
        self.RB_group_4.addButton(self.SIH_ankayun_1)
        self.RB_group_4.addButton(self.SIH_ankayun_2)
        self.RB_group_4.addButton(self.SIH_ankayun_3)
        self.RB_group_4.addButton(self.SIH_ankayun_4)
        self.RB_group_4.addButton(self.SIH_ankayun_5)
        self.RB_group_4.addButton(self.SIH_ankayun_6)









        self.label27 = QtWidgets.QLabel(self.widget)
        self.label27.setText("Սրտային անբավարարություն՝ ")
        self.label27.move(80, 1590)
        self.label27.setFont(QFont("Arial latarm", 15))
        self.label27.adjustSize()

        self.layout5 = QVBoxLayout()
        self.setLayout(self.layout5)

        self.srt_anbav_1 = QRadioButton('0', self.widget)
        self.srt_anbav_1.toggled.connect(self.update_ubh)
        self.srt_anbav_1.move(550, 1590)
        self.srt_anbav_1.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_anbav_1.setFont(QFont("Arial latarm", 21))
        self.srt_anbav_1.adjustSize()

        self.srt_anbav_2 = QRadioButton('Ⅱ', self.widget)
        self.srt_anbav_2.toggled.connect(self.update_ubh)
        self.srt_anbav_2.move(750, 1590)
        self.srt_anbav_2.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_anbav_2.setFont(QFont("Arial latarm", 21))
        self.srt_anbav_2.adjustSize()

        self.srt_anbav_3 = QRadioButton('Ⅲ', self.widget)
        self.srt_anbav_3.toggled.connect(self.update_ubh)
        self.srt_anbav_3.move(950, 1590)
        self.srt_anbav_3.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_anbav_3.setFont(QFont("Arial latarm", 21))
        self.srt_anbav_3.adjustSize()

        self.srt_anbav_4 = QRadioButton('Ⅳ', self.widget)
        self.srt_anbav_4.toggled.connect(self.update_ubh)
        self.srt_anbav_4.move(1150, 1590)
        self.srt_anbav_4.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_anbav_4.setFont(QFont("Arial latarm", 21))
        self.srt_anbav_4.adjustSize()

        self.layout5.addWidget(self.srt_anbav_1)
        self.layout5.addWidget(self.srt_anbav_2)
        self.layout5.addWidget(self.srt_anbav_3)
        self.layout5.addWidget(self.srt_anbav_4)

        self.RB_group_5 = QtWidgets.QButtonGroup()
        self.RB_group_5.addButton(self.srt_anbav_1)
        self.RB_group_5.addButton(self.srt_anbav_2)
        self.RB_group_5.addButton(self.srt_anbav_3)
        self.RB_group_5.addButton(self.srt_anbav_4)












        self.label28 = QtWidgets.QLabel(self.widget)
        self.label28.setText("Սրտամկանի ինֆարկտ՝ ")
        self.label28.move(80, 1740)
        self.label28.setFont(QFont("Arial latarm", 15))
        self.label28.adjustSize()

        self.layout6 = QVBoxLayout()
        self.setLayout(self.layout6)

        self.srt_infarkt_1 = QRadioButton('< 6Ժ', self.widget)
        self.srt_infarkt_1.toggled.connect(self.update_ubh)
        self.srt_infarkt_1.move(550, 1740)
        self.srt_infarkt_1.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_infarkt_1.setFont(QFont("Arial latarm", 19))
        self.srt_infarkt_1.adjustSize()

        self.srt_infarkt_2 = QRadioButton('6-12Ժ', self.widget)
        self.srt_infarkt_2.toggled.connect(self.update_ubh)
        self.srt_infarkt_2.move(750, 1740)
        self.srt_infarkt_2.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_infarkt_2.setFont(QFont("Arial latarm", 19))
        self.srt_infarkt_2.adjustSize()

        self.srt_infarkt_3 = QRadioButton('12-24Ժ', self.widget)
        self.srt_infarkt_3.toggled.connect(self.update_ubh)
        self.srt_infarkt_3.move(950, 1740)
        self.srt_infarkt_3.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_infarkt_3.setFont(QFont("Arial latarm", 19))
        self.srt_infarkt_3.adjustSize()

        self.srt_infarkt_4 = QRadioButton('> 24Ժ', self.widget)
        self.srt_infarkt_4.toggled.connect(self.update_ubh)
        self.srt_infarkt_4.move(1150, 1740)
        self.srt_infarkt_4.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.srt_infarkt_4.setFont(QFont("Arial latarm", 19))
        self.srt_infarkt_4.adjustSize()

        self.layout6.addWidget(self.srt_infarkt_1)
        self.layout6.addWidget(self.srt_infarkt_2)
        self.layout6.addWidget(self.srt_infarkt_3)
        self.layout6.addWidget(self.srt_infarkt_4)

        self.RB_group_6 = QtWidgets.QButtonGroup()
        self.RB_group_6.addButton(self.srt_infarkt_1)
        self.RB_group_6.addButton(self.srt_infarkt_2)
        self.RB_group_6.addButton(self.srt_infarkt_3)
        self.RB_group_6.addButton(self.srt_infarkt_4)

        ###











        self.label29 = QtWidgets.QLabel(self.widget)
        self.label29.setText("Կարդիոգեն շոկ՝ ")
        self.label29.move(80, 1890)
        self.label29.setFont(QFont("Arial latarm", 15))
        self.label29.adjustSize()

        self.layout7 = QVBoxLayout()
        self.setLayout(self.layout7)

        self.kard_shok_1 = QRadioButton('Ոչ', self.widget)
        self.kard_shok_1.toggled.connect(self.update_ubh)
        self.kard_shok_1.move(550, 1890)
        self.kard_shok_1.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.kard_shok_1.setFont(QFont("Arial latarm", 19))
        self.kard_shok_1.adjustSize()

        self.kard_shok_2 = QRadioButton('Այո', self.widget)
        self.kard_shok_2.toggled.connect(self.update_ubh)
        self.kard_shok_2.move(750, 1890)
        self.kard_shok_2.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.kard_shok_2.setFont(QFont("Arial latarm", 19))
        self.kard_shok_2.adjustSize()

        self.kard_shok_3 = QRadioButton('Հեմոդինամիկ անկայուն', self.widget)
        self.kard_shok_3.toggled.connect(self.update_ubh)
        self.kard_shok_3.move(950, 1890)
        self.kard_shok_3.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.kard_shok_3.setFont(QFont("Arial latarm", 19))
        self.kard_shok_3.adjustSize()

        self.kard_shok_4 = QRadioButton('Ռեֆռակտեր շոկ', self.widget)
        self.kard_shok_4.toggled.connect(self.update_ubh)
        self.kard_shok_4.move(1450, 1890)
        self.kard_shok_4.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.kard_shok_4.setFont(QFont("Arial latarm", 19))
        self.kard_shok_4.adjustSize()

        self.layout7.addWidget(self.kard_shok_1)
        self.layout7.addWidget(self.kard_shok_2)
        self.layout7.addWidget(self.kard_shok_3)
        self.layout7.addWidget(self.kard_shok_4)

        self.RB_group_7 = QtWidgets.QButtonGroup()
        self.RB_group_7.addButton(self.kard_shok_1)
        self.RB_group_7.addButton(self.kard_shok_2)
        self.RB_group_7.addButton(self.kard_shok_3)
        self.RB_group_7.addButton(self.kard_shok_4)













        self.label30 = QtWidgets.QLabel(self.widget)
        self.label30.setText("Առիթմիա՝ ")
        self.label30.move(80, 2040)
        self.label30.setFont(QFont("Arial latarm", 15))
        self.label30.adjustSize()

        self.layout8 = QVBoxLayout()
        self.setLayout(self.layout8)

        self.aritmia_1 = QRadioButton('Sust VT/VF', self.widget)
        self.aritmia_1.toggled.connect(self.update_ubh)
        self.aritmia_1.move(550, 2040)
        self.aritmia_1.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.aritmia_1.setFont(QFont("Arial latarm", 19))
        self.aritmia_1.adjustSize()

        self.aritmia_2 = QRadioButton('Heart Block', self.widget)
        self.aritmia_2.toggled.connect(self.update_ubh)
        self.aritmia_2.move(950, 2040)
        self.aritmia_2.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.aritmia_2.setFont(QFont("Arial latarm", 19))
        self.aritmia_2.adjustSize()

        self.aritmia_3 = QRadioButton('AF/Flutter', self.widget)
        self.aritmia_3.toggled.connect(self.update_ubh)
        self.aritmia_3.move(1350, 2040)
        self.aritmia_3.setStyleSheet("QRadioButton::indicator{width : 20px;height : 20px;}")
        self.aritmia_3.setFont(QFont("Arial latarm", 19))
        self.aritmia_3.adjustSize()

        self.layout8.addWidget(self.aritmia_1)
        self.layout8.addWidget(self.aritmia_2)
        self.layout8.addWidget(self.aritmia_3)

        self.RB_group_8 = QtWidgets.QButtonGroup()
        self.RB_group_8.addButton(self.aritmia_1)
        self.RB_group_8.addButton(self.aritmia_2)
        self.RB_group_8.addButton(self.aritmia_3)






















        self.label31 = QtWidgets.QLabel(self.widget)
        self.label31.setText("Նախնական ախտորոշում՝ ")
        self.label31.move(80, 2240)
        self.label31.setFont(QFont("Arial latarm", 16))
        self.label31.setStyleSheet("font-weight: bold")
        self.label31.adjustSize()

        self.N_axtoroshum = QDateEdit(self.widget)
        self.N_axtoroshum.setGeometry(520, 2240, 200, 37)
        self.N_axtoroshum.setFont(QFont("Arial latarm", 14))
        self.d = QDate(2020, 6, 10)
        self.N_axtoroshum.setDate(self.d)


        self.N_axtoroshum_text = QTextEdit(self.widget)
        self.N_axtoroshum_text.setGeometry(80, 2340, 1690, 307)
        self.N_axtoroshum_text.setFont(QFont("Arial latarm", 14))















        self.label32 = QtWidgets.QLabel(self.widget)
        self.label32.setText("Ուղեկցող հիվանդություններ՝ ")
        self.label32.move(80, 2760)
        self.label32.setFont(QFont("Arial latarm", 16))
        self.label32.setStyleSheet("font-weight: bold")
        self.label32.adjustSize()

        self.Ux_hivandutyunner = QTextEdit(self.widget)
        self.Ux_hivandutyunner.setGeometry(80, 2860, 1690, 197)
        self.Ux_hivandutyunner.setFont(QFont("Arial latarm", 14))

















        self.label33 = QtWidgets.QLabel(self.widget)
        self.label33.setText("Նախկինում կատարած ներսրտային միջամտություն / վիրահատություն՝ ")
        self.label33.move(80, 3220)
        self.label33.setFont(QFont("Arial latarm", 16))
        self.label33.setStyleSheet("font-weight: bold")
        self.label33.adjustSize()



        self.label34 = QtWidgets.QLabel(self.widget)
        self.label34.setText("1. ")
        self.label34.move(80, 3350)
        self.label34.setFont(QFont("Arial latarm", 16))
        self.label34.setStyleSheet("font-weight: bold")
        self.label34.adjustSize()

        self.nersrtayin_mij_1 = QLineEdit(self.widget)
        self.nersrtayin_mij_1.move(140, 3350)
        self.nersrtayin_mij_1.resize(1500, 32)
        self.nersrtayin_mij_1.setFont(QFont("Arial latarm", 15))



        self.label35 = QtWidgets.QLabel(self.widget)
        self.label35.setText("2. ")
        self.label35.move(80, 3450)
        self.label35.setFont(QFont("Arial latarm", 16))
        self.label35.setStyleSheet("font-weight: bold")
        self.label35.adjustSize()

        self.nersrtayin_mij_2 = QLineEdit(self.widget)
        self.nersrtayin_mij_2.move(140, 3450)
        self.nersrtayin_mij_2.resize(1500, 32)
        self.nersrtayin_mij_2.setFont(QFont("Arial latarm", 15))



        self.label36 = QtWidgets.QLabel(self.widget)
        self.label36.setText("3. ")
        self.label36.move(80, 3550)
        self.label36.setFont(QFont("Arial latarm", 16))
        self.label36.setStyleSheet("font-weight: bold")
        self.label36.adjustSize()

        self.nersrtayin_mij_3 = QLineEdit(self.widget)
        self.nersrtayin_mij_3.move(140, 3550)
        self.nersrtayin_mij_3.resize(1500, 32)
        self.nersrtayin_mij_3.setFont(QFont("Arial latarm", 15))



        self.label37 = QtWidgets.QLabel(self.widget)
        self.label37.setText("4. ")
        self.label37.move(80, 3650)
        self.label37.setFont(QFont("Arial latarm", 16))
        self.label37.setStyleSheet("font-weight: bold")
        self.label37.adjustSize()

        self.nersrtayin_mij_4 = QLineEdit(self.widget)
        self.nersrtayin_mij_4.move(140, 3650)
        self.nersrtayin_mij_4.resize(1500, 32)
        self.nersrtayin_mij_4.setFont(QFont("Arial latarm", 15))




        self.label38 = QtWidgets.QLabel(self.widget)
        self.label38.setText("5. ")
        self.label38.move(80, 3750)
        self.label38.setFont(QFont("Arial latarm", 16))
        self.label38.setStyleSheet("font-weight: bold")
        self.label38.adjustSize()

        self.nersrtayin_mij_5 = QLineEdit(self.widget)
        self.nersrtayin_mij_5.move(140, 3750)
        self.nersrtayin_mij_5.resize(1500, 32)
        self.nersrtayin_mij_5.setFont(QFont("Arial latarm", 15))




        self.label39 = QtWidgets.QLabel(self.widget)
        self.label39.setText("6. ")
        self.label39.move(80, 3850)
        self.label39.setFont(QFont("Arial latarm", 16))
        self.label39.setStyleSheet("font-weight: bold")
        self.label39.adjustSize()

        self.nersrtayin_mij_6 = QLineEdit(self.widget)
        self.nersrtayin_mij_6.move(140, 3850)
        self.nersrtayin_mij_6.resize(1500, 32)
        self.nersrtayin_mij_6.setFont(QFont("Arial latarm", 15))












        self.label40 = QtWidgets.QLabel(self.widget)
        self.label40.setText("Ելք՝ ")
        self.label40.move(80, 4020)
        self.label40.setFont(QFont("Arial latarm", 16))
        self.label40.setStyleSheet("font-weight: bold")
        self.label40.adjustSize()



        self.layout9 = QVBoxLayout()
        self.setLayout(self.layout9)

        self.elq_1 = QRadioButton(' Առողջացում', self.widget)
        self.elq_1.toggled.connect(self.update_ubh)
        self.elq_1.move(320, 4020)
        self.elq_1.setFont(QFont("Arial latarm", 17))
        self.elq_1.adjustSize()

        self.elq_2 = QRadioButton(' Լավացում', self.widget)
        self.elq_2.toggled.connect(self.update_ubh)
        self.elq_2.move(620, 4020)
        self.elq_2.setFont(QFont("Arial latarm", 17))
        self.elq_2.adjustSize()

        self.elq_3 = QRadioButton(' Անփոփոխ', self.widget)
        self.elq_3.toggled.connect(self.update_ubh)
        self.elq_3.move(920, 4020)
        self.elq_3.setFont(QFont("Arial latarm", 17))
        self.elq_3.adjustSize()

        self.elq_4 = QRadioButton(' Վատացում', self.widget)
        self.elq_4.toggled.connect(self.update_ubh)
        self.elq_4.move(1220, 4020)
        self.elq_4.setFont(QFont("Arial latarm", 17))
        self.elq_4.adjustSize()

        self.layout9.addWidget(self.elq_1)
        self.layout9.addWidget(self.elq_2)
        self.layout9.addWidget(self.elq_3)
        self.layout9.addWidget(self.elq_4)

        self.RB_group_9 = QtWidgets.QButtonGroup()
        self.RB_group_9.addButton(self.elq_1)
        self.RB_group_9.addButton(self.elq_2)
        self.RB_group_9.addButton(self.elq_3)
        self.RB_group_9.addButton(self.elq_4)






        self.mutqagrel = QPushButton("Մուտքագրել",self.widget)
        self.mutqagrel.setFont(QFont("Arial latarm", 16))
        self.mutqagrel.move(1520, 4020)
        self.mutqagrel.resize(300, 50)

        self.mutqagrel.clicked.connect(self.mutq)



        self.showMaximized()



    # def mutq(self):
    #     pass

    def update_ubh(self):
        rn = self.sender()

        if rn.isChecked():
            print("2 is checked")

    def update(self):
        # get the radio button the send the signal
        rb = self.sender()

        # check if the radio button is checked
        if rb.isChecked():
            print("1 is checked")
















def application():
    app=QApplication(sys.argv)
    window = Window()


    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()
