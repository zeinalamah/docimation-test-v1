from __future__ import annotations
from typing import Tuple, List
from PIL import Image, ImageDraw


def highlight_region(
    image: Image.Image,
    bbox: Tuple[int, int, int, int],
    progress: float = 1.0,
    color: str = "yellow",
    alpha: float = 0.4,
) -> Image.Image:
    """Return a copy of *image* with a partially filled highlight box."""
    progress = max(0.0, min(1.0, progress))
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    x0, y0, x1, y1 = bbox
    width = int((x1 - x0) * progress)
    draw.rectangle([x0, y0, x0 + width, y1], fill=color)
    overlay.putalpha(int(255 * alpha))
    out = image.copy()
    out.paste(overlay, (0, 0), overlay)
    return out


def highlight_frames(
    image: Image.Image,
    bbox: Tuple[int, int, int, int],
    steps: int = 10,
    color: str = "yellow",
    alpha: float = 0.4,
) -> List[Image.Image]:
    """Generate frames highlighting *bbox* progressively."""
    frames = []
    for i in range(1, steps + 1):
        progress = i / float(steps)
        frames.append(highlight_region(image, bbox, progress, color, alpha))
    return frames
