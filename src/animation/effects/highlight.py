from __future__ import annotations
from typing import Tuple, List
from PIL import Image, ImageDraw, ImageColor


def highlight_region(
    image: Image.Image,
    bbox: Tuple[int, int, int, int],
    progress: float = 1.0,
    color: str = "yellow",
    alpha: float = 0.4,
) -> Image.Image:
    """Return ``image`` with a partially filled highlight overlay.

    Parameters
    ----------
    image:
        The base image that will receive the overlay.
    bbox:
        Rectangle coordinates ``(x0, y0, x1, y1)`` specifying the highlight area.
    progress:
        Number from ``0`` to ``1`` representing how much of the region should be
        filled horizontally.
    color:
        Fill color of the highlight.
    alpha:
        Opacity of the highlight overlay.
    """
    progress = max(0.0, min(1.0, progress))
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    x0, y0, x1, y1 = bbox
    width = int((x1 - x0) * progress)
    rgb = ImageColor.getrgb(color)
    draw.rectangle(
        [x0, y0, x0 + width, y1],
        fill=rgb + (int(255 * alpha),),
    )
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
    """Generate a sequence of images highlighting ``bbox`` progressively.

    Parameters
    ----------
    image:
        Source image to draw on.
    bbox:
        Tuple of ``(x0, y0, x1, y1)`` coordinates describing the highlight box.
    steps:
        Number of intermediate frames.  Higher values produce smoother motion.
    color:
        Fill color of the highlight region.
    alpha:
        Opacity of the highlight overlay, between ``0`` and ``1``.
    """
    frames = []
    for i in range(1, steps + 1):
        progress = i / float(steps)
        frames.append(highlight_region(image, bbox, progress, color, alpha))
    return frames


def highlight_text_frames(
    image: Image.Image,
    bbox: Tuple[int, int, int, int],
    text: str,
    color: str = "yellow",
    alpha: float = 0.4,
) -> List[Image.Image]:
    """Animate highlighting ``text`` one character at a time.

    The function calculates the number of steps from ``text`` length and then
    delegates to :func:`highlight_frames`.  This is useful when you need the
    highlight animation to synchronise with typing or narration.
    """
    steps = max(1, len(text))
    return highlight_frames(image, bbox, steps=steps, color=color, alpha=alpha)
