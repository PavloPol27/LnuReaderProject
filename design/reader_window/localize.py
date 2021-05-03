# Program supports EN, UA languages
import json
from PyQt5.QtCore import QSize
import os

# abstract base class
class Localizator:

    def localize_reader_window(self, window):
        pass


class ENLocalizator(Localizator):

    def localize_reader_window(self, window):
        window.fullscreenQButton.setToolTip("Fullscreen mode")
        window.zoomInQButton.setToolTip("Zoom In")
        window.zoomOutQButton.setToolTip("Zoom Out")
        window.contentQButton.setToolTip("Show content")
        window.addBookmarkQButton.setToolTip("Add a bookmark")
        window.addNoteQButton.setToolTip("Add a note")
        window.switchModeQButton.setToolTip("Switch a mode")


class UALocalizator(Localizator):

    def localize_reader_window(self, window):
        window.fullscreenQButton.setToolTip("Повноекранний режим")
        window.zoomInQButton.setToolTip("Приблизити")
        window.zoomOutQButton.setToolTip("Віддалити")
        window.contentQButton.setToolTip("Показати зміст")
        window.addBookmarkQButton.setToolTip("Додати закладку")
        window.addNoteQButton.setToolTip("Додати нотатку")
        window.switchModeQButton.setToolTip("Змінити режим")


def set_reader_localization(window):
    with open(os.path.expanduser("~/Documents/LNUReader/settings.json")) as json_file:
        lg_info = json.load(json_file)
    if lg_info['language'] == 'EN':
        ENLocalizator().localize_reader_window(window)
    elif lg_info['language'] == 'UA':
        UALocalizator().localize_reader_window(window)
    else:
        raise Exception('something goes wrong.')
