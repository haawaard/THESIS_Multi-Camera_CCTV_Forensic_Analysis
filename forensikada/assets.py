from pathlib import Path

from PyQt6.QtGui import QIcon, QPixmap


BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"


def asset_path(name: str) -> Path:
    return ASSET_DIR / name


def icon(name: str) -> QIcon:
    path = asset_path(name)
    return QIcon(str(path)) if path.exists() else QIcon()


def pixmap(name: str) -> QPixmap:
    path = asset_path(name)
    return QPixmap(str(path))
