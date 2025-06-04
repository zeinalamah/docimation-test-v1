from dataclasses import dataclass, field
from typing import List, Tuple
from io import BytesIO
import re

import matplotlib.pyplot as plt
from PIL import Image

from theming.theme import Theme

Segment = Tuple[str, str]


@dataclass
class Page:
    width: int = 1280
    height: int = 720
    theme: Theme = field(default_factory=Theme)
    segments: List[Segment] = field(default_factory=list)
    images: List[Tuple[Image.Image, Tuple[float, float], float]] = field(default_factory=list)

    def add_segment(self, segment: Segment) -> None:
        self.segments.append(segment)

    def add_image(
        self, img: Image.Image, position: Tuple[float, float] = (0.5, 0.5), scale: float = 1.0
    ) -> None:
        """Add a PIL image to be drawn at a relative position."""
        self.images.append((img, position, scale))

    def render_image(self) -> Image.Image:
        """Render the page to a PIL Image."""
        fig, ax = plt.subplots(figsize=(self.width / 100, self.height / 100), dpi=100)
        ax.set_facecolor(self.theme.background_color)
        ax.axis('off')

        y = 0.95
        for seg_type, text in self.segments:
            if seg_type == 'ltx':
                ax.text(0.05, y, f"${text}$", va='top', **self.theme.as_mpl_kwargs())
                y -= 0.1
            else:
                for line in text.splitlines():
                    if line.startswith('#'):
                        level = len(line) - len(line.lstrip('#'))
                        content = line.lstrip('#').strip()
                        size = max(20, 32 - level * 2)
                        kw = self.theme.as_mpl_kwargs()
                        kw.update({"fontsize": size, "weight": 'bold'})
                        ax.text(0.05, y, content, va='top', **kw)
                    else:
                        kw = self.theme.as_mpl_kwargs()
                        parts = re.split(r"(==.+?==)", line)
                        x = 0.05
                        for part in parts:
                            if not part:
                                continue
                            if part.startswith("==") and part.endswith("=="):
                                text_part = part[2:-2]
                                hl_kw = kw.copy()
                                hl_kw.update({
                                    "bbox": dict(facecolor="yellow", alpha=0.4, boxstyle="round,pad=0.1")
                                })
                                ax.text(x, y, text_part, va='top', **hl_kw)
                            else:
                                ax.text(x, y, part, va='top', **kw)
                            x += len(part) * 0.01
                        
                    y -= 0.08
                y -= 0.08
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        plt.close(fig)
        buf.seek(0)
        base = Image.open(buf).convert("RGBA")

        for img, pos, scale in self.images:
            w = int(img.width * scale)
            h = int(img.height * scale)
            resized = img.resize((w, h), Image.ANTIALIAS)
            x = int(pos[0] * self.width - w / 2)
            y_pos = int(pos[1] * self.height - h / 2)
            base.paste(resized, (x, y_pos), resized)

        return base
