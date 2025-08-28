import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel #to set the maingui window  applicvation
from PyQt5.QtGui import QIcon  #only to set icon on the top 
from PyQt5.QtGui import QFont   #only to set the text  or font work
from PyQt5.QtCore import Qt     # it is used to allignment
from PyQt5.QtGui import QPixmap  # it is used to fix the image on the api 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" this is my first application")               
        self.setGeometry(200,200,200,200) # it means x,y,width,height            # these 3 lines are used to set the gui screen

        self.setStyleSheet(                                            # makes more effcent like css and html
                            "background-color:yellow;"                                
                            "font-style:italic;"
                            "font-weight:bold;"
                            "text-decoration:underline;")     

                          

        self.setWindowIcon(QIcon("tillu.jpg"))                              # this line is used to  only for set the pic to icon
       
        label=QLabel("hello",self)
        label.setFont(QFont("arial",30))                                  # these 3 lines are used to  set the font in gui screen
        label.setGeometry(0,0,600,800)
        label.setStyleSheet("color:red;")

        label.setAlignment(Qt.AlignHCenter | Qt.AlignRight )                     # this is work in aligement if VCenter and HCenter also used

        label=QLabel(self)                                                # these lines are used to how th e image is print on the api
        label.setGeometry(0,0,400,400)
        pixmap=QPixmap("tillu.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

def main():
    app=QApplication(sys.argv)
    Window=MainWindow()
    Window.show()
    sys.exit(app.exec_()) #don't forget
if __name__=='__main__':
    main()   

