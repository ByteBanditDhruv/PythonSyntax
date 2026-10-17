import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit,
    QHBoxLayout, QVBoxLayout, QGroupBox
)
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# Main Window
window = QWidget()
window.setWindowTitle("Avengers Layout Demo")
window.setGeometry(400, 200, 700, 400)
window.setStyleSheet("""
    QWidget {
        background-color: #1e1e2f;
        color: white;
        font-size: 14px;
    }
    QGroupBox {
        border: 2px solid #555;
        border-radius: 10px;
        margin-top: 10px;
        padding: 15px;
    }
    QLineEdit {
        background-color: white;
        color: black;
        padding: 6px;
        border-radius: 5px;
    }
    QPushButton {
        background-color: #e63946;
        color: white;
        padding: 8px 15px;
        border-radius: 6px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #ff6b6b;
    }
""")

# Main Title
title = QLabel("⚡ AVENGERS HERO SELECTOR ⚡")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffd166;")

# ---------------- HORIZONTAL SECTION ----------------

horizontal_box = QGroupBox("QHBoxLayout - Horizontal")

name1 = QLineEdit()
name1.setPlaceholderText("Enter Hero Name")

power1 = QLineEdit()
power1.setPlaceholderText("Enter Superpower")

button1 = QPushButton("Select")

horizontal_layout = QHBoxLayout()
horizontal_layout.addWidget(name1)
horizontal_layout.addWidget(power1)
horizontal_layout.addWidget(button1)

horizontal_box.setLayout(horizontal_layout)

# ---------------- VERTICAL SECTION ----------------

vertical_box = QGroupBox("QVBoxLayout - Vertical")

name2 = QLineEdit()
name2.setPlaceholderText("Enter Hero Name")

power2 = QLineEdit()
power2.setPlaceholderText("Enter Superpower")

button2 = QPushButton("Select")

vertical_layout = QVBoxLayout()
vertical_layout.addWidget(name2)
vertical_layout.addWidget(power2)
vertical_layout.addWidget(button2)

vertical_box.setLayout(vertical_layout)

# ---------------- MAIN LAYOUT ----------------

main_layout = QVBoxLayout()

main_layout.addWidget(title)
main_layout.addWidget(horizontal_box)
main_layout.addWidget(vertical_box)

window.setLayout(main_layout)

window.show()
sys.exit(app.exec_())