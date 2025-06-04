from __future__ import annotations
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont


def typing_frames(
    image: Image.Image,
    position: Tuple[int, int],
    text: str,
    color: str = "black",
    font: ImageFont.ImageFont | None = None,
) -> List[Image.Image]:
    """Generate frames showing *text* typed onto *image* one character at a time."""
    font = font or ImageFont.load_default()
    frames = []
    typed = ""
    for ch in text:
        typed += ch
        frame = image.copy()
        draw = ImageDraw.Draw(frame)
        draw.text(position, typed, fill=color, font=font)
        frames.append(frame)
    return frames
