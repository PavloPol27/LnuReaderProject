from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QInputDialog, QTableWidget, QHeaderView, \
    QTableWidgetItem, QLineEdit, QScrollBar, QAbstractItemView, QMessageBox, \
    QShortcut, QFileDialog, QMenu
from PyQt5.QtGui import QFont, QIcon, QMouseEvent, QKeyEvent
from PyQt5.QtCore import QSize, Qt
from design.main_window.dialog_confirm_decline import ConfirmDialog
from design.main_window.messages import WarningMessage
import db.database as db
import sys
import design.main_window.localize as localize
import design.main_window.styles as styles
import logging
import os
import json

logging.basicConfig(filename='ReaderLogger.log',
                    level=logging.INFO,
                    format='Called from:%(funcName)s, %(message)s, time: %(asctime)s')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # needed variable

        self.db_connection = self.connect_to_db()
        db.create_db(self.db_connection)
        self.buttonCalledAction = None

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
        self.addBookQButton.setIcon(QIcon('design/images/add.png'))
        self.addBookQButton.setIconSize(QSize(28, 28))
        self.addBookQButton.setFocusPolicy(Qt.NoFocus)

        # Remove Book Button
        self.removeBookQButton = QPushButton()
        self.removeBookQButton.setIcon(QIcon('design/images/removeBook.png'))
        self.removeBookQButton.setIconSize(QSize(28, 28))
        self.removeBookQButton.setFocusPolicy(Qt.NoFocus)

        # Search Bar
        self.searchBar = QLineEdit()
        self.searchBar.setClearButtonEnabled(True)
        self.searchBar.setFocusPolicy(Qt.ClickFocus)

        # Settings
        self.settingsQButton = QPushButton()
        self.settingsQButton.setIcon(QIcon('design/images/settings.png'))
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
        styles.Styles.set_context_menu_styles(self.context_menu)

        # Categories
        self.categoriesQWidget = QWidget()
        self.categoriesQVBoxLayout = QVBoxLayout()
        self.categoriesQVBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.categoriesQVBoxLayout.setSpacing(0)

        # Categories buttons
        self.categories = []
        self.allQButton = QPushButton()
        self.favouritesQButton = QPushButton()

        # Create Category Button
        self.createCategoryQButton = QPushButton()

        # Create Category Dialog
        self.categoryQDialog = QInputDialog()
        self.categoryQDialog.setInputMode(QInputDialog.TextInput)
        self.categoryQDialog.setWindowIcon(QIcon('design/images/icon.ico'))
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

        self.cont = QWidget()

    def set_size(self):
        with open(os.path.expanduser("~/Documents/LNUReader/settings.json")) as json_file:
            lg_info = json.load(json_file)
        self.resize(lg_info["screen"][0], lg_info["screen"][1])

    @staticmethod
    def connect_to_db():
        path_to_db = os.path.expanduser("~/Documents/LNUReader")
        if not os.path.exists(path_to_db):
            os.makedirs(path_to_db)
        return db.create_connection(path_to_db + r'\ReaderDatabase.db')

    def init_header(self):
        self.headerQHBoxLayout.addWidget(self.addBookQButton)
        self.headerQHBoxLayout.addWidget(self.removeBookQButton)
        self.headerQHBoxLayout.addStretch()
        self.headerQHBoxLayout.addWidget(self.searchBar)
        self.headerQHBoxLayout.addWidget(self.settingsQButton)
        self.header.setLayout(self.headerQHBoxLayout)

    def init_categories(self):
        self.set_category_button_options(self.allQButton)
        self.set_category_button_options(self.favouritesQButton)
        self.categoriesQVBoxLayout.addWidget(self.allQButton)
        self.categoriesQVBoxLayout.addWidget(self.favouritesQButton)
        user_categories = db.select_all_data(self.db_connection, "library")["library_name"]
        for ctg in user_categories:
            added_button = QPushButton(ctg)
            self.set_category_button_options(added_button)
            self.categoriesQVBoxLayout.addWidget(added_button)
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
        self.table.setShowGrid(False)
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setHighlightSections(False)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.resizeSection(2, 120)
        header.resizeSection(3, 100)
        header.resizeSection(4, 80)
        header.resizeSection(5, 50)

        for i in range(30):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(f'text{i}'))
            self.table.setItem(i, 1, QTableWidgetItem(f'author{i}'))

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

    def set_category_button_options(self, category_button):
        styles.Styles.set_category_button_styles(category_button)
        category_button.setFocusPolicy(Qt.ClickFocus)
        category_button.setContextMenuPolicy(Qt.CustomContextMenu)
        category_button.customContextMenuRequested.connect(self.on_context_menu)
        self.categories.append(category_button)
        category_button.clicked.connect(self.category_button_clicked)

    def category_button_clicked(self):
        for ctg in self.categories:
            styles.Styles.set_category_button_styles(ctg)
        styles.Styles.set_clicked_category_button_styles(self.sender())
        self.categoryQLabel.setText(self.sender().text())

    def settings_button_clicked(self):
        """
        Method opens settings window and closes current window.
        :return: None
        """
        # if self.sett_menu is None:
        #     self.sett_menu = settings_menu.SettingsWindow()
        #
        # self.remember_window_size()
        #
        # self.sett_menu.set_size()
        # self.sett_menu.show()
        # self.close()

    def on_context_menu(self, point):
        """
        Method that show context menu when user does right mouse click on category.
        :param point: cursor coordinates
        :return: None
        """
        self.buttonCalledAction = self.sender()
        if not self.is_standard_category():
            self.delete_act.setEnabled(True)
            self.edit_act.setEnabled(True)
        else:
            self.delete_act.setEnabled(False)
            self.edit_act.setEnabled(False)
        self.context_menu.exec_(self.buttonCalledAction.mapToGlobal(point))

    def is_standard_category(self):
        """
        Method checks if right clicked category is standard (All + Favourites).
        :return: boolean
        """
        return self.buttonCalledAction in [button for button in self.categories[:2]]
