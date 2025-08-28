import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ghuergouergiuerhghergurgr")
        self.setStyleSheet("background-color:pink;")
        label=QLabel("hellogffggf",self)
        label.setStyleSheet("background-color:red;")
def main():
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":   
    main()