import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QMessageBox
)

app = QApplication(sys.argv)    

# Window
window = QWidget()
window.setWindowTitle("Avengers Mission")
window.setGeometry(650, 300, 500, 300)
window.setStyleSheet("background-color: #FFF8DC;")

# Button
button = QPushButton("Start Mission", window)
button.setGeometry(40, 100, 200, 60)

# Button Style
button.setStyleSheet("""
    QPushButton {
        background-color: #F4C430;
        color: #4A3B0A;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #FFD966;
    }
""")

button2 = QPushButton("Warning", window)
button2.setGeometry(260, 100, 200, 60)

# Button Style
# button2.setStyleSheet("""
#     QPushButton {
#         background-color: #F4C430;
#         color: #4A3B0A;
#         font-size: 18px;
#         font-weight: bold;
#         border-radius: 10px;
#     }
#     QPushButton:hover {
#         background-color: #FFD966;
#     }
# """)

# Function
def show_dialog():
    QMessageBox.information(
        window,
        "Avengers Mission",
        "⚡ Your mission is ready!\nThe Avengers are assembling!"
    )   

def show_dialog2():
    QMessageBox.warning(
        window,
        "Warning!",
        "Thanos is approaching!"
    )

# Connect Button
button.clicked.connect(show_dialog)
button2.clicked.connect(show_dialog2)

# Show Window
window.show()

sys.exit(app.exec_())

# QMessageBox.information()  # Information
# QMessageBox.warning()      # Warning
# QMessageBox.critical()     # Error
# QMessageBox.question()     # Ask a question