from design.main_window.main_menu import *
from design.settings_window.settings_menu import *
from design.reader_window.reader_window import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(900, 600)
        self.resize(1200, int(0.618 * 1200))
        self.set_styles()

        self.currentWindow = None
        # IF YOU WANT TO WORK WITH READER MENU, CHANGE THE LINE BELOW TO
        # self.exec_reader_menu()
        self.exec_main_menu()

    def exec_main_menu(self):
        self.setWindowTitle('LNU Reader')
        self.setWindowIcon(QIcon('design/images/icon.ico'))
        self.currentWindow = WindowInteractivity()
        self.currentWindow.settingsQButton.clicked.connect(self.exec_settings_menu)
        self.setCentralWidget(self.currentWindow)

    def exec_settings_menu(self):
        self.setWindowTitle('Settings')
        self.setWindowIcon(QIcon('design/images/settings.png'))
        self.currentWindow = SettingsWindow()
        self.currentWindow.backQButton.clicked.connect(self.exec_main_menu)
        self.setCentralWidget(self.currentWindow)

    def exec_reader_menu(self):
        self.setWindowTitle('LNU Reader')
        self.setWindowIcon(QIcon('design/images/icon.ico'))
        self.currentWindow = ReaderWindow()
        self.setCentralWidget(self.currentWindow)

    def set_styles(self):
        self.setStyleSheet("""
                background-color: beige;
                color: #5c5c5c;
                font-family: "Century Gothic";
                """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
