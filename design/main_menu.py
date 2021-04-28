from main_menu_front import *
import settings_menu
import json


class WindowInteractivity(MainWindow):
    def __init__(self):
        super().__init__()
        # create needed variable
        self.acceptableFormats = ['.pdf', '.epub', '.fb2']
        self.filesDirectories = []
        self.deleteDialog = ConfirmDialog()

        # Create Category Button options
        self.createCategoryQButton.clicked.connect(self.show_category_creating_dialog)
        self.createCategoryQButton.setFocusPolicy(Qt.NoFocus)

        # creating shortcuts
        QShortcut("Ctrl+O", self).activated.connect(self.open_files)
        QShortcut("Ctrl+A", self).activated.connect(lambda: self.table.selectAll())

        # bind buttons to functions
        self.addBookQButton.clicked.connect(self.open_files)
        self.removeBookQButton.clicked.connect(self.delete_files)

        # bind actions to functions
        self.open_act.triggered.connect(self.open_category)
        self.edit_act.triggered.connect(self.rename_category)
        self.delete_act.triggered.connect(self.delete_category)

        # drag and drop settings
        self.setAcceptDrops(True)

        # binding table to functions
        self.table.clicked.connect(lambda index: self.table.selectRow(index.row()))

    def show_category_creating_dialog(self):
        """
        Method show dialog after pressing "Create new category" button
        :return: None
        """
        ok = self.categoryQDialog.exec_()
        text = self.categoryQDialog.textValue()
        if ok:
            self.execute_category_creating_dialog(text)

    def execute_category_creating_dialog(self, category_name):
        """
        Method execute category creating by dialog.
        Also it insert new category to Database and set options to new button.

        :param category_name: text of InputDialog (name of category)
        :return: None
        """
        if self.is_create_dialog_error(category_name):
            return
        added_button = QPushButton(category_name)
        self.set_category_button_options(added_button)
        db.insert_data(self.db_connection, "library", (category_name,))
        self.categoriesQVBoxLayout.addWidget(added_button)
        self.categoriesQWidget.setLayout(self.categoriesQVBoxLayout)

    def is_create_dialog_error(self, category_name):
        """
        Method checks if create dialog raise error.
        Error can be raised if category name is empty or if category is already exists.
        :param category_name: text of InputDialog (name of category)
        :return: boolean
        """
        if category_name.isspace() or not category_name:
            WarningMessage("Empty input", 'You wrote empty category title. Please try again')
            return True
        if category_name in [button.text() for button in self.categories]:
            WarningMessage("Category is already exists", "You are bustard")
            return True

    def settings_button_clicked(self):
        """
        Method opens settings window and closes current window.
        :return: None
        """
        if self.sett_menu is None:
            self.sett_menu = settings_menu.SettingsWindow()

        self.remember_window_size()

        self.sett_menu.set_size()
        self.sett_menu.show()
        self.close()

    def remember_window_size(self):
        with open('settings.json') as json_file:
            lg_info = json.load(json_file)
        lg_info["screen"] = self.get_window_size()
        with open('settings.json', 'w') as outfile:
            json.dump(lg_info, outfile)

    def get_window_size(self):
        return self.size().width(), self.size().height()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        """
        Overloading mouse press event. Clears Focus from window.
        :param a0:
        :return: None
        """
        focused_widget = QApplication.focusWidget()
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()

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

    def keyPressEvent(self, event):
        """
        Method does operations with hotkeys in table.
        :param event: key pressing event
        :return: None
        """
        if event.key() == Qt.Key_Down:
            self.chose_row(1)
        if event.key() == Qt.Key_Up:
            self.chose_row(-1)
        if event.key() == Qt.Key_Delete:
            self.delete_files()

    def dragEnterEvent(self, event):
        # TODO Documentation
        url = str(event.mimeData().urls()[0])
        if any([form in url for form in self.acceptableFormats]):
            event.accept()
            logging.info(f"file's url = {url} was added")
        else:
            event.ignore()
            logging.info(f"file's url = {url} was declined")

    def dropEvent(self, event):
        # TODO Documentation
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
        # TODO Documentation
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
                insert_data()
                logging.info(f"Directory {directory} was added to list.")
            else:
                logging.info(f"Directory {directory} was ignored.")

    def delete_files(self):
        # TODO Documentation
        try:
            if len(self.table.selectedItems()) == 0:
                WarningMessage("No file selected", "Can not delete not selected file")
                return
            if self.deleteDialog.exec_():
                for index in self.table.selectedItems():
                    self.delete_book_from_table(index.row(), index.column())
        except Exception as e:
            print(e)
            return

    def delete_book_from_table(self, r, c):
        # TODO Documentation
        if c != 0:
            logging.info(f"Deleting from table is declined for item row = {r}")
            return
        self.table.removeRow(r)
        logging.info(f"Deleted item in table with row = {r}")

    def rename_category(self):
        # TODO Documentation
        if self.is_standard_category():
            return

        self.categoryQDialog.setWindowTitle('Rename')
        ok = self.categoryQDialog.exec_()
        text = self.categoryQDialog.textValue()
        if ok:
            db.update_data(self.db_connection, "library", "library_name", text, self.buttonCalledAction.text())
            if self.categoryQLabel.text() == self.buttonCalledAction.text():
                self.categoryQLabel.setText(text)
            logging.info(f"Renamed category {self.buttonCalledAction.text()} to {text}")
            self.buttonCalledAction.setText(text)
        else:
            logging.info(f"Renaming category {self.buttonCalledAction.text()} was declined")
        self.categoryQDialog.setWindowTitle('Create new category')

    def delete_category(self):
        # TODO Documentation
        if self.is_standard_category():
            return

        self.deleteDialog.warningLabel.setText('Do you want to delete category?')
        ok = self.deleteDialog.exec_()
        if ok:
            self.categories.remove(self.buttonCalledAction)
            self.categoriesQVBoxLayout.removeWidget(self.buttonCalledAction)
            db.delete_data(self.db_connection, "library", self.buttonCalledAction.text())
            logging.info(f'Removed the category {self.buttonCalledAction.text()}')
        else:
            logging.info(f'Declined removing the category {self.buttonCalledAction.text()}')
        self.deleteDialog.warningLabel.setText('Do you want to delete file?')

    def open_category(self):
        self.categoryQLabel.setText(self.buttonCalledAction.text())
        for ctg in self.categories:
            styles.Styles.set_category_button_styles(ctg)
        styles.Styles.set_clicked_category_button_styles(self.buttonCalledAction)

    def chose_row(self, i=1):
        # TODO Documentation
        if i not in [1, -1]:
            return
        row = self.table.currentRow()
        self.table.selectRow(row+i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowInteractivity()
    win.show()
    sys.exit(app.exec_())

# TODO table styles
