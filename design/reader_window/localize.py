# Program supports EN, UA languages
import json
from PyQt5.QtCore import QSize
import os

# abstract base class
class Localizator:

    def localize_reader_window(self, window):
        pass


class ENLocalizator(Localizator):

    def localize_settings_window(self, window):
        window.settingsLabel.setText('Settings')
        window.setWindowTitle('Settings')
        window.languageLabel.setText('Language')


class UALocalizator(Localizator):

    def localize_settings_window(self, window):
        window.settingsLabel.setText('Налаштування')
        window.setWindowTitle('Налаштування')
        window.languageLabel.setText('Мова       ')


def set_settings_localization(window):
    with open(os.path.expanduser("~/Documents/LNUReader/settings.json")) as json_file:
        lg_info = json.load(json_file)
    if lg_info['language'] == 'EN':
        ENLocalizator().localize_settings_window(window)
        window.ENButton.setIconSize(QSize(56, 56))
    elif lg_info['language'] == 'UA':
        UALocalizator().localize_settings_window(window)
        window.UAButton.setIconSize(QSize(56, 56))
    else:
        raise Exception('something goes wrong.')
