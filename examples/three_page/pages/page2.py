from animation import Page
from parsing.document_parser import parse_document

TEXT_HEAVY = r"""
||md
# Detailed Explanation
This page contains more extensive text. Here we demonstrate ==highlighted text== within a sentence to draw the viewer's attention.
||ltx
\int_a^b f(x) dx
||md
Additional commentary follows after the equation.
"""


def make_page() -> Page:
    segments = parse_document(TEXT_HEAVY)
    page = Page()
    for seg in segments:
        page.add_segment(seg)
    return page
