# Program supports EN, UA languages
import json

# abstract base class
class Localizator:
    def localize_main_window(self, window):
        pass

    def localize_settings_window(self, window):
        pass


class ENLocalizator(Localizator):
    def localize_main_window(self, window):
        window.addBookQButton.setText(' Add book')
        window.removeBookQButton.setText(' Remove Book')
        window.searchBar.setPlaceholderText('Search in category...')
        window.libLabel.setText('Library')
        window.allQButton.setText('All')
        window.favouritesQButton.setText('Favourites')
        window.createCategoryQButton.setText('Create new category')
        window.categoryQDialog.setWindowTitle("Create new category")
        window.categoryQDialog.setLabelText("Enter title of category:")
        window.table.setHorizontalHeaderLabels([
            "Name", "Author", "Genre", "Published", "Page", " "
        ])
        window.categoryQDialog.setOkButtonText('Ok')
        window.categoryQDialog.setCancelButtonText('Cancel')
        window.categoryQLabel.setText('Choose category...')

    def localize_settings_window(self, window):
        window.settingsLabel.setText('Settings')
        window.setWindowTitle('Settings')
        window.languageLabel.setText('Language')


class UALocalizator(Localizator):
    def localize_main_window(self, window):
        window.addBookQButton.setText(' Додати книгу')
        window.removeBookQButton.setText(' Видалити книгу')
        window.searchBar.setPlaceholderText('Шукати в категорії...')
        window.libLabel.setText('Бібліотека')
        window.allQButton.setText('Всі')
        window.favouritesQButton.setText('Улюблені')
        window.createCategoryQButton.setText('Створити нову категорію')
        window.categoryQDialog.setWindowTitle("Створити нову категорію")
        window.categoryQDialog.setLabelText("Введіть назву категорії:")
        window.table.setHorizontalHeaderLabels([
            "Ім\'я", "Автор", "Жанр", "Опубліковано", "Сторінка", " "
        ])
        window.categoryQDialog.setOkButtonText('Ок')
        window.categoryQDialog.setCancelButtonText('Скасувати')
        window.categoryQLabel.setText('Виберіть категорію...')

    def localize_settings_window(self, window):
        window.settingsLabel.setText('Налаштування')
        window.setWindowTitle('Налаштування')
        window.languageLabel.setText('Мова       ')


def set_main_menu_localization(window):
    # changed the directory to solve the problem localy;
    # file was not found without full path.
    with open('E:\Написані програми\Python\BookReaderProject\design\language.json') as json_file:
        lg_info = json.load(json_file)
    if lg_info['language'] == 'EN':
        ENLocalizator().localize_main_window(window)
    elif lg_info['language'] == 'UA':
        UALocalizator().localize_main_window(window)
    else:
        raise Exception('something goes wrong.')


def set_settings_localization(window):
    with open('language.json') as json_file:
        lg_info = json.load(json_file)
    if lg_info['language'] == 'EN':
        ENLocalizator().localize_settings_window(window)
    elif lg_info['language'] == 'UA':
        UALocalizator().localize_settings_window(window)
    else:
        raise Exception('something goes wrong.')

