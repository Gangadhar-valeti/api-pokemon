import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QPoint
from PyQt5.QtGui import QLinearGradient, QPainter, QBrush, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 with Geometric Effects")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget (QLabel) to demonstrate effects
        self.central_label = QLabel(self)
        self.central_label.setAlignment(Qt.AlignCenter)
        self.central_label.setText("Geometric Effects Demo")
        self.central_label.setStyleSheet("font-size: 24px; color: #545333;")
        self.setCentralWidget(self.central_label)

        # Create a simple gradient background using QPalette (or override `paintEvent`)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #4a00e0, stop:1 #8e2de2
                );
                color: white;
            }
        """)

    def paintEvent(self, event):
        # Optional: Override paintEvent for more custom gradient effects
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(1.0, QColor("#F5162C"))
        gradient.setColorAt(0.5, QColor("#07770b"))
        painter.fillRect(self.rect(), QBrush(gradient))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
