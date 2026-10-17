# import sys
# from PyQt5.QtWidgets import QApplication, QWidget

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("My First App")
# window.resize(400, 300)

# window.show()

# sys.exit(app.exec_())

## Adding our First Widget
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("My First App")
# window.resize(400, 300)

# label = QLabel("Hello, Students!", window)
# label.move(150, 130)

# window.show()

# sys.exit(app.exec_())

## Adding a Button
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("My First App")
# window.resize(400, 300)

# label = QLabel("Hello Captain!", window)
# label.move(170, 80)

# button = QPushButton("Click Me", window)
# button.move(150, 150)

# window.show()

# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Space Mission")
window.resize(400, 300)

label1 = QLabel("🚀 SPACE MISSION", window)
label1.move(130, 30)
label1.setStyleSheet("font-size: 24px; font-weight: bold; color: blue")

label2 = QLabel("Mission Control", window)
label2.move(150, 70)

label3 = QLabel("Choose an action:", window)
label3.move(140, 110)

button1 = QPushButton("Launch 🚀", window)
button1.move(140, 140)

button2 = QPushButton("Check Fuel", window)
button2.move(140, 175)

button3 = QPushButton("Check Map", window)
button3.move(140, 210)

button4 = QPushButton("Return to Earth 🌍", window)
button4.move(128, 245)

window.show()

sys.exit(app.exec_())
