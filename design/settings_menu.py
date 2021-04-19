from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout,\
    QHBoxLayout, QApplication, QInputDialog, QTableWidget, QHeaderView, \
    QTableWidgetItem, QLineEdit, QScrollBar, QAbstractItemView, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QMouseEvent, QKeyEvent
from PyQt5.QtCore import QSize, Qt
import sys
import json
import localize
import styles
import main_menu


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set main window options
        self.setWindowIcon(QIcon('images/settings.png'))

        # Set the size of window
        self.width = 1200
        self.height = int(0.618 * self.width)
        self.resize(self.width, self.height)
        self.setMinimumSize(900, 500)

        # Container
        self.body = QWidget()
        self.bodyQVBoxLayout = QVBoxLayout()
        self.bodyQVBoxLayout.setSpacing(50)

        # Header
        self.header = QWidget()
        self.headerQHBoxLayout = QHBoxLayout()
        self.headerQHBoxLayout.setSpacing(100)

        # Back Button
        self.backQButton = QPushButton()
        self.backQButton.setIcon(QIcon('images/back.png'))
        self.backQButton.setIconSize(QSize(32, 32))
        self.backQButton.setFocusPolicy(Qt.NoFocus)
        self.backQButton.clicked.connect(self.back_button_clicked)

        # Settings Label
        self.settingsLabel = QLabel()
        self.settingsLabel.setFont(QFont("Agency FB", 20))

        # Container
        self.container = QWidget()
        self.containerQVBoxLayout = QVBoxLayout()

        # Language Box
        self.languageBox = QWidget()
        self.languageQHBoxLayout = QHBoxLayout()
        self.languageQHBoxLayout.setSpacing(20)

        # Language Label
        self.languageLabel = QLabel()
        self.languageLabel.setFont(QFont("Agency FB", 12))

        # Language buttons
        self.ENButton = QPushButton()
        self.ENButton.setObjectName('EN')
        self.ENButton.setIcon(QIcon('images/united-kingdom.png'))
        self.ENButton.setIconSize(QSize(32, 32))

        self.UAButton = QPushButton()
        self.UAButton.setObjectName('UA')
        self.UAButton.setIcon(QIcon('images/ukraine.png'))
        self.UAButton.setIconSize(QSize(32, 32))

        self.buttons = [self.ENButton, self.UAButton]
        self.ENButton.clicked.connect(self.category_button_clicked)
        self.UAButton.clicked.connect(self.category_button_clicked)

        localize.set_settings_localization(self)
        styles.Styles.set_settings_styles(self)
        self.init_body()

        # Main window
        self.main_window = None

    def init_header(self):
        self.headerQHBoxLayout.addWidget(self.backQButton)
        self.headerQHBoxLayout.addWidget(self.settingsLabel)
        self.headerQHBoxLayout.addStretch()
        self.header.setLayout(self.headerQHBoxLayout)

    def init_language_box(self):
        self.languageQHBoxLayout.addWidget(self.languageLabel)

        self.languageQHBoxLayout.addWidget(self.ENButton)
        self.languageQHBoxLayout.addWidget(self.UAButton)
        self.languageQHBoxLayout.addStretch()
        self.languageBox.setLayout(self.languageQHBoxLayout)

    def init_container(self):
        self.init_language_box()
        self.containerQVBoxLayout.addWidget(self.languageBox)
        self.container.setLayout(self.containerQVBoxLayout)

    def init_body(self):
        self.init_header()
        self.init_container()
        self.bodyQVBoxLayout.addWidget(self.header)
        self.bodyQVBoxLayout.addWidget(self.container)
        self.bodyQVBoxLayout.addStretch()
        self.body.setLayout(self.bodyQVBoxLayout)
        self.setCentralWidget(self.body)

    def category_button_clicked(self):
        button = self.sender()
        for lg_button in self.buttons:
            if lg_button == button:
                button.setIconSize(QSize(56, 56))
                button.setFocus()
                lg_info = {'language': button.objectName()}
                with open('language.json', 'w') as outfile:
                    json.dump(lg_info, outfile)
                localize.set_settings_localization(self)
            else:
                lg_button.setIconSize(QSize(32, 32))

    def back_button_clicked(self):
        if self.main_window is None:
            self.main_window = main_menu.MainWindow()
        self.main_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsWindow()
    ex.show()
    sys.exit(app.exec_())
