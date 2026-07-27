from PyQt6.QtGui import QFont


class Theme:
    WINDOW_BG = "#f4f4f4"
    PANEL_BG = "#ffffff"
    PANEL_BORDER = "rgba(0, 0, 0, 0.2)"
    DARK_BAR = "#303841"
    DARK_BAR_2 = "#2d3237"
    DARK_BAR_3 = "#2b3238"
    TEXT = "#000000"
    MUTED = "rgba(0, 0, 0, 0.3)"
    PRIMARY_BLUE = "#2f318e"
    SUCCESS = "#427432"
    SUCCESS_BG = "#b6e8b3"
    WARNING = "#c8a724"
    WARNING_BG = "#fef9e8"
    PURPLE = "#74326e"
    PURPLE_BG = "#d8aadd"
    INFO = "#324574"
    INFO_BG = "#98afe3"
    DANGER = "#e44d4d"
    DANGER_BG = "#f8e0e0"
    TABLE_TEXT = "#191919"
    TABLE_GREEN = "#48742c"

    FONT_FAMILY = "Inter"


def app_font(size: int, weight: QFont.Weight = QFont.Weight.Normal) -> QFont:
    font = QFont(Theme.FONT_FAMILY, size)
    font.setWeight(weight)
    return font
