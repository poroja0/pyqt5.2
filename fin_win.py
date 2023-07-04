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
      
       self.initUI(age,p1,p2,p3)


      


       # старт:
       self.show()

   
   
   
   
   
   def results(self, age,p1,p2,p3):

      age = int(age)
      self.index = (4*(int(p1)+int(p2)+int(p3))-200)/10
      if age >=7:
           
            if age <=8:
                if self.index >=6.4:
                    
                    if self.index <=11.9:
                        return txt_res4
                    elif self.index <=16.9:
                        return txt_res3
                    elif self.index <=20.9:
                        return txt_res2
                    else:
                        return txt_res1

                
                else:
                    self.setStyleSheet("background-color: ")
                    return txt_res5

            elif age <=10:

                if self.index >=4.9:
                    
                    if self.index <=10.4:
                        return txt_res4
                    elif self.index <=15.4:
                        return txt_res3
                    elif self.index <=19.4:
                        return txt_res2
                    else:
                        return txt_res1

                
                else:
                    return txt_res5

            elif age <=12:

                if self.index >=3.4:
                    
                    if self.index <=8.9:
                        return txt_res4
                    elif self.index <=13.9:
                        return txt_res3
                    elif self.index <=17.9:
                        return txt_res2
                    else:
                        return txt_res1

                
                else:
                    return txt_res5

            elif age <=14:

                if self.index >=1.9:
                    
                    if self.index <=7.4:
                        return txt_res4
                    elif self.index <=12.4:
                        return txt_res3
                    elif self.index <=16.4:
                        return txt_res2
                    else:
                        return txt_res1

                
                else:
                    return txt_res5

            else:

                if self.index >=0.4:
                    
                    if self.index <=5.9:
                        return txt_res4
                    elif self.index <=10.9:
                        return txt_res3
                    elif self.index <=14.9:
                        return txt_res2
                    else:
                        return txt_res1

                
                else:
                    return txt_res5



                
            
      else:
          return 'вы не подходите под параметры'



   def initUI(self, age,p1,p2,p3):
       ''' создаёт графические элементы '''
       
      
       self.text2 = QLabel(txt_workheart + self.results(age,p1,p2,p3)) 
       self.text1 = QLabel(txt_index + str(self.index))
       

       
       self.layoutV = QVBoxLayout()

       self.layoutV.addWidget(self.text1, alignment = Qt.AlignCenter)
       self.layoutV.addWidget(self.text2, alignment = Qt.AlignCenter)
       
     
       
       self.setLayout(self.layoutV)

  


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

