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
window.setGeometry(650, 300, 600, 450)

title = QLabel("Avengers Hero Selector", window)
title.setFont(QFont("Arial", 24, QFont.Bold))
title.setAlignment(Qt.AlignCenter)
title.setGeometry(50, 30, 500, 50)

subtitle = QLabel("Choose your favorite hero!", window)
subtitle.setFont(QFont("Arial", 14))
subtitle.setAlignment(Qt.AlignCenter)
subtitle.setGeometry(50, 85, 500, 30)

checkbox = QCheckBox("I am an Avengers Fan!", window)
checkbox.setGeometry(180, 135, 250, 40)

label = QLabel("Choose your favorite Avenger:", window)
label.setGeometry(170, 185, 300, 30)

combo = QComboBox(window)
combo.addItems([
    "Iron Man",
    "Captain America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Spider-Man"
])
combo.setGeometry(150, 220, 300, 40)

button = QPushButton("Assemble!", window)
button.setGeometry(200, 285, 200, 50)

result = QLabel("", window)
result.setAlignment(Qt.AlignCenter)
result.setGeometry(50, 355, 500, 40)

def assemble():
    hero = combo.currentText()

    if checkbox.isChecked():
        result.setText(hero + " is ready to fight!")

    else:
        result.setText("Become an Avengers Fan first!") 

button.clicked.connect(assemble)

window.show()

sys.exit(app.exec_())