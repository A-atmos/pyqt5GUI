from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 70, 500 ,500)
        self.setWindowTitle('Just a try!')

        self.initUI()


    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Label')
        # self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Button1')
        self.b1.move(65,65)
        self.b1.clicked.connect(self.clicked) #clicked to call the above function

    def clicked(self):
        self.label.setText('You pressed the button')
        self.update()
    
    def update(self):
        self.label.adjustSize()

def clicked():  #function after clicking the b1
    print('Clicked')

def window():
    app = QApplication(sys.argv) #os application window
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()