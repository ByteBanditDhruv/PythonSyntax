import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit,
    QHBoxLayout, QVBoxLayout, QGroupBox
)
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Avengers Hero Selector")
window.setGeometry(400, 200, 700, 400)

window.setStyleSheet("""
    QWidget { background: #1e1e2f; color: white; }
    QLineEdit { background: white; color: black; padding: 6px; }
    QPushButton { background: #e63946; padding: 8px; }
    QGroupBox { border: 2px solid #555; padding: 10px; }
""")

title = QLabel("⚡ AVENGERS HERO SELECTOR ⚡")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("font-size: 24px; color: #ffd166;")

# Horizontal Layout
hbox = QGroupBox("Horizontal Layout")
h = QHBoxLayout()
h.addWidget(QLineEdit("Enter Hero Name"))
h.addWidget(QLineEdit("Enter Superpower"))
h.addWidget(QPushButton("Select"))
hbox.setLayout(h)

# Vertical Layout
vbox = QGroupBox("Vertical Layout")
v = QVBoxLayout()
v.addWidget(QLineEdit("Enter Hero Name"))
v.addWidget(QLineEdit("Enter Superpower"))
v.addWidget(QPushButton("Select"))
vbox.setLayout(v)

# Main Layout
layout = QVBoxLayout()
layout.addWidget(title)
layout.addWidget(hbox)
layout.addWidget(vbox)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())