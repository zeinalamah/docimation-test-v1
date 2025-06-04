from dataclasses import dataclass

@dataclass
class Camera:
    """Simple camera controlling zoom and position."""
    x: float = 0.0
    y: float = 0.0
    zoom: float = 1.0

    def move_to(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def set_zoom(self, zoom: float) -> None:
        self.zoom = zoom
