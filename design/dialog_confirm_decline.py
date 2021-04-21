from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys



class ConfirmDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        #craete the placeholder for
        self.dialogBackgroundVLayout = QVBoxLayout() #all widgets and layours
        self.buttonHLayout = QHBoxLayout() #buttons
        
        self.changeStyle()

        self.layout_init()
        self.buttons_init()

        self.setLayout(self.dialogBackgroundVLayout)
    
    def changeStyle(self):
        self.setWindowTitle('Deleting file')
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
        '''
            )

    def buttons_init(self):
        #create buttons
        self.acceptButton = QPushButton("Yes!")
        self.declineButton = QPushButton("No")

        #bind them to closing files function
        self.declineButton.clicked.connect(lambda: self.done(0))
        self.acceptButton.clicked.connect(lambda: self.done(1))

        #add buttons to layout
        self.buttonHLayout.addWidget(self.acceptButton)
        self.buttonHLayout.addWidget(self.declineButton)

    def layout_init(self):
        self.warningLable = QLabel("Are you really want to delete file?")
        self.warningLable.setAlignment(Qt.AlignHCenter|Qt.AlignCenter)
        self.dialogBackgroundVLayout.addWidget(self.warningLable)
        self.dialogBackgroundVLayout.addLayout(self.buttonHLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if ConfirmDialog().exec_():
        print("Accepted")
    else:
        print("declined")
    sys.exit(app.exec_())