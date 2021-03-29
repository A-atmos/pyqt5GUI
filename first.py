from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv) #os application window
    win = QMainWindow()
    win.setGeometry(100, 70, 500 ,500)
    win.setWindowTitle('Just a try!')

    win.show()
    sys.exit(app.exec_())

window()