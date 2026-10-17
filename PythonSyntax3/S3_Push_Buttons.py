from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Avengers Team")
window.resize(700, 400)
window.setStyleSheet("background-color: #FFF4E6;")

title = QLabel("Choose Your Avenger!", window)
title.setGeometry(150, 40, 400, 100)
title.setFont(QFont("Comic Sans MS", 22, QFont.Bold))
title.setStyleSheet("color: #5B4B8A;")
title.setAlignment(Qt.AlignCenter)

message = QLabel("Click a hero!", window)
message.setGeometry(200, 130, 300, 60)
message.setFont(QFont("Comic Sans MS", 18, QFont.Bold))
message.setStyleSheet("color: #6B5B73;")
message.setAlignment(Qt.AlignCenter)


def iron_man():
    message.setText("🔥 I am Iron Man!")
    window.setStyleSheet("background-color: #FFD6D6;")


def captain():
    message.setText("🛡️ Captain America!")
    window.setStyleSheet("background-color: #D6EAF8;")


def thor():
    message.setText("⚡ Thor is here!")
    window.setStyleSheet("background-color: #E6D9F2;")


iron_button = QPushButton("🔥 Iron Man", window)
iron_button.setGeometry(100, 250, 150, 60)
iron_button.setStyleSheet("background-color: #FFB5A7; border-radius: 15px;")
iron_button.clicked.connect(iron_man)

captain_button = QPushButton("🛡️ Captain", window)
captain_button.setGeometry(275, 250, 150, 60)
captain_button.setStyleSheet("background-color: #A9D6E5; border-radius: 15px;")
captain_button.clicked.connect(captain)

thor_button = QPushButton("⚡ Thor", window)
thor_button.setGeometry(450, 250, 150, 60)
thor_button.setStyleSheet("background-color: #CDB4DB; border-radius: 15px;")
thor_button.clicked.connect(thor)

window.show()
sys.exit(app.exec_())