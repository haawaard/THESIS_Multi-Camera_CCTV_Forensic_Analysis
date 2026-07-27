from PyQt6.QtCore import QObject, pyqtSignal

from .data import empty_dashboard_state, sample_dashboard_state
from .models import DashboardState


class DashboardController(QObject):
    state_changed = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self._states = {
            "sample": sample_dashboard_state(),
            "empty": empty_dashboard_state(),
        }
        self._active_key = "sample"

    @property
    def state(self) -> DashboardState:
        return self._states[self._active_key]

    @property
    def active_key(self) -> str:
        return self._active_key

    def set_active_key(self, key: str) -> None:
        if key not in self._states:
            return
        if key == self._active_key:
            return
        self._active_key = key
        self.state_changed.emit()

    def toggle_case(self) -> None:
        self.set_active_key("empty" if self._active_key == "sample" else "sample")
