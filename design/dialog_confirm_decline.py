from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
import sys


class ConfirmDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Deleting File')
        self.setWindowIcon(QIcon('images/removeBook.png'))
        self.setFixedSize(400, 200)
        self.setStyleSheet('''
        QDialog {
                color: #5c5c5c;
                background-color: beige;
                }
                QDialog QPushButton:hover
                {
                border: 2px dashed #5c5c5c;
                border-radius: 15px;
                }

                QDialog QPushButton:pressed 
                {
                border-style: solid;
                }

                QDialog QPushButton
                {
                border: 0;
                font-size: 15px;
                width: 90px;
                height: 35px;
                }
                QDialog QLabel
                {
                font-size: 25px;
                }
                
        """
        '''
            )
        self.dialogBackgroundVLayout = QVBoxLayout()
        self.buttonHLayout = QHBoxLayout()
        self.warningLable = QLabel("Are you really want to delete file?")
        
        self.acceptButton = QPushButton("Yes!")
        self.declineButton = QPushButton("No")


        self.dialogBackgroundVLayout.addWidget(self.warningLable)
        self.buttonHLayout.addWidget(self.acceptButton)
        self.buttonHLayout.addWidget(self.declineButton)

        self.declineButton.clicked.connect(lambda: self.done(0))
        self.acceptButton.clicked.connect(lambda: self.done(1))

        self.dialogBackgroundVLayout.addLayout(self.buttonHLayout)
        self.setLayout(self.dialogBackgroundVLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if ConfirmDialog().exec_():
        print("Accepted")
    else:
        print("declined")
    sys.exit(app.exec_())