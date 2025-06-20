# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTimer
import math
import re


class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFocus()
        # App Settings
        self.setWindowTitle("Calculator App")
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(300,500)

        # Create all widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))
        self.text_box.setStyleSheet("""
            QLineEdit {
                border: 2px solid #f1c40f;  /* Yellow border */
                border-radius: 15px;        /* Rounded corners */
                padding: 10px;
                background-color: #000000;  /* Black background */
                color: #f1c40f;             /* Yellow text */
            }
        """)
        self.text_box.setAlignment(Qt.AlignLeft)


        self.grid = QGridLayout()

        self.buttons = [
            "sin", "cos", "tan", "log",
            "√", "(", ")", "/", "7",
            "8", "9", "*","4", "5",
            "6", "-", "1", "2", "3",
            "+", "0", ".", "=", 
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
                        background-color: #444444;
                        color: #f1c40f;
                    }
                    QPushButton:hover {
                        background-color: #666666;
                    }
                """)

            else:
                button.setStyleSheet("""
                    QPushButton {
                    font: 20pt Comic Sans MS;
                    padding: 15px;
                    border-radius: 15px;
                    background-color: #333333;  /* Dark gray */
                    color: #f1c40f;             /* Yellow text */
                }
                QPushButton:hover {
                    background-color: #555555;
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
                        background-color: #c0392b;  /* Red */
                        color: #ffffff;             /* White text */
                    }
                    QPushButton:hover {
                        background-color: #e74c3c;
                    }
                """)
        self.delete.setStyleSheet("""
                    QPushButton {
                    font: 20pt Comic Sans MS;
                    padding: 15px;
                    border-radius: 15px;
                    background-color: #c0392b;  /* Red */
                    color: #ffffff;             /* White text */
                }
                QPushButton:hover {
                    background-color: #e74c3c;
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

    def animate_button(self, button):
        # Save the original style
        original_style = button.styleSheet()

        # Apply the pressed style
        button.setStyleSheet(original_style + " QPushButton { background-color: #cccccc; }")

        # Use QTimer to revert the style after 150 milliseconds
        QTimer.singleShot(150, lambda: button.setStyleSheet(original_style))


    def is_valid_input(self, current_value, new_input):
        operators = ['+', '-', '*', '/']

        if not current_value:
            # Prevent starting with an operator (except minus)
            if new_input in ['+', '*', '/']:
                return False

        if current_value:
            last_char = current_value[-1]

            # Prevent two operators in a row
            if last_char in operators and new_input in operators:
                return False
            
            # Prevent double decimals within the same number
            if new_input == '.':
                # Get the last part after an operator
                tokens = re.split(r'[\+\-\*/]', current_value)
                if '.' in tokens[-1]:
                    return False


        return True

    def get_validated_expression(self, expression):
        # Auto-close missing parentheses
        open_count = expression.count('(')
        close_count = expression.count(')')

        if open_count > close_count:
            expression += ')' * (open_count - close_count)

        if not expression.strip():
            return None

        return expression

    def button_click(self):
        button = self.sender()
        text = button.text()
        self.animate_button(button)

        if text == "=":
            symbol = self.text_box.text()

            validated = self.get_validated_expression(symbol)
            if not validated:
                self.text_box.setText("Error")
                return

            try:
                res = eval(validated, {"__builtins__": None, "math": math})
                self.text_box.setText(str(res))
            except Exception:
                self.text_box.setText("Error")
                
        elif text == "Clear":
            self.text_box.clear()

        elif text == "Del":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])
        
        else:
            current_value = self.text_box.text()

            if text == '√':
                self.text_box.setText(current_value + 'math.sqrt(')

            elif text == 'sin':
                self.text_box.setText(current_value + 'math.sin(')

            elif text == 'cos':
                self.text_box.setText(current_value + 'math.cos(')

            elif text == 'tan':
                self.text_box.setText(current_value + 'math.tan(')

            elif text == 'log':
                self.text_box.setText(current_value + 'math.log(')

            else:
                if self.is_valid_input(current_value, text):
                    self.text_box.setText(current_value + text)

        self.text_box.setCursorPosition(0)



    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Backspace:
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])

        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            symbol = self.text_box.text()

            validated = self.get_validated_expression(symbol)
            if not validated:
                self.text_box.setText("Error")
                return

            try:
                res = eval(validated, {"__builtins__": None, "math": math})
                self.text_box.setText(str(res))
            except Exception:
                self.text_box.setText("Error")
        
        elif key == Qt.Key_Escape:
            self.close()

        else:
            text = event.text()
            if text.isdigit() or text in ['+', '-', '*', '/', '.']:
                current_value = self.text_box.text()
                if self.is_valid_input(current_value, text):
                    self.text_box.setText(current_value + text)

        self.text_box.setCursorPosition(0)



if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #000000; }")
    main_window.show()
    app.exec_()