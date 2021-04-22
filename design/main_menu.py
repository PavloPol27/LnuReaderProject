from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout,\
    QHBoxLayout, QApplication, QInputDialog, QTableWidget, QHeaderView, \
    QTableWidgetItem, QLineEdit, QScrollBar, QAbstractItemView, QMessageBox,\
    QShortcut, QFileDialog, QMenu
from PyQt5.QtGui import QFont, QIcon, QMouseEvent, QKeyEvent
from PyQt5.QtCore import QSize, Qt
from dialog_confirm_decline import ConfirmDialog
from messages import ErrorMessage, WarningMessage
import sys
import localize
import styles
import settings_menu
import logging
from functools import partial
logging.basicConfig(filename='ReaderLogger.log',
                    level=logging.INFO,
                    format='Called from:%(funcName)s, %(message)s, time: %(asctime)s')
  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # needed variable
        self.buttonCalledAction = None

        # Set main window options
        self.setWindowTitle('LNU Reader')
        self.setWindowIcon(QIcon('images/icon.ico'))

        # Set the size of window
        self.width = 1200
        self.height = int(0.618 * self.width)
        self.resize(self.width, self.height)
        self.setMinimumSize(900, 500)

        # Main body
        self.bodyQVBoxLayout = QVBoxLayout()
        self.body = QWidget()

        # -----------------
        # Header
        self.headerQHBoxLayout = QHBoxLayout()
        self.header = QWidget()
        self.headerQHBoxLayout.setSpacing(20)
        self.headerQHBoxLayout.setContentsMargins(20, 11, 20, 11)

        # Add Book Button
        self.addBookQButton = QPushButton()
        self.addBookQButton.setIcon(QIcon('images/add.png'))
        self.addBookQButton.setIconSize(QSize(28, 28))
        self.addBookQButton.setFocusPolicy(Qt.NoFocus)

        # Remove Book Button
        self.removeBookQButton = QPushButton()
        self.removeBookQButton.setIcon(QIcon('images/removeBook.png'))
        self.removeBookQButton.setIconSize(QSize(28, 28))
        self.removeBookQButton.setFocusPolicy(Qt.NoFocus)

        # Search Bar
        self.searchBar = QLineEdit()
        self.searchBar.setClearButtonEnabled(True)
        self.searchBar.setFocusPolicy(Qt.ClickFocus)

        # Settings
        self.settingsQButton = QPushButton()
        self.settingsQButton.setIcon(QIcon('images/settings.png'))
        self.settingsQButton.setIconSize(QSize(32, 32))
        self.settingsQButton.setFocusPolicy(Qt.NoFocus)
        self.settingsQButton.clicked.connect(self.settings_button_clicked)
        # -----------------
        # Container
        self.containerQHBoxLayout = QHBoxLayout()
        self.container = QWidget()
        self.containerQHBoxLayout.setContentsMargins(20, 20, 20, 40)
        self.containerQHBoxLayout.setSpacing(0)

        # Side Bar
        self.sideBar = QWidget()
        self.sideBarQVBoxLayout = QVBoxLayout()
        self.sideBarQVBoxLayout.setContentsMargins(0, 10, 0, 0)

        # Library Label
        self.libLabel = QLabel()
        self.libLabel.setAlignment(Qt.AlignCenter)

        # Context menu
        self.context_menu = QMenu()
        self.open_act = self.context_menu.addAction("")
        self.edit_act = self.context_menu.addAction("")
        self.delete_act = self.context_menu.addAction("")

        # Categories
        self.categoriesQWidget = QWidget()
        self.categoriesQVBoxLayout = QVBoxLayout()
        self.categoriesQVBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.categoriesQVBoxLayout.setSpacing(0)

        # Categories buttons
        self.categories = []
        self.allQButton = QPushButton()
        self.favouritesQButton = QPushButton()
        self.category_button_options(self.allQButton)
        self.category_button_options(self.favouritesQButton)

        # Create Category Button
        self.createCategoryQButton = QPushButton()
        self.createCategoryQButton.clicked.connect(self.show_dialog)
        self.createCategoryQButton.setFocusPolicy(Qt.NoFocus)

        # Create Category Dialog
        self.categoryQDialog = QInputDialog()
        self.categoryQDialog.setInputMode(QInputDialog.TextInput)
        self.categoryQDialog.setWindowIcon(QIcon('images/icon.ico'))
        self.categoryQDialog.resize(600, 400)

        # Content
        self.content = QWidget()
        self.contentQVBoxLayout = QVBoxLayout()
        self.contentQVBoxLayout.setContentsMargins(0, 0, 0, 0)

        # Category title in Content
        self.categoryQLabel = QLabel()
        self.categoryQLabel.setAlignment(Qt.AlignCenter)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(6)

        # ScrollBar in Table
        self.tableScrollBar = QScrollBar()
        self.table.setVerticalScrollBar(self.tableScrollBar)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Main run
        localize.set_main_menu_localization(self)
        styles.Styles.set_main_menu_styles(self)
        self.init_body()

        # Settings window
        self.sett_menu = None

    def init_header(self):
        self.headerQHBoxLayout.addWidget(self.addBookQButton)
        self.headerQHBoxLayout.addWidget(self.removeBookQButton)
        self.headerQHBoxLayout.addStretch()
        self.headerQHBoxLayout.addWidget(self.searchBar)
        self.headerQHBoxLayout.addWidget(self.settingsQButton)
        self.header.setLayout(self.headerQHBoxLayout)

    def init_categories(self):
        for ctg in self.categories:
            ctg.setFocusPolicy(Qt.ClickFocus)
            self.categoriesQVBoxLayout.addWidget(ctg)
        self.categoriesQWidget.setLayout(self.categoriesQVBoxLayout)

    def init_sidebar(self):
        self.init_categories()
        self.sideBarQVBoxLayout.addWidget(self.libLabel)
        self.sideBarQVBoxLayout.addWidget(self.categoriesQWidget)
        self.sideBarQVBoxLayout.addStretch()
        self.sideBarQVBoxLayout.addWidget(self.createCategoryQButton)

        self.sideBar.setLayout(self.sideBarQVBoxLayout)

    def init_table(self):
        header = self.table.horizontalHeader()
        self.table.verticalHeader().setVisible(False)
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.resizeSection(2, 120)
        header.resizeSection(3, 100)
        header.resizeSection(4, 80)
        header.resizeSection(5, 50)

        for i in range(30):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(f'text{i}'))

    def init_content(self):
        self.init_table()
        self.contentQVBoxLayout.addWidget(self.categoryQLabel)
        self.contentQVBoxLayout.addWidget(self.table)
        self.content.setLayout(self.contentQVBoxLayout)

    def init_container(self):
        self.init_sidebar()
        self.init_content()
        self.containerQHBoxLayout.addWidget(self.sideBar)
        self.containerQHBoxLayout.addWidget(self.content)
        self.container.setLayout(self.containerQHBoxLayout)

    def init_body(self):
        self.init_header()
        self.init_container()
        self.bodyQVBoxLayout.addWidget(self.header)
        self.bodyQVBoxLayout.addWidget(self.container)
        self.body.setLayout(self.bodyQVBoxLayout)
        self.setCentralWidget(self.body)

    def show_dialog(self):
        ok = self.categoryQDialog.exec_()
        text = self.categoryQDialog.textValue()
        if ok:
            if text.isspace() or not text:
                ErrorMessage("Empty input", 'You wrote empty category title. Please try again')
            else:
                self.category_button_options(QPushButton(text))
                self.init_categories()

    def category_button_options(self, category_button):
        styles.Styles.set_category_button_styles(category_button)
        category_button.setFocusPolicy(Qt.NoFocus)
        category_button.setContextMenuPolicy(Qt.CustomContextMenu)
        category_button.customContextMenuRequested.connect(self.on_context_menu)
        self.categories.append(category_button)

        category_button.clicked.connect(self.category_button_clicked)

    def category_button_clicked(self):
        button = self.sender()
        for ctg in self.categories:
            styles.Styles.set_category_button_styles(ctg)
        styles.Styles.set_clicked_category_button_styles(button)
        self.categoryQLabel.setText(button.text())

    def on_context_menu(self, point):
        self.buttonCalledAction = self.sender()
        self.context_menu.exec_(self.buttonCalledAction.mapToGlobal(point))

    def settings_button_clicked(self):
        if self.sett_menu is None:
            self.sett_menu = settings_menu.SettingsWindow()
        self.sett_menu.show()
        self.close()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()


class WindowInteractivity(MainWindow):
    def __init__(self):
        super().__init__()
        self.acceptableFormats = ['.pdf', '.epub', '.fb2']
        self.filesDirectories = []
        self.deleteDialog = ConfirmDialog()

# ------------------------------------------------------
# ------------------Open File--------------------------
# ------------------------------------------------------
        QShortcut("Ctrl+O", self).activated.connect(self.open_files)
        QShortcut("Del", self).activated.connect(self.delete_files)
        QShortcut("Ctrl+A", self).activated.connect(lambda: self.table.selectAll())

        self.addBookQButton.clicked.connect(self.open_files)
        self.removeBookQButton.clicked.connect(self.delete_files)

        self.open_act.triggered.connect(self.open_category)
        self.edit_act.triggered.connect(self.rename_category)
        self.delete_act.triggered.connect(self.delete_category)
        # drag and drop
        self.setAcceptDrops(True)
        self.table.clicked.connect(lambda index: self.table.selectRow(index.row()))


    def select_col(self, index):
        self.table.selectRow(index.row())

    def dragEnterEvent(self, event):
        url = str(event.mimeData().urls()[0])
        if any([form in url for form in self.acceptableFormats]):
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

    def open_files(self):
        directories, _ = QFileDialog.getOpenFileNames(self, filter='PDF (*.pdf);; FB2 (*.fb2);; EPUB (*.epub)')
        self.add_file(directories)
        # TODO:
        # add parsing book's metadata;
        # place information into table;
        # insert information into database;

    def add_file(self, directories):
        for directory in directories:
            if directory not in self.filesDirectories:
                self.filesDirectories.append(directory)
                logging.info(f"Directory {directory} was added to list.")
            else:
                logging.info(f"Directory {directory} was ignored.")

# ------------------------------------------------------
# ------------------Delete File------------------------
# ------------------------------------------------------
    def delete_files(self):
        if self.deleteDialog.exec_():
            for index in self.table.selectedItems():
                self.delete_file(index.row(), index.column())
        
    def delete_file(self, r, c):
        if c != 0:
            logging.info(f"Deleting from table is declined for item row = {r}, column = {c}")
            return
        self.table.removeRow(r)
        logging.info(f"Deleted item in table with row = {r}, column = {c}")

    def rename_category(self):
        previous_title = self.buttonCalledAction.text()
        if previous_title in ['All', 'Favourites']:
            WarningMessage("Can not rename this category", "This is basic category")
            logging.info("Can not change this category title")
            return

        self.categoryQDialog.setWindowTitle('Rename')
        ok = self.categoryQDialog.exec_()
        text = self.categoryQDialog.textValue()
        if ok:
            self.buttonCalledAction.setText(text)
            logging.info(f"Renamed category {previous_title} to {text}")
        else:
            logging.info(f"Renaming category {previous_title} was declined")
        self.categoryQDialog.setWindowTitle('Create new category')

    def delete_category(self):
        previous_title = self.buttonCalledAction.text()
        if previous_title in ['All', 'Favourites']:
            ErrorMessage('Can not delete this category!', 'This category is a basic one.')
            logging.info("Can not delete this category")
            return

        self.deleteDialog.warningLabel.setText('Do you want to delete category?')
        ok = self.deleteDialog.exec_()
        if ok:
            self.categories.remove(self.buttonCalledAction)
            self.categoriesQVBoxLayout.removeWidget(self.buttonCalledAction)
            logging.info(f'Removed the category {self.buttonCalledAction.text()}')
        else:
            logging.info(f'Declined removing the category {self.buttonCalledAction.text()}')
        self.deleteDialog.warningLabel.setText('Do you want to delete file?')

    def open_category(self):
        self.categoryQLabel.setText(self.buttonCalledAction.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowInteractivity()
    win.show()
    sys.exit(app.exec_())
