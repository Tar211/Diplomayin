from main import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow ,QTableWidgetItem,QLineEdit,QDateEdit,QRadioButton,QVBoxLayout,QTimeEdit,QScrollArea,QWidget,QTextEdit,QPushButton,QStackedWidget,QHBoxLayout,QTableWidget,QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window_2(QMainWindow):
    def __init__(self):
        super(Window_2,self).__init__()


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


#################################################################################################################
###### TABLE
#################################################################################################################

        self.table = QTableWidget(self.widget)
        self.table.setFixedWidth(1840)
        self.table.move(30, 300)






        self.table.setColumnCount(3)
        self.table.setRowCount(1)

        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 1200)
        self.table.setColumnWidth(2, 419)

        self.table.setHorizontalHeaderLabels([" ID ", " Անուն Ազգանուն Հայրանուն  ", " Հեռ․ համար "])
        self.table.horizontalHeaderItem(0).setToolTip(" ID ")
        self.table.horizontalHeaderItem(1).setToolTip(" Անուն Ազգանուն Հայրանուն  ")
        self.table.horizontalHeaderItem(2).setToolTip(" Հեռ․ համար ")

        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)





        self.table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        self.table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))



        # self.header = self.table.horizontalHeader()
        # self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # self.table.resizeColumnsToContents()

        # self.layout = QVBoxLayout(self.widget)
        # self.layout.addWidget(self.table)
        # self.setLayout(self.layout)

        # grid_layout.addWidget(self.table, 100, 100)



        self.btn2 = QtWidgets.QPushButton("Անկետա", self.widget)
        self.btn2.setGeometry(0, 0, 175, 33)
        self.btn2.setFont(QFont("Arial latarm", 12))
        self.btn2.clicked.connect(self.switchToPage1)



        self.showMaximized()



    def switchToPage1(self):
        self.hide()
        self.window.show()





