from animation import Page
from parsing.document_parser import parse_document
from visuals import bar_chart, circle

INFOGRAPHIC = """
||md
# Sales Overview
Below is a simple bar chart illustrating quarterly revenue.
"""


def make_page() -> Page:
    segments = parse_document(INFOGRAPHIC)
    page = Page()
    for seg in segments:
        page.add_segment(seg)
    chart_img = bar_chart(["Q1", "Q2", "Q3", "Q4"], [3, 6, 4, 5])
    page.add_image(chart_img, position=(0.5, 0.5), scale=0.7)
    page.add_image(circle(80, "green"), position=(0.85, 0.2))
    return page
