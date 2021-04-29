from PyQt5.QtWidgets import QMessageBox

import design.main_window.styles


class WarningMessage(QMessageBox):
    def __init__(self, text='', info=''):
        super().__init__()

        self.setIcon(QMessageBox.Warning)
        self.setText(text)
        self.setInformativeText(info)
        self.setWindowTitle("Warning")
        Styles.set_message_style(self)
        self.exec_()
