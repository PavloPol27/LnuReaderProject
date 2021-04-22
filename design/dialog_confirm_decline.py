from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys



class ConfirmDialog(QDialog):
    def __init__(self):
        super().__init__()

        # create the placeholder for
        # all widgets and layouts
        self.dialogBackgroundVLayout = QVBoxLayout()
        # buttons
        self.buttonHLayout = QHBoxLayout()
        # label with warning text
        self.warningLabel = QLabel("Do you want to delete file?")
        # create buttons
        self.acceptButton = QPushButton("Yes!")
        self.declineButton = QPushButton("No")

        self.change_style()
        self.layout_init()
        self.buttons_init()

        self.setLayout(self.dialogBackgroundVLayout)

    def change_style(self):
        self.setWindowTitle('Deleting')
        self.setWindowIcon(QIcon('images/removeBook.ico'))
        self.setFixedSize(300, 100)
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
                font-size: 17px;
                }
                
        """
        ''')

    def buttons_init(self):
        # bind them to closing files function
        self.declineButton.clicked.connect(lambda: self.done(0))
        self.acceptButton.clicked.connect(lambda: self.done(1))

        # add buttons to layout
        self.buttonHLayout.addWidget(self.acceptButton)
        self.buttonHLayout.addWidget(self.declineButton)

    def layout_init(self):
        self.warningLabel.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.dialogBackgroundVLayout.addWidget(self.warningLabel)
        self.dialogBackgroundVLayout.addLayout(self.buttonHLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if ConfirmDialog().exec_():
        print("Accepted")
    else:
        print("declined")
    sys.exit(app.exec_())
