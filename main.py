# Imports
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout


# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(340,390)

# Design

# Show/Run
main_window.show()
app.exec_()