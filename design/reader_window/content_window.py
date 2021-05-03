from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QInputDialog, QTableWidget, QHeaderView, \
    QTableWidgetItem, QLineEdit, QScrollBar, QAbstractItemView, QMessageBox, \
    QShortcut, QFileDialog, QMenu, QSizePolicy, QTabWidget, QGridLayout
from PyQt5.QtGui import QFont, QIcon, QMouseEvent, QKeyEvent
from PyQt5.QtCore import QSize, Qt
from design.main_window.dialog_confirm_decline import ConfirmDialog
from design.main_window.messages import WarningMessage
import db.database as db
import sys
import design.reader_window.styles as styles
import logging
import os


class ContentWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 400)
        self.resize(1000, 600)
        self.setWindowTitle('Bookmarks & Notes')
        self.setWindowIcon(QIcon('design/images/icon.ico'))

        self.mainLayout = QVBoxLayout()
        self.bookmarksLabel = QLabel("Widget in Tab 1.")
        self.notesLabel = QLabel("Widget in Tab 2.")
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.bookmarksLabel, "Bookmarks")
        self.tabWidget.addTab(self.notesLabel, "Notes")

        # Back Button
        self.backQButton = QPushButton()
        self.backQButton.setIcon(QIcon('design/images/back.png'))
        self.backQButton.setIconSize(QSize(32, 32))
        self.backQButton.setFocusPolicy(Qt.NoFocus)
        self.backQButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        styles.Styles.set_back_button_styles(self.backQButton)

        self.main_init()

    def main_init(self):
        self.mainLayout.addWidget(self.backQButton)
        self.mainLayout.addWidget(self.tabWidget)
        self.setLayout(self.mainLayout)

        self.setStyleSheet("""
                        background-color: beige;
                        color: #5c5c5c;
                        font-family: "Century Gothic";
                        """)

