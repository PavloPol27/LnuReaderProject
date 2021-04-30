class Styles:
    def __init__(self):
        pass

    @staticmethod
    def set_window_styles(window):
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
                margin-bottom: 50px;
                }
                """)

        window.sidebar.setStyleSheet("""
                width: 50px;
                
                padding:0;
                margin: 0;
                """)