from __future__ import annotations
from typing import List
from PIL import Image


def fade_in_frames(image: Image.Image, steps: int = 10) -> List[Image.Image]:
    """Generate frames fading in the image."""
    frames = []
    for i in range(steps):
        alpha = (i + 1) / steps
        frame = image.copy()
        frame.putalpha(int(255 * alpha))
        frames.append(frame)
    return frames


def fade_out_frames(image: Image.Image, steps: int = 10) -> List[Image.Image]:
    """Generate frames fading out the image."""
    frames = []
    for i in range(steps):
        alpha = 1 - (i + 1) / steps
        frame = image.copy()
        frame.putalpha(int(255 * alpha))
        frames.append(frame)
    return frames
