from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit, QSpinBox)



from instr import *
from fin_win import *



     
class TestWin(QWidget):
    def __init__(self):
       ''' окно, в котором располагается приветствие '''
       super().__init__()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()


       # создаём и настраиваем графические элементы:
       self.initUI()


       self.i = 0


       #устанавливает связи между элементами
       self.connects()


       # старт:
       self.show()



    def timerEvent(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.i+=1
        self.text_timer.setFont(QFont('Times', 36+self.i, QFont.Bold))
        
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()


    
    def timerEvent2(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.i+=1
        self.text_timer.setFont(QFont('Times', 36+self.i, QFont.Bold))
        
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timerEvent3(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.i+=1
        self.text_timer.setFont(QFont('Times', 36+self.i, QFont.Bold))
        
        if int(self.text_timer.text()[6:8]) >= 45 or int(self.text_timer.text()[6:8]) <=15:
           self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
           self.text_timer.setStyleSheet('color: rgb(0,0,0)')



        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()





    def timer1(self):
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
        
    
    def timer2(self):
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent2)
        self.timer.start(1500)
    
    def timer3(self):
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent3)
        self.timer.start(1000)
        

    def initUI(self):
       ''' создаёт графические элементы '''
       self.text_age = QLabel( txt_age)
       self.text_pol1 = QSpinBox()
       self.but1 = QPushButton('Начать первый тест')

       self.text_age2 = QLabel(txt_starttest1)
       self.text_pol2 = QSpinBox()
       self.but2 = QPushButton(txt_starttest2)

       self.text_age3 = QLabel(txt_test2)
       self.text_pol3 = QSpinBox()
       self.but3 = QPushButton(txt_starttest3)

       self.text_age4 = QLabel(txt_test1)
       self.text_pol4 = QSpinBox()
       

       self.but4 = QPushButton(txt_sendresults)
       
       
       self.text_timer = QLabel(txt_timer)
       
       self.text_timer.setFont(QFont('Times', 30, QFont.Bold))


       self.layoutH = QHBoxLayout()
       self.layoutV1 = QVBoxLayout()
       self.layoutV2 = QVBoxLayout()

       self.layoutV1.addWidget(self.text_age, alignment = Qt.AlignLeft)
       self.layoutV1.addWidget(self.text_pol1, alignment = Qt.AlignLeft)
       
       self.layoutV1.addWidget(self.text_age2, alignment = Qt.AlignLeft)
       self.layoutV1.addWidget(self.but1, alignment = Qt.AlignLeft)
       self.layoutV1.addWidget(self.text_pol2, alignment = Qt.AlignLeft)

       self.layoutV1.addWidget(self.text_age3, alignment = Qt.AlignLeft)
       self.layoutV1.addWidget(self.but2, alignment = Qt.AlignLeft)

       self.layoutV1.addWidget(self.text_age4, alignment = Qt.AlignLeft)
       self.layoutV1.addWidget(self.but3, alignment = Qt.AlignLeft)

       self.layoutV2.addWidget(self.text_timer, alignment = Qt.AlignCenter)

       self.layoutV1.addWidget(self.text_pol3, alignment = Qt.AlignLeft)
       self.layoutV1.addWidget(self.text_pol4, alignment = Qt.AlignLeft)

       self.layoutV1.addWidget(self.but4, alignment = Qt.AlignCenter)



       self.layoutH.addLayout(self.layoutV1)
       self.layoutH.addLayout(self.layoutV2)
       self.setLayout(self.layoutH)


       




    def next_click(self):
       self.tw = Result_win(self.text_pol1.text(), self.text_pol2.text(), self.text_pol3.text(), self.text_pol4.text())
       self.hide()


    def connects(self):
       self.but4.clicked.connect(self.next_click)
       self.but1.clicked.connect(self.timer1)
       self.but2.clicked.connect(self.timer2)
       self.but3.clicked.connect(self.timer3)

   
    def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

