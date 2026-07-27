from .models import CameraItem, DashboardState, ObservationDetail, ObservationRow


def sample_dashboard_state() -> DashboardState:
    return DashboardState(
        case_name="CASE-2026-014",
        title="CAM-01 • Main Entrance",
        active_camera_label="CAM-01 • Main Entrance",
        active_view_mode="Enhanced",
        camera_items=[
            CameraItem("CAM-01", "Main Entrance", "green", True),
            CameraItem("CAM-02", "Checkout Area", "green", False),
            CameraItem("CAM-03", "Hallway", "green", False),
        ],
        observation_rows=[
            ObservationRow(True, "Mobile Phone", "phone", "CAM-01", "14:32:12.420", "90%", "CAM-02 Match", ""),
            ObservationRow(False, "Bag", "bag", "CAM-01", "14:32:08.120", "94%", "CAM-02 Match", ""),
            ObservationRow(False, "Knife", "knife", "CAM-03", "14:33:05.670", "67%", "Single View", ""),
            ObservationRow(False, "Handgun", "gun", "CAM-02", "14:31:55.213", "92%", "CAM-01, CAM-03", ""),
        ],
        details=[
            ObservationDetail("Object Class", "Mobile Phone"),
            ObservationDetail("Confidence", "86%"),
            ObservationDetail("Camera", "CAM-01"),
            ObservationDetail("Frame", "45,723"),
            ObservationDetail("Timestamp", "2026-07-18 14:32:12.480"),
            ObservationDetail("Bounding Box", "[412, 158, 468, 249]"),
            ObservationDetail("Source", "Enhanced Footage"),
            ObservationDetail("Temporal Support", "7 consecutive frames"),
            ObservationDetail("Cross-Camera Status", "Corroborated by CAM-02"),
            ObservationDetail("Review Status", "Pending Analyst Review"),
        ],
        validation_tags=[
            ("High Confidence", "#b6e8b3", "#427432"),
            ("Temporarily Supported", "#98afe3", "#324574"),
            ("Cross-Camera Corroborated", "#d8aadd", "#74326e"),
        ],
        analyst_note="Enter notes about this observation...",
        analyst_warning="Automated observations require human review and do not establish that a crime occurred.",
        analysis_summary=["Processing Complete", "All videos analyzed", "3 cameras • 01:42:82 total"],
    )


def empty_dashboard_state() -> DashboardState:
    return DashboardState(
        case_name="",
        title="No Camera Detected • -",
        active_camera_label="No Camera Detected • -",
        active_view_mode="Enhanced",
        camera_items=[CameraItem("No Camera Detected", "-", "red", True)],
        observation_rows=[],
        details=[
            ObservationDetail("Object Class", "-"),
            ObservationDetail("Confidence", "-"),
            ObservationDetail("Camera", "-"),
            ObservationDetail("Frame", "-"),
            ObservationDetail("Timestamp", "-"),
            ObservationDetail("Bounding Box", "-"),
            ObservationDetail("Source", "-"),
            ObservationDetail("Temporal Support", "-"),
            ObservationDetail("Cross-Camera Status", "-"),
            ObservationDetail("Review Status", "-"),
        ],
        validation_tags=[
            ("High Confidence", "#b6e8b3", "#427432"),
            ("Temporarily Supported", "#98afe3", "#324574"),
            ("Cross-Camera Corroborated", "#d8aadd", "#74326e"),
        ],
        analyst_note="Enter notes about this observation...",
        analyst_warning="Automated observations require human review and do not establish that a crime occurred.",
        analysis_summary=["", "", ""],
        empty=True,
    )
