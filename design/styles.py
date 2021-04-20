import settings_menu


class Styles:
    @staticmethod
    def set_main_menu_styles(window):
        # Main style
        window.setStyleSheet("""
                background-color: beige;
                color: #5c5c5c;
                """)

        # Book buttons styles
        window.addBookQButton.setStyleSheet("""
                QPushButton:hover
                {
                border: 2px dashed #5c5c5c;
                border-radius: 15px;
                }

                QPushButton:pressed 
                {
                border-style: solid;
                }

                QPushButton
                {
                border: 0;
                font-size: 15px;
                width: 140px;
                height: 55px;
                }
                """)
        window.removeBookQButton.setStyleSheet("""
                QPushButton:hover
                {
                border: 2px dashed #5c5c5c;
                border-radius: 15px;
                }

                QPushButton:pressed 
                {
                border-style: solid;
                }

                QPushButton
                {
                border: 0;
                font-size: 15px;
                width: 160px;
                height: 55px;
                }
                """)

        # Settings button styles
        window.settingsQButton.setStyleSheet("""

                QPushButton:hover
                {
                border: 2px dashed #5c5c5c;
                border-radius: 20px;
                }

                QPushButton:pressed 
                {
                border-style: solid;
                }

                QPushButton
                {
                border: 0;
                width: 55px;
                height: 55px;
                }
                """)

        # Search Bar styles
        window.searchBar.setStyleSheet("""
                background-color: white;
                width: 100px;
                height: 25px;
                """)

        # Side Bar styles
        window.sideBar.setStyleSheet("""
                background-color: white;
                border: 1px solid #5c5c5c;
                width: 200px;
                padding:0;
                margin: 0;
                """)

        # Lib Label styles
        window.libLabel.setStyleSheet("""
                border-bottom: 0;
                border-top: 0;
                """)

        # Categories styles
        window.categoriesQWidget.setStyleSheet("""
                border-bottom: 0;
                border-top: 1px solid #5c5c5c;
                """)

        # Create category button styles
        window.createCategoryQButton.setStyleSheet("""
                QPushButton:hover
                {
                color: white;
                background-color : #6938fb;
                }
                QPushButton
                {
                border-top: 1px solid #5c5c5c;
                font-size: 12px;
                height: 30px;
                }
                """)

        # Content styles
        window.content.setStyleSheet("""
                border: 1px solid #5c5c5c;
                border-left: 0;
                """)

        # Category label styles
        window.categoryQLabel.setStyleSheet("""
                border-bottom: 0;
                border-left: 0;
                """)

        # Table styles
        window.table.horizontalHeader().setStyleSheet("""
                border: 1px solid black;
                border-top: 0px;
                border-right: 0px;
                border-left: 0px;
                """)

        window.table.setStyleSheet("""
                QTableWidget
                {
                border-left: 0;
                background-color: white;
                selection-background-color: #6938fb;
                }
                """)

        window.tableScrollBar.setStyleSheet("""
                QScrollBar {
                border: 1px transparent #2A2929;
                border-radius: 5px;
                }
                QScrollBar::handle {
                background: #d0d0d0;
                border-radius: 5px;
                }
                """)

        window.categoryQDialog.setStyleSheet("""
                QDialog {
                color: #5c5c5c;
                background-color: beige;
                }
                QDialog QPushButton:hover
                {
                border: 2px dashed #5c5c5c;
                border-radius: 15px;
                }

                QDialog QPushButton:pressed 
                {
                border-style: solid;
                }

                QDialog QPushButton
                {
                border: 0;
                font-size: 15px;
                width: 90px;
                height: 35px;
                }
                QDialog QLineEdit
                {
                background-color: white;
                width: 100px;
                height: 25px;
                }
                
        """)

    @staticmethod
    def set_category_button_styles(category_button):
        category_button.setStyleSheet("""  
                QPushButton
                {          
                border-top: 0;
                border-bottom: 0;
                font-size: 12px;
                padding-left: 10px;
                height: 30px;
                text-align: left;
                }
                QPushButton:hover
                {
                color: white;
                background-color : #6938fb;
                }
                QPushButton:focus
                {
                border:0;
                color: white;
                background-color : #6938fb;
                }
                """)

    @staticmethod
    def set_settings_styles(window):
        window.setStyleSheet("""
                        background-color: beige;
                        color: #5c5c5c;
                        """)

        window.backQButton.setStyleSheet("""
                QPushButton:hover
                {
                border: 2px dashed #5c5c5c;
                border-radius: 25px;
                }

                QPushButton:pressed 
                {
                border-style: solid;
                }

                QPushButton
                {
                border: 0;
                width: 50px;
                height: 50px;
                }
                """)

        window.ENButton.setStyleSheet("""
                QPushButton
                {
                width: 64px;
                height: 64px;
                border: 0;
                }
                """)

        window.UAButton.setStyleSheet("""
                QPushButton
                {
                width: 64px;
                height: 64px;
                border: 0;
                }
                """)