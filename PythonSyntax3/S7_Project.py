import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Employee(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Employee Registration")
        self.setGeometry(500, 100, 450, 600)

        # Title
        title = QLabel("Employee Registration")
        title.setAlignment(Qt.AlignCenter)

        # Input Fields
        name = QLineEdit()
        name.setPlaceholderText("Enter Employee Name")

        email = QLineEdit()
        email.setPlaceholderText("Enter Email")

        phone = QLineEdit()
        phone.setPlaceholderText("Enter Phone Number")

        # Department
        department = QComboBox()
        department.addItems(["Select Department", "IT", "HR",
                             "Finance", "Marketing", "Sales"])

        # Gender
        male = QRadioButton("Male")
        female = QRadioButton("Female")
        other = QRadioButton("Other")

        gender = QHBoxLayout()
        gender.addWidget(male)
        gender.addWidget(female)
        gender.addWidget(other)

        # Address
        address = QTextEdit()
        address.setPlaceholderText("Enter Address")
        address.setFixedHeight(70)

        # Button
        button = QPushButton("Register Employee")
        message = QLabel("Fill in the details")
        message.setAlignment(Qt.AlignCenter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(name)
        layout.addWidget(email)
        layout.addWidget(phone)
        layout.addWidget(department)
        layout.addLayout(gender)
        layout.addWidget(address)
        layout.addWidget(button)
        layout.addWidget(message)

        self.setLayout(layout)

        # Style
        # self.setStyleSheet("""
        #     QWidget {
        #         background: #1e1e2f;
        #         color: white;
        #         font-size: 14px;
        #     }

        #     QLabel {
        #         color: white;
        #     }

        #     QLineEdit, QComboBox, QTextEdit {
        #         background: white;
        #         color: black;
        #         padding: 8px;
        #         border-radius: 5px;
        #     }

        #     QPushButton {
        #         background: #e63946;
        #         color: white;
        #         padding: 10px;
        #         border-radius: 6px;
        #         font-weight: bold;
        #     }

        #     QPushButton:hover {
        #         background: #ff6b6b;
        #     }
        # """)

        # title.setStyleSheet(
        #     "font-size: 24px; font-weight: bold; color: #ffd166;"
        # )

app = QApplication(sys.argv)
window = Employee()
window.show()

sys.exit(app.exec_())