from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Avengers Team")
window.resize(700, 400)

# Title
title = QLabel("Choose Your Avenger!", window)
title.setGeometry(150, 40, 400, 60)
title.setAlignment(Qt.AlignCenter)

# Message
message = QLabel("Click a hero!", window)
message.setGeometry(200, 130, 300, 60)
message.setAlignment(Qt.AlignCenter)

# Functions
def iron_man():
    message.setText("I am Iron Man!")
    window.setStyleSheet("background: #FFD6D6;")

def captain():
    message.setText("Captain America!")
    window.setStyleSheet("background: #D6EAF8;")

def thor():
    message.setText("Thor is here!")
    window.setStyleSheet("background: #E6D9F2;")

# Buttons
b1 = QPushButton("Iron Man", window)
b1.setGeometry(100, 250, 150, 60)
b1.clicked.connect(iron_man)

b2 = QPushButton("Captain", window)
b2.setGeometry(275, 250, 150, 60)
b2.clicked.connect(captain)

b3 = QPushButton("Thor", window)
b3.setGeometry(450, 250, 150, 60)
b3.clicked.connect(thor)

window.show()
sys.exit(app.exec_())