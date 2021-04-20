from PyQt5.QtWidgets import QApplication, QShortcut, QFileDialog
from main_menu import MainWindow
import sys
import logging

logging.basicConfig(filename = "ReaderLogger.log", level = logging.INFO,
                    format = "time:%(asctime)s, called:%(funcName)s — %(message)s")

class WidnowInteractivity(MainWindow):
    def __init__(self):
        super().__init__()
        self.filesDirectories = []

#------------------------------------------------------
#------------------Open File--------------------------
#------------------------------------------------------
        QShortcut("Ctrl+O", self).activated.connect(self.openFile)

        self.addBookQButton.clicked.connect(self.openFile)

    def openFile(self):
        directories, _ = QFileDialog.getOpenFileNames(self, filter = 'PDF (*.pdf);; FB2 (*.fb2);; EPUB (*.epub)')
        for directory in directories:
            if directory not in self.filesDirectories:
                self.filesDirectories.append(directory)
                logging.info(f"Directory {directory} was added to list.")
            else:
                logging.info(f"Directory {directory} was ignored.")
            # TODO:
            # add parsing book's metadata;
            # place information into table;
            # insert information into database;




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WidnowInteractivity()
    ex.show()
    sys.exit(app.exec_())
