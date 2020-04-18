import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
import time

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.move(300,300)
        self.setWindowTitle('Hello')
        self.resize(500,500)
        self.show()



app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())