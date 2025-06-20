# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        # App Settings
        self.setWindowTitle("Calculator App")
        self.resize(300,400)

        # Create all widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))

        self.grid = QGridLayout()

        self.buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
            ]
        
        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)

            # Apply styling based on button type
            if text in ['+', '-', '*', '/', '=']:
                button.setStyleSheet("""
                    QPushButton {
                        font: 20pt Comic Sans MS;
                        padding: 15px;
                        border-radius: 15px;
                        background-color: #add8e6;  /* Light blue */
                    }
                    QPushButton:hover {
                        background-color: #87ceeb;  /* Sky blue on hover */
                    }
                """)
            else:
                button.setStyleSheet("""
                    QPushButton {
                        font: 20pt Comic Sans MS;
                        padding: 15px;
                        border-radius: 15px;
                        background-color: #ffffff;  /* White */
                    }
                    QPushButton:hover {
                        background-color: #d3d3d3;  /* Gray on hover */
                    }
                """)

            self.grid.addWidget(button, row, col)

            
            col +=1

            if col > 3:
                col = 0
                row +=1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("Del")
        self.clear.setStyleSheet("""
                    QPushButton {
                        font: 20pt Comic Sans MS;
                        padding: 15px;
                        border-radius: 15px;
                        background-color: #f08080;  /* Light red */
                    }
                    QPushButton:hover {
                        background-color: #fa8072;  /* Salmon on hover */
                    }
                """)
        self.delete.setStyleSheet("""
                    QPushButton {
                        font: 20pt Comic Sans MS;
                        padding: 15px;
                        border-radius: 15px;
                        background-color: #f08080;  /* Light red */
                    }
                    QPushButton:hover {
                        background-color: #fa8072;  /* Salmon on hover */
                    }
                """)

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)


        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)


    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))

            except Exception as e:
                print("Error", e)
                
        elif text == "Clear":
            self.text_box.clear()

        elif text == "Del":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])
        
        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)


if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #e6f2ff}")
    main_window.show()
    app.exec_()