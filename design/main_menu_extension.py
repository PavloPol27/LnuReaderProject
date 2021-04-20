from PyQt5.QtWidgets import QApplication, QShortcut, QFileDialog, QDialog
from main_menu import MainWindow
import sys
import logging

logging.basicConfig(filename = "ReaderLogger.log", level = logging.INFO,
                    format = "time:%(asctime)s, called:%(funcName)s — %(message)s")

class WidnowInteractivity(MainWindow):
    def __init__(self):
        super().__init__()
        self.accaptableFormats = ['.pdf', '.epub', '.fb2']
        self.filesDirectories = []
        self.deleteDialog = QDialog(QDialog)

#------------------------------------------------------
#------------------Open File--------------------------
#------------------------------------------------------
        QShortcut("Ctrl+O", self).activated.connect(self.openFiles)
        self.addBookQButton.clicked.connect(self.openFiles)
        self.removeBookQButton.clicked.connect(self.deleteFile)
        #drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        url = str(event.mimeData().urls()[0])
        if any([format in url for format in self.accaptableFormats]):
            event.accept()
            logging.info(f"file's url = {url} was added")
        else:
            event.ignore()
            logging.info(f"file's url = {url} was declined")

    def dropEvent(self, event):
        urls = [str(url) for url in event.mimeData().urls()]
        urls = [url[url.find("'")+1:url.rfind("'")].replace(r"file:///", '') for url in urls]
        for url in urls:
            if url in self.filesDirectories:
                event.ignore()
                logging.info(f"file's url = {url} was declined")
            else:
                self.filesDirectories.append(url)
                logging.info(f"file's url = {url} was added")


    def openFiles(self):
        directories, _ = QFileDialog.getOpenFileNames(self, filter = 'PDF (*.pdf);; FB2 (*.fb2);; EPUB (*.epub)')
        self.addFile(directories)
            # TODO:
            # add parsing book's metadata;
            # place information into table;
            # insert information into database;

    def addFile(self, directories):
        for directory in directories:
            if directory not in self.filesDirectories:
                self.filesDirectories.append(directory)
                logging.info(f"Directory {directory} was added to list.")
            else:
                logging.info(f"Directory {directory} was ignored.")

#------------------------------------------------------
#------------------Delete File------------------------
#------------------------------------------------------    
    def deleteFile(self):
        if self.table.currentColumn() != 0:
            return
        else:
            print(self.table.currentRow())
            print(self.deleteDialog.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WidnowInteractivity()
    ex.show()
    sys.exit(app.exec_())
