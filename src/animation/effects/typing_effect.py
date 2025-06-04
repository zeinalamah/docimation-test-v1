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
    """Generate frames showing ``text`` typed onto ``image`` one character at a time.

    Parameters
    ----------
    image:
        Base image that the text will be drawn on.
    position:
        ``(x, y)`` coordinates for the text origin.
    text:
        Text string to type.
    color:
        Text color.
    font:
        Optional PIL font instance. If ``None`` the default bitmap font is used.
    """
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
