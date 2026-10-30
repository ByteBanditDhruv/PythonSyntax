import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont

class Avengers(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Avengers Portal")
        self.resize(1300, 900)

        # self.setStyleSheet("""
        #     QWidget { background: #101010; color: white; }
        #     QLabel { color: #FFD700; }
        #     QLineEdit { background: white; color: black; }
        #     QPushButton {
        #         background: #E62429;
        #         color: white;
        #         padding: 10px;
        #         border-radius: 5px;
        #     }
        # """)

        # Title
        title = QLabel("⚡ AVENGERS PORTAL ⚡", self)
        title.move(500, 30)
        title.setFont(QFont("Impact", 26))

        # Image
        image = QLabel(self)
        image.setPixmap(QPixmap(
            r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\Python\PythonSyntax3\avengers.jpg"
        ).scaled(800, 400))
        image.move(50, 100)

        # Checkboxes
        label = QLabel("Choose Your Avengers:", self)
        label.move(900, 100)

        heroes = ["Iron Man", "Captain America", "Spider-Man", "Hulk"]

        for i, hero in enumerate(heroes):
            check = QCheckBox(hero, self)
            check.move(900, 140 + i * 40)

        # Radio Buttons
        mission = QLabel("Choose Your Mission:", self)
        mission.move(900, 330)

        missions = ["Save the City", "Fight Villains", "Save the World"]

        for i, text in enumerate(missions):
            radio = QRadioButton(text, self)
            radio.move(900, 370 + i * 40)

        # Name
        name_label = QLabel("Avenger Name:", self)
        name_label.move(50, 550)

        name = QLineEdit(self)
        name.move(200, 550)

        # Button
        button = QPushButton("START MISSION", self)
        button.move(900, 520)
        button.setFont(QFont("Impact", 16))


app = QApplication(sys.argv)
window = Avengers()
window.showMaximized()

sys.exit(app.exec_())