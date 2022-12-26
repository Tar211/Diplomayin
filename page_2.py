from main import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLineEdit,QDateEdit,QRadioButton,QVBoxLayout,QTimeEdit,QScrollArea,QWidget,QTextEdit,QPushButton,QStackedWidget,QHBoxLayout
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

        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setText("ԲԵՍԹ ԼԱՅՖ ՍԻՐՏ-ԱՆՈԹԱՅԻՆ  ")
        self.label1.move(730,50)
        self.label1.setFont(QFont("Arial latarm", 19))
        self.label1.setStyleSheet("font-weight: bold")
        self.label1.adjustSize()

        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setText("ԲԺՇԿԱԿԱՆ ԿԵՆՏՐՈՆ  ")
        self.label2.move(790, 125)
        self.label2.setFont(QFont("Arial latarm", 19))
        self.label2.setStyleSheet("font-weight: bold")
        self.label2.adjustSize()


        # self.stackedwidget = QStackedWidget()
        # self.stackedwidget.addWidget(Window())
        # self.stackedwidget.addWidget(Window_2())
        #
        # buttonlayout = QHBoxLayout()
        # buttonlayout.addWidget(self.btn2)
        # buttonlayout.addWidget(self.btn1)


        # wi_2 = Window_2()

        self.btn2 = QtWidgets.QPushButton("button 2", self.widget)
        self.btn2.setGeometry(20, 80, 75, 23)
        self.btn2.clicked.connect(self.switchToPage1)



        self.showMaximized()



    def switchToPage1(self):
        self.hide()
        self.window.show()





