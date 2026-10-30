import sys
from PyQt5.QtWidgets import *

class Avengers(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Avengers Mission")
        self.setGeometry(500, 300, 500, 300)
        self.setStyleSheet("background: #FFF8DC;")

        # Buttons
        self.b1 = QPushButton("Start Mission", self)
        self.b1.setGeometry(40, 100, 200, 60)

        self.b2 = QPushButton("Warning", self)
        self.b2.setGeometry(260, 100, 200, 60)

        # Button Color
        self.b1.setStyleSheet("background: #F4C430;")
        self.b2.setStyleSheet("background: #F4C430;")

        # Connect Buttons
        self.b1.clicked.connect(self.mission)
        self.b2.clicked.connect(self.warning)

    # Functions
    def mission(self):
        QMessageBox.information(self, "Mission", "Avengers are assembling!")

    def warning(self):
        QMessageBox.warning(self, "Warning", "Thanos is approaching!")


app = QApplication(sys.argv)
window = Avengers()
window.show()

sys.exit(app.exec_())