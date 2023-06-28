from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit, QSpinBox)


from instr import *




     
class Result_win(QWidget):
   def __init__(self, age,p1,p2,p3):
       ''' окно, в котором располагается приветствие '''
       super().__init__()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()


       # создаём и настраиваем графические элементы:
       self.results(age,p1,p2,p3)
       self.initUI()


      


       # старт:
       self.show()

   def results(self, age,p1,p2,p3):
      self.index = (4*(int(age)+ int(p1)+int(p2)+int(p3))-200)/10



   def initUI(self):
       ''' создаёт графические элементы '''
       self.text1 = QLabel(txt_index + str(self.index))
      
       self.text2 = QLabel(txt_workheart)
       

       
       self.layoutV = QVBoxLayout()

       self.layoutV.addWidget(self.text1, alignment = Qt.AlignCenter)
       self.layoutV.addWidget(self.text2, alignment = Qt.AlignCenter)
       
     
       
       self.setLayout(self.layoutV)

  


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

