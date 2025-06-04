from dataclasses import dataclass
from typing import Tuple

@dataclass
class Theme:
    background_color: str = "white"
    font: str = "DejaVu Sans"
    font_size: int = 20
    text_color: str = "black"

    def as_mpl_kwargs(self) -> dict:
        return {
            "fontname": self.font,
            "fontsize": self.font_size,
            "color": self.text_color,
        }
