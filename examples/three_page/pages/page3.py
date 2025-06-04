from animation import Page
from parsing.document_parser import parse_document

TEXT = """
||md
# Third Page
Additional page to demonstrate grid layout.
"""


def make_page() -> Page:
    segments = parse_document(TEXT)
    page = Page()
    for seg in segments:
        page.add_segment(seg)
    return page
