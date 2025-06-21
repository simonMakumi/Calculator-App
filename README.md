# 🧮 PyQt5 Calculator App

![Calculator Screenshot](calc_pic.png)

## 📚 Project Overview

This is a **Modern Scientific Calculator** built using **PyQt5** in Python.  
The calculator features:
- A sleek **black and yellow theme**
- Rounded buttons with click animations
- Support for **basic and scientific operations** including:
  - sin, cos, tan, log, square root, and parentheses handling
- Smart input validation and automatic parentheses balancing
- Keyboard input support
- Custom app icon

---

## 🚀 Features

- **Basic Arithmetic:** Addition, Subtraction, Multiplication, Division
- **Scientific Functions:** sin, cos, tan, log, square root
- **Smart Validation:** Prevents invalid input (like double operators)
- **Auto-close Parentheses:** Balances expressions automatically
- **Keyboard Support:** Type directly using keyboard keys
- **Responsive Design:** Smooth button animations
- **Dark Theme:** Stylish black and yellow color scheme
- **Custom Icon:** App includes a custom window icon (if supported by packager)

---

## 🛠️ Technologies Used
- Python 3.x
- PyQt5
- Math Library
- Regex for input validation

---

## 💻 Installation

### Clone the repository:
```bash
git clone https://github.com/simonMakumi/Calculator-App.git
```

### Install dependencies:
```bash
pip install pyqt5
```

### Run the app:
```bash
python main.py
```

### 📦 Packaging
You can package the app into an .exe using PyInstaller:
```bash
pyinstaller --noconfirm --windowed --icon=icon.ico main.py
```

### Notes:
- To ensure the icon displays correctly, test both with and without the --onefile flag.
- Make sure your icon.ico is a valid ICO file.


## ✨ Future Improvements
-Add theme switch (light/dark).
-Add calculation history.
-Add memory functions (M+, M-, MR).
-Further optimize packaging with tools like Nuitka for faster startup.

