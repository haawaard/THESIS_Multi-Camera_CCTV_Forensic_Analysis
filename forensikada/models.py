from dataclasses import dataclass, field
from typing import List


@dataclass
class CameraItem:
    title: str
    subtitle: str
    status: str
    selected: bool = False


@dataclass
class ObservationRow:
    selected: bool
    object_name: str
    object_icon: str
    camera: str
    timestamp: str
    confidence: str
    cross_camera: str
    validation_status: str


@dataclass
class ObservationDetail:
    label: str
    value: str


@dataclass
class DashboardState:
    case_name: str
    title: str
    camera_items: List[CameraItem] = field(default_factory=list)
    observation_rows: List[ObservationRow] = field(default_factory=list)
    details: List[ObservationDetail] = field(default_factory=list)
    validation_tags: List[tuple[str, str, str]] = field(default_factory=list)
    analyst_note: str = ""
    analyst_warning: str = ""
    analysis_summary: List[str] = field(default_factory=list)
    active_camera_label: str = ""
    active_view_mode: str = "Enhanced"
    empty: bool = False
