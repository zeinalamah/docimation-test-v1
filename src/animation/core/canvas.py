from __future__ import annotations
from typing import List, Tuple
from PIL import Image

from .page import Page

class Canvas:
    """Container for pages and other renderable objects."""

    def __init__(self, width: int = 1920, height: int = 1080, background: str = "white") -> None:
        self.width = width
        self.height = height
        self.background = background
        self.objects: List[Tuple[Page, Tuple[int, int]]] = []

    def add_page(self, page: Page, position: Tuple[int, int] = (0, 0)) -> None:
        """Add a page at a specific position."""
        self.objects.append((page, position))

    def render_images(self) -> List[Image.Image]:
        """Render each page individually and return list of images."""
        images = []
        for page, _ in self.objects:
            img = page.render_image()
            images.append(img)
        return images

    def render_composite(self) -> Image.Image:
        """Render all pages onto a single canvas respecting their positions."""
        base = Image.new("RGBA", (self.width, self.height), self.background)
        for page, pos in self.objects:
            img = page.render_image()
            base.paste(img, pos, img)
        return base
