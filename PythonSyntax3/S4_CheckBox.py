import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QCheckBox, QComboBox, QPushButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Avengers Hero Selector")
window.setGeometry(500, 300, 600, 450)

# Title
title = QLabel("Avengers Hero Selector", window)
title.setGeometry(100, 30, 400, 50)

# Checkbox
check = QCheckBox("I am an Avengers Fan!", window)
check.setGeometry(180, 100, 250, 40)

# Dropdown
label = QLabel("Choose your favorite hero:", window)
label.setGeometry(170, 150, 300, 30)

combo = QComboBox(window)
combo.addItems(["Iron Man", "Thor", "Hulk", "Captain America"])
combo.setGeometry(150, 190, 300, 40)

# Button
button = QPushButton("Assemble!", window)
button.setGeometry(200, 260, 200, 50)

# Result
result = QLabel("", window)
result.setGeometry(50, 330, 500, 40)

# Function
def assemble():
    if check.isChecked():
        result.setText(combo.currentText() + " is ready to fight!")
    else:
        result.setText("Become an Avengers Fan first!")

button.clicked.connect(assemble)

window.show()
sys.exit(app.exec_())