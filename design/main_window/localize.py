# Program supports EN, UA languages
import json
from PyQt5.QtCore import QSize
import os


# abstract base class
class Localizator:
    def localize_main_window(self, window):
        pass


class ENLocalizator(Localizator):
    def localize_main_window(self, window):
        window.addBookQButton.setText(' Add book')
        window.removeBookQButton.setText(' Remove Book')
        window.searchBar.setPlaceholderText('Search in category...')
        window.libLabel.setText('Library')
        window.allQButton.setText('All')
        window.favouritesQButton.setText('Favourites')
        window.open_act.setText("Open")
        window.edit_act.setText("Rename")
        window.delete_act.setText("Delete")
        window.createCategoryQButton.setText('Create new category')
        window.categoryQDialog.setWindowTitle("Create new category")
        window.categoryQDialog.setLabelText("Enter title of category:")
        window.table.setHorizontalHeaderLabels([
            "Name", "Author", "Added", "Page", "Rating", " "
        ])
        window.categoryQDialog.setOkButtonText('Ok')
        window.categoryQDialog.setCancelButtonText('Cancel')
        window.categoryQLabel.setText('Choose category...')


class UALocalizator(Localizator):
    def localize_main_window(self, window):
        window.addBookQButton.setText(' Додати книгу')
        window.removeBookQButton.setText(' Видалити книгу')
        window.searchBar.setPlaceholderText('Шукати в категорії...')
        window.libLabel.setText('Бібліотека')
        window.allQButton.setText('Всі')
        window.favouritesQButton.setText('Улюблені')
        window.open_act.setText("Відкрити")
        window.edit_act.setText("Перейменувати")
        window.delete_act.setText("Видалити")
        window.createCategoryQButton.setText('Створити нову категорію')
        window.categoryQDialog.setWindowTitle("Створити нову категорію")
        window.categoryQDialog.setLabelText("Введіть назву категорії:")
        window.table.setHorizontalHeaderLabels([
            "Ім\'я", "Автор", "Додано", "Сторінка", "Оцінка", " "
        ])
        window.categoryQDialog.setOkButtonText('Ок')
        window.categoryQDialog.setCancelButtonText('Скасувати')
        window.categoryQLabel.setText('Виберіть категорію...')


def set_main_menu_localization(window):
    # changed the directory to solve the problem locally;
    # file was not found without full path.
    with open(os.path.expanduser("~/Documents/LNUReader/settings.json")) as json_file:
        lg_info = json.load(json_file)
    if lg_info['language'] == 'EN':
        ENLocalizator().localize_main_window(window)
    elif lg_info['language'] == 'UA':
        UALocalizator().localize_main_window(window)
    else:
        raise Exception('something goes wrong.')
