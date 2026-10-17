import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread

# 1. Define the Pygame Game Logic in a QThread
class GameThread(QThread):
    def run(self):
        # Initialize Pygame components
        pygame.init()
        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_set_caption("Pygame Window Launched from PyQt5")
        clock = pygame.time.Clock()
        
        running = True
        while running:
            # Handle Pygame background color
            screen.fill((40, 44, 52)) 
            
            # Handle Pygame user input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Refresh screen and cap frame rate
            pygame.display.flip()
            clock.tick(60)
            
        pygame.quit()

# 2. Build the Main PyQt5 App Launcher Window
class LauncherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Launcher Menu")
        self.setGeometry(100, 100, 300, 200)
        
        # Build layout with a start button
        layout = QVBoxLayout()
        self.start_button = QPushButton("Start Pygame Game")
        self.start_button.clicked.connect(self.launch_game)
        layout.addWidget(self.start_button)
        
        # Display central widget container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # Placeholder reference variable for our background worker thread
        self.game_thread = None

    def launch_game(self):
        # Prevent spinning multiple game processes concurrently
        if self.game_thread is None or not self.game_thread.isRunning():
            self.game_thread = GameThread()
            self.game_thread.start()

# 3. Standard Application Execution Initialization
if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = LauncherWindow()
    launcher.show()
    sys.exit(app.exec_())
