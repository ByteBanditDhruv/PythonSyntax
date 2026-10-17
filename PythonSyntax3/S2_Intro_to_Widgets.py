from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QCheckBox, QRadioButton
)
from PyQt5.QtGui import QPixmap, QFont
import sys


class AvengersPortal(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Avengers Portal")
        self.resize(1300, 900)

        self.setStyleSheet("""
            QWidget {
                background-color: #101010;
                color: white;
            }

            QLabel {
                color: #FFD700;
            }

            QCheckBox, QRadioButton {
                color: white;
            }

            QLineEdit {
                background-color: white;
                color: black;
            }

            QPushButton {
                background-color: #E62429;
                color: white;
                padding: 10px;
                border-radius: 5px;
            }
        """)

        # TITLE
        self.title = QLabel("⚡ AVENGERS PORTAL ⚡", self)
        self.title.move(650, 30)

        self.title_font = QFont("Impact", 26)
        self.title.setFont(self.title_font)


        # IMAGE
        self.image = QLabel(self)

        self.pixmap = QPixmap(
            r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\PythonSyntax3\avengers.jpg"
        )

        self.pixmap = self.pixmap.scaled(1200, 650)

        self.image.setPixmap(self.pixmap)
        self.image.move(50, 100)


        # CHECKBOX
        self.avenger_label = QLabel("Choose Your Avengers:", self)
        self.avenger_label.move(1300, 100)
        self.avenger_label.setFont(QFont("Trebuchet MS", 15))

        self.ironman = QCheckBox("Iron Man", self)
        self.ironman.move(1300, 140)
        self.ironman.setFont(QFont("Trebuchet MS", 13))

        self.cap = QCheckBox("Captain America", self)
        self.cap.move(1300, 180)
        self.cap.setFont(QFont("Trebuchet MS", 13))

        self.spidy = QCheckBox("Spider-Man", self)
        self.spidy.move(1300, 220)
        self.spidy.setFont(QFont("Trebuchet MS", 13))

        self.hulk = QCheckBox("Hulk", self)
        self.hulk.move(1300, 260)
        self.hulk.setFont(QFont("Trebuchet MS", 13))


        # RADIO BUTTONS
        self.mission_label = QLabel("Choose Your Mission:", self)
        self.mission_label.move(1300, 330)
        self.mission_label.setFont(QFont("Trebuchet MS", 15))

        self.mission1 = QRadioButton("Save the City", self)
        self.mission1.move(1300, 370)
        self.mission1.setFont(QFont("Trebuchet MS", 13))

        self.mission2 = QRadioButton("Fight Villains", self)
        self.mission2.move(1300, 410)
        self.mission2.setFont(QFont("Trebuchet MS", 13))

        self.mission3 = QRadioButton("Save the World", self)
        self.mission3.move(1300, 450)
        self.mission3.setFont(QFont("Trebuchet MS", 13))


        # NAME
        self.name_label = QLabel("Avenger Name:", self)
        self.name_label.move(50, 800)
        self.name_label.setFont(QFont("Trebuchet MS", 15))

        self.name = QLineEdit(self)
        self.name.move(225, 800)
        self.name.setFont(QFont("Trebuchet MS", 13))


        # BUTTON
        self.button = QPushButton("START MISSION", self)
        self.button.move(1500, 520)
        self.button.setFont(QFont("Impact", 16))


# SHOW WINDOW

app = QApplication(sys.argv)

window = AvengersPortal()

window.showMaximized()

sys.exit(app.exec_())