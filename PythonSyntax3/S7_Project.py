import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox,
    QRadioButton, QHBoxLayout, QTextEdit
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# Main Window
window = QWidget()
window.setWindowTitle("Employee Registration")
window.setGeometry(500, 100, 450, 650)

# -----------------------------
# Profile Avatar
# -----------------------------
avatar = QLabel()
pixmap = QPixmap(r"C:\Users\OMOLP247\OneDrive\Desktop\dhruv\PythonSyntax3\businessman-character-avatar-isolated.png")
avatar.setPixmap(pixmap.scaled(
    100, 100,
    Qt.KeepAspectRatio,
    Qt.SmoothTransformation
))
avatar.setAlignment(Qt.AlignCenter)

# -----------------------------
# Title
# -----------------------------
title = QLabel("Employee Registration")
title.setAlignment(Qt.AlignCenter)

# -----------------------------
# Input Fields
# -----------------------------
name = QLineEdit()
name.setPlaceholderText("Enter Employee Name")  

email = QLineEdit()
email.setPlaceholderText("Enter Email Address")

phone = QLineEdit()
phone.setPlaceholderText("Enter Phone Number")

# -----------------------------
# Department ComboBox
# -----------------------------
department = QComboBox()
department.addItems([
    "Select Department",
    "IT",
    "HR",
    "Finance",
    "Marketing",
    "Sales"
])

# -----------------------------
# Gender Radio Buttons
# -----------------------------
gender_label = QLabel("Select Gender:")

male = QRadioButton("Male")
female = QRadioButton("Female")
other = QRadioButton("Other")

gender_layout = QHBoxLayout()
gender_layout.addWidget(male)
gender_layout.addWidget(female)
gender_layout.addWidget(other)

# -----------------------------
# Address
# -----------------------------
address = QTextEdit()
address.setPlaceholderText("Enter Address")
address.setFixedHeight(70)

# -----------------------------
# Register Button
# -----------------------------
register_button = QPushButton("Register Employee")

message = QLabel("Fill in the details and click Register")
message.setAlignment(Qt.AlignCenter)

# -----------------------------
# Main Vertical Layout
# -----------------------------
layout = QVBoxLayout()

layout.addWidget(avatar)
layout.addWidget(title)
layout.addWidget(name)
layout.addWidget(email)
layout.addWidget(phone)
layout.addWidget(department)
layout.addWidget(gender_label)
layout.addLayout(gender_layout)
layout.addWidget(address)
layout.addWidget(register_button)
layout.addWidget(message)

# -----------------------------
# Styling
# -----------------------------
window.setStyleSheet("""
    QWidget {
        background-color: #1e1e2f;
        color: white;
        font-size: 14px;
    }

    QLabel {
        font-size: 14px;
    }

    QLabel#title {
        font-size: 24px;
        font-weight: bold;
        color: #ffd166;
    }

    QLineEdit, QComboBox, QTextEdit {
        background-color: white;
        color: black;
        padding: 8px;
        border-radius: 5px;
    }

    QPushButton {
        background-color: #e63946;
        color: white;
        padding: 10px;
        border-radius: 6px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #ff6b6b;
    }
""")

title.setObjectName("title")

window.setLayout(layout)
window.show()

sys.exit(app.exec_())