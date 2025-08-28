import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QLinearGradient, QPainter, QBrush, QColor

class BaseWindow(QMainWindow):
    """Superclass for geometric effects (gradient, animations)."""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 with Geometric Effects")
        self.setGeometry(100, 100, 800, 600)
        self._init_effects()

    def _init_effects(self):
        """Set up common visual effects."""
        # Gradient Background
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #4a00e0, stop:1 #8e2de2
                );
                color: white;
            }
        """)
        # Animation (rotating central widget)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self._setup_animation()

    def _setup_animation(self):
        """Rotate the central widget for a geometric effect."""
        self.animation = QPropertyAnimation(self.central_widget, b"pos")
        self.animation.setDuration(3000)  # 3 seconds
        self.animation.setLoopCount(-1)  # Infinite loop
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setEndValue(QPoint(50, 50))
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start()

    def paintEvent(self, event):
        """Optional: Custom paint for advanced effects."""
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor("#4a00e0"))
        gradient.setColorAt(1.0, QColor("#8e2de2"))
        painter.fillRect(self.rect(), QBrush(gradient))

class MainWindow(BaseWindow):
    """Subclass for app-specific logic (inherits effects from BaseWindow)."""
    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("HARIKA", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(self.label)
        self.central_widget.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
