from __future__ import annotations
from typing import List

from .page import Page

class Document:
    """A collection of pages."""

    def __init__(self) -> None:
        self.pages: List[Page] = []

    def add_page(self, page: Page) -> None:
        self.pages.append(page)
