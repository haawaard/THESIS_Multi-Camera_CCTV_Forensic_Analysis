from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from .assets import icon, pixmap, asset_path
from .controller import DashboardController
from .theme import Theme, app_font
from .widgets import (
    CameraCard,
    CaseSelector,
    DecisionButton,
    DetailRow,
    HeaderButton,
    PanelFrame,
    PillLabel,
    SegmentedToggle,
    TableWidget,
    TimelinePanel,
    VideoPlayer,
)


class ForensikadaWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Forensikada")
        self.setMinimumSize(1360, 900)
        self.resize(1600, 1000)
        self.controller = DashboardController()
        self.controller.state_changed.connect(self.refresh_state)
        self._build_ui()
        self.refresh_state()

    def _build_ui(self) -> None:
        root = QWidget()
        self.setCentralWidget(root)
        grid = QGridLayout(root)
        grid.setContentsMargins(10, 10, 10, 10)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(10)
        grid.setRowStretch(1, 1)
        grid.setRowStretch(2, 0)
        grid.setColumnStretch(1, 1)

        self.header = self._build_header()
        grid.addWidget(self.header, 0, 0, 1, 3)

        self.left_panel = self._build_left_panel()
        grid.addWidget(self.left_panel, 1, 0)

        self.center_panel = self._build_center_panel()
        grid.addWidget(self.center_panel, 1, 1)

        self.right_panel = self._build_right_panel()
        grid.addWidget(self.right_panel, 1, 2)

        self.timeline_panel = self._build_timeline_panel()
        grid.addWidget(self.timeline_panel, 2, 0, 1, 3)

        grid.setColumnMinimumWidth(0, 338)
        grid.setColumnMinimumWidth(2, 453)

        self.setStyleSheet(
            f"""
            QWidget {{
                font-family: "{Theme.FONT_FAMILY}";
                color: {Theme.TEXT};
            }}
            QMainWindow {{
                background: {Theme.WINDOW_BG};
            }}
            QFrame#panelFrame {{
                background: {Theme.PANEL_BG};
                border: 1px solid {Theme.PANEL_BORDER};
            }}
            QPushButton {{
                background: {Theme.PANEL_BG};
                border: 1px solid rgba(255,255,255,0.8);
                border-radius: 10px;
                color: white;
                padding: 6px 12px;
            }}
            QPushButton[selected="true"] {{
                background: #f5f5f5;
                border: 1px solid {Theme.PRIMARY_BLUE};
                color: {Theme.PRIMARY_BLUE};
            }}
            QListWidget {{
                border: none;
                background: transparent;
            }}
            QListWidget::item {{
                border: none;
            }}
            QLineEdit, QTextEdit {{
                border: 1px solid rgba(0,0,0,0.2);
                border-radius: 10px;
                padding: 8px 10px;
                background: white;
            }}
            """
        )

    def _build_header(self) -> QWidget:
        frame = PanelFrame()
        frame.setFixedHeight(72)
        frame.setStyleSheet(f"background: {Theme.DARK_BAR};")
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(10)

        logo = QLabel()
        logo.setFixedSize(58, 58)
        logo.setPixmap(pixmap("logo.png").scaled(58, 58, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        layout.addWidget(logo)

        title_col = QVBoxLayout()
        title_col.setSpacing(0)
        title = QLabel("Forensikada")
        title.setFont(app_font(14, QFont.Weight.Medium))
        title.setStyleSheet("color: white;")
        subtitle = QLabel("Multi-Camera CCTV Forensic Anayalysis")
        subtitle.setFont(app_font(8, QFont.Weight.Light))
        subtitle.setStyleSheet("color: white;")
        title_col.addWidget(title)
        title_col.addWidget(subtitle)
        layout.addLayout(title_col)

        layout.addSpacing(24)

        self.case_selector = CaseSelector()
        self.case_selector.setStyleSheet(
            f"QPushButton{{background:{Theme.DARK_BAR_2}; color:white; border:1px solid white; border-radius:2px; text-align:left; padding-left:14px;}}"
        )
        self.case_selector.clicked.connect(self.controller.toggle_case)
        layout.addWidget(self.case_selector)

        layout.addStretch(1)

        for text, icon_name in [("Import Video", "opened_folder.png"), ("Run Analysis", "run_analysis.svg"), ("Generate Report", "generate_report.svg")]:
            btn = HeaderButton(text, icon_name)
            btn.setStyleSheet(
                f"QPushButton{{background:{Theme.DARK_BAR}; color:white; border:1px solid white; border-radius:10px; text-align:left; padding-left:12px;}}"
            )
            layout.addWidget(btn)

        settings = QLabel()
        settings.setFixedSize(30, 30)
        settings.setPixmap(icon("settings.svg").pixmap(30, 30))
        layout.addWidget(settings)
        return frame

    def _build_left_panel(self) -> QWidget:
        frame = PanelFrame()
        frame.setFixedWidth(338)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(12)

        self.camera_list = QListWidget()
        self.camera_list.setSpacing(10)
        self.camera_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        layout.addWidget(QLabel("CAMERAS"))
        layout.addWidget(self.camera_list)

        layout.addWidget(QLabel("VIEW MODE"))
        self.view_toggle = SegmentedToggle("Original", "Enhanced", "Enhanced")
        layout.addWidget(self.view_toggle)

        layout.addSpacing(6)
        layout.addWidget(QLabel("ANALYSIS STATUS"))
        self.analysis_status = QFrame()
        self.analysis_status.setFixedHeight(81)
        self.analysis_status.setStyleSheet("background:white; border: 1px solid rgba(0,0,0,0.2); border-radius:10px;")
        self.analysis_status_layout = QVBoxLayout(self.analysis_status)
        self.analysis_status_layout.setContentsMargins(14, 10, 14, 10)
        self.analysis_status_layout.setSpacing(2)
        layout.addWidget(self.analysis_status)
        layout.addStretch(1)
        return frame

    def _build_center_panel(self) -> QWidget:
        frame = PanelFrame()
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(10)
        self.video_player = VideoPlayer()
        layout.addWidget(self.video_player)

        label = QLabel("RECENT OBJECT OBSERVATION")
        label.setFont(app_font(12, QFont.Weight.DemiBold))
        layout.addWidget(label)

        self.observation_table = TableWidget()
        layout.addWidget(self.observation_table, 1)
        return frame

    def _build_right_panel(self) -> QWidget:
        frame = PanelFrame()
        frame.setFixedWidth(453)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(10)

        layout.addWidget(QLabel("OBSERVATION DETAILS"))
        self.detail_panel = QWidget()
        detail_layout = QVBoxLayout(self.detail_panel)
        detail_layout.setContentsMargins(0, 0, 0, 0)
        detail_layout.setSpacing(3)
        layout.addWidget(self.detail_panel)

        self.validation_row = QWidget()
        validation_layout = QHBoxLayout(self.validation_row)
        validation_layout.setContentsMargins(0, 0, 0, 0)
        validation_layout.setSpacing(4)
        layout.addWidget(self.validation_row)

        layout.addWidget(QLabel("ANALYST DECISION"))
        decision_row = QHBoxLayout()
        decision_row.setSpacing(10)
        self.accept_btn = DecisionButton("Accept\nObservation", "check_circle_outline.svg", Theme.SUCCESS, Theme.SUCCESS)
        self.uncertain_btn = DecisionButton("Mark\nUncertain", "warning.svg", Theme.WARNING, Theme.WARNING)
        self.reject_btn = DecisionButton("Reject\nDetection", "error.svg", Theme.DANGER, Theme.DANGER)
        decision_row.addWidget(self.accept_btn)
        decision_row.addWidget(self.uncertain_btn)
        decision_row.addWidget(self.reject_btn)
        layout.addLayout(decision_row)

        layout.addWidget(QLabel("ANALYST NOTES"))
        self.notes_box = QWidget()
        notes_layout = QVBoxLayout(self.notes_box)
        notes_layout.setContentsMargins(0, 0, 0, 0)
        notes_layout.setSpacing(8)
        self.notes_edit = QLabel()
        self.notes_edit.setWordWrap(True)
        self.notes_edit.setFixedHeight(67)
        self.notes_edit.setStyleSheet("border:1px solid rgba(0,0,0,0.2); border-radius:10px; padding: 8px 10px; color: rgba(0,0,0,0.3); background: white;")
        notes_layout.addWidget(self.notes_edit)
        warn = QFrame()
        warn.setStyleSheet("background:#fef9e8; border:1px solid rgba(0,0,0,0.2); border-radius:10px;")
        warn.setFixedHeight(91)
        warn_layout = QHBoxLayout(warn)
        warn_layout.setContentsMargins(14, 12, 14, 12)
        warn_layout.setSpacing(10)
        self.warning_icon = QLabel()
        self.warning_icon.setFixedSize(24, 24)
        warn_layout.addWidget(self.warning_icon, 0, Qt.AlignmentFlag.AlignTop)
        self.warning_text = QLabel()
        self.warning_text.setWordWrap(True)
        warn_layout.addWidget(self.warning_text, 1)
        notes_layout.addWidget(warn)
        layout.addWidget(self.notes_box)
        layout.addStretch(1)
        return frame

    def _build_timeline_panel(self) -> QWidget:
        frame = PanelFrame()
        frame.setFixedHeight(184)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(10)
        self.timeline_panel = TimelinePanel()
        layout.addWidget(self.timeline_panel)
        return frame

    def refresh_state(self) -> None:
        state = self.controller.state
        self.case_selector.set_case_name(state.case_name)
        self.video_player.title.setText(state.title)
        self.view_toggle.set_selected(state.active_view_mode)

        self.camera_list.clear()
        for item in state.camera_items:
            list_item = QListWidgetItem()
            widget = CameraCard(item.title, item.subtitle, item.status, item.selected)
            list_item.setSizeHint(widget.sizeHint())
            self.camera_list.addItem(list_item)
            self.camera_list.setItemWidget(list_item, widget)

        self.analysis_status_layout.takeAt(0)
        while self.analysis_status_layout.count():
            child = self.analysis_status_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        if state.analysis_summary and not state.empty:
            green = QLabel(state.analysis_summary[0])
            green.setFont(app_font(8, QFont.Weight.DemiBold))
            green.setStyleSheet("color:#11651d;")
            self.analysis_status_layout.addWidget(green)
            for line in state.analysis_summary[1:]:
                lab = QLabel(line)
                lab.setFont(app_font(8))
                self.analysis_status_layout.addWidget(lab)
        else:
            self.analysis_status_layout.addStretch(1)

        self.observation_table.set_rows(state.observation_rows)

        detail_layout = self.detail_panel.layout()
        while detail_layout.count():
            child = detail_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for detail in state.details:
            detail_layout.addWidget(DetailRow(detail.label, detail.value, Theme.DANGER if detail.label == "Review Status" and not state.empty else Theme.TEXT))

        validation_layout = self.validation_row.layout()
        while validation_layout.count():
            child = validation_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for text, bg, fg in state.validation_tags:
            validation_layout.addWidget(PillLabel(text, bg, fg))

        self.notes_edit.setText(state.analyst_note or "")
        self.warning_text.setText(state.analyst_warning or "")
        self.warning_icon.setPixmap(icon("warning.svg").pixmap(24, 24))

