from PyQt5.QtWidgets import QApplication
from main_menu import MainWindow
import sys
import logging

class WidnowInteractivity(MainWindow):
    def __init__(self):
        super().__init__()
        self.files = {}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WidnowInteractivity()
    ex.show()
    sys.exit(app.exec_())
