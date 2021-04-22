from PyQt5.QtWidgets import QMessageBox

class ErrorMessage(QMessageBox):
    def __init__(self, text='', info=''):
        super().__init__()

        self.setIcon(QMessageBox.Critical)
        self.setText(text)
        self.setInformativeText(info)
        self.setWindowTitle("Error")
        self.exec_()
