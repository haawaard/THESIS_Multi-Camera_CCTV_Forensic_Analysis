import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

from .theme import Theme
from .window import ForensikadaWindow


def run() -> None:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QFont(Theme.FONT_FAMILY, 10))
    window = ForensikadaWindow()
    window.show()
    sys.exit(app.exec())
