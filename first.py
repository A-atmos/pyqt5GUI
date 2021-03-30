from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():  #function after clicking the b1
    print('Clicked')

def window():
    app = QApplication(sys.argv) #os application window
    win = QMainWindow()
    win.setGeometry(100, 70, 500 ,500)
    win.setWindowTitle('Just a try!')

    label = QtWidgets.QLabel(win)
    label.setText('Label')
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText('Button1')
    b1.move(65,65)
    b1.clicked.connect(clicked) #clicked to call the above function

    win.show()
    sys.exit(app.exec_())

window()