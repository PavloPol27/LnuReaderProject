class Styles:
    def __init__(self):
        pass

    @staticmethod
    def set_settings_styles(window):
        window.setStyleSheet("""
                        background-color: beige;
                        color: #5c5c5c;
                        font-family: "Century Gothic";
                        """)
        window.settingsLabel.setStyleSheet("""
        font-size: 30px;
        """)
        window.languageLabel.setStyleSheet("""
        font-size: 20px;
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
