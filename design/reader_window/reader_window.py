from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QInputDialog, QTableWidget, QHeaderView, \
    QTableWidgetItem, QLineEdit, QScrollBar, QAbstractItemView, QMessageBox, \
    QShortcut, QFileDialog, QMenu, QSizePolicy, QStackedWidget
from PyQt5.QtGui import QFont, QIcon, QMouseEvent, QKeyEvent
from PyQt5.QtCore import QSize, Qt
from design.main_window.dialog_confirm_decline import ConfirmDialog
from design.main_window.messages import WarningMessage
import db.database as db
import sys
import design.reader_window.styles as styles
import design.reader_window.localize as localize
import logging
import os
import design.reader_window.content_window as content_win


class ReaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main body
        self.bodyQHBoxLayout = QVBoxLayout()
        self.body = QWidget()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.body)

        # Container
        self.containerQHBoxLayout = QHBoxLayout()
        self.containerQHBoxLayout.setSpacing(50)
        self.container = QWidget()

        # SideBar
        self.sidebarQVBoxLayout = QVBoxLayout()
        self.sidebar = QWidget()
        self.sidebar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        # Back Button
        self.backQButton = QPushButton()
        self.backQButton.setIcon(QIcon('design/images/back.png'))
        self.backQButton.setIconSize(QSize(32, 32))
        self.backQButton.setFocusPolicy(Qt.NoFocus)
        self.backQButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        styles.Styles.set_back_button_styles(self.backQButton)

        # Button menu
        self.buttonMenuQVBoxLayout = QVBoxLayout()
        self.buttonMenuQVBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonMenu = QWidget()

        # Fullscreen Button
        self.fullscreenQButton = QPushButton()
        self.fullscreenQButton.setIcon(QIcon('design/images/fullscreen.png'))
        self.fullscreenQButton.setIconSize(QSize(32, 32))
        self.fullscreenQButton.setFocusPolicy(Qt.NoFocus)

        # Zoom In Button
        self.zoomInQButton = QPushButton()
        self.zoomInQButton.setIcon(QIcon('design/images/zoom-in.png'))
        self.zoomInQButton.setIconSize(QSize(32, 32))
        self.zoomInQButton.setFocusPolicy(Qt.NoFocus)

        # Zoom Out Button
        self.zoomOutQButton = QPushButton()
        self.zoomOutQButton.setIcon(QIcon('design/images/zoom-out.png'))
        self.zoomOutQButton.setIconSize(QSize(32, 32))
        self.zoomOutQButton.setFocusPolicy(Qt.NoFocus)

        # Show Content Button
        self.contentQButton = QPushButton()
        self.contentQButton.setIcon(QIcon('design/images/content.png'))
        self.contentQButton.setIconSize(QSize(32, 32))
        self.contentQButton.setFocusPolicy(Qt.NoFocus)
        self.contentQButton.clicked.connect(self.show_content)

        # Add Bookmarks Button
        self.addBookmarkQButton = QPushButton()
        self.addBookmarkQButton.setIcon(QIcon('design/images/bookmark.png'))
        self.addBookmarkQButton.setIconSize(QSize(32, 32))
        self.addBookmarkQButton.setFocusPolicy(Qt.NoFocus)

        # Add Notes Button
        self.addNoteQButton = QPushButton()
        self.addNoteQButton.setIcon(QIcon('design/images/notes.png'))
        self.addNoteQButton.setIconSize(QSize(32, 32))
        self.addNoteQButton.setFocusPolicy(Qt.NoFocus)

        # Switch mode Button
        self.switchModeQButton = QPushButton()
        self.switchModeQButton.setIcon(QIcon('design/images/switch.png'))
        self.switchModeQButton.setIconSize(QSize(32, 32))
        self.switchModeQButton.setFocusPolicy(Qt.NoFocus)

        # Content
        self.contentQVBoxLayout = QVBoxLayout()
        self.content = QWidget()
        self.content.setStyleSheet("""
        background-color: white;
        """)

        # Content window
        self.content_window = None

        # Footer
        self.footerQHBoxLayout = QHBoxLayout()
        self.footer = QWidget()
        self.footer.setContentsMargins(11, 0, 0, 0)

        # Show progress Label
        self.progressLabel = QLabel("100%                    ")
        self.progressLabel.setAlignment(Qt.AlignCenter)

        # Switch page block
        self.switchPageQHBoxLayout = QHBoxLayout()
        self.switchPageWidget = QWidget()
        self.switchPageQHBoxLayout.setSpacing(0)

        # Previous Page Button
        self.previousPageQButton = QPushButton()
        self.previousPageQButton.setIcon(QIcon('design/images/back.png'))
        self.previousPageQButton.setIconSize(QSize(32, 32))
        self.previousPageQButton.setFocusPolicy(Qt.NoFocus)

        # Next Page Button
        self.nextPageQButton = QPushButton()
        self.nextPageQButton.setIcon(QIcon('design/images/front.png'))
        self.nextPageQButton.setIconSize(QSize(32, 32))
        self.nextPageQButton.setFocusPolicy(Qt.NoFocus)

        styles.Styles.set_window_styles(self)
        localize.set_reader_localization(self)
        self.init_body()

    def init_sidebar(self):
        self.sidebarQVBoxLayout.addWidget(self.backQButton)
        self.buttonMenuQVBoxLayout.addWidget(self.fullscreenQButton)
        self.buttonMenuQVBoxLayout.addWidget(self.zoomInQButton)
        self.buttonMenuQVBoxLayout.addWidget(self.zoomOutQButton)
        self.buttonMenuQVBoxLayout.addWidget(self.contentQButton)
        self.buttonMenuQVBoxLayout.addWidget(self.addBookmarkQButton)
        self.buttonMenuQVBoxLayout.addWidget(self.addNoteQButton)
        self.buttonMenuQVBoxLayout.addWidget(self.switchModeQButton)
        self.buttonMenu.setLayout(self.buttonMenuQVBoxLayout)
        self.sidebarQVBoxLayout.addWidget(self.buttonMenu)
        self.sidebarQVBoxLayout.addStretch()
        self.sidebarQVBoxLayout.setSpacing(80)
        self.sidebar.setLayout(self.sidebarQVBoxLayout)

    def init_content(self):
        self.content.setLayout(self.contentQVBoxLayout)

    def init_container(self):
        self.init_sidebar()
        self.init_content()
        self.containerQHBoxLayout.addWidget(self.sidebar)
        self.containerQHBoxLayout.addWidget(self.content)
        self.container.setLayout(self.containerQHBoxLayout)

    def init_footer(self):
        self.footerQHBoxLayout.addWidget(self.progressLabel)

        self.switchPageQHBoxLayout.addWidget(self.previousPageQButton)
        self.switchPageQHBoxLayout.addWidget(self.nextPageQButton)
        self.switchPageWidget.setLayout(self.switchPageQHBoxLayout)
        self.footerQHBoxLayout.addStretch()
        self.footerQHBoxLayout.addWidget(self.switchPageWidget)
        self.footerQHBoxLayout.addStretch()
        self.footer.setLayout(self.footerQHBoxLayout)

    def init_body(self):
        self.init_container()
        self.init_footer()
        self.bodyQHBoxLayout.addWidget(self.container)
        self.bodyQHBoxLayout.addWidget(self.footer)
        self.body.setLayout(self.bodyQHBoxLayout)
        self.setCentralWidget(self.stack)

    def show_content(self):
        self.stack.addWidget(self.create_content_widget())
        self.stack.setCurrentIndex(1)

    def hide_content(self):
        self.stack.setCurrentIndex(0)
        self.stack.removeWidget(self.content_window)
        self.content_window = None

    def create_content_widget(self):
        self.content_window = content_win.ContentWindow()
        self.content_window.backQButton.clicked.connect(self.hide_content)
        return self.content_window
