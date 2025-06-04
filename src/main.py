from parsing.document_parser import parse_document
from animation.document import Document
from animation.page import Page
from animation.canvas import Canvas
from animation.camera import Camera
from animation.renderer import Renderer
from visuals import bar_chart, circle


INFOGRAPHIC = """
||md
# Sales Overview
Below is a simple bar chart illustrating quarterly revenue.
"""

TEXT_HEAVY = r"""
||md
# Detailed Explanation
This page contains more extensive text. Here we demonstrate ==highlighted text== within a sentence to draw the viewer's attention.
||ltx
\int_a^b f(x) dx
||md
Additional commentary follows after the equation.
"""


def main() -> None:
    segments1 = parse_document(INFOGRAPHIC)
    page1 = Page()
    for seg in segments1:
        page1.add_segment(seg)

    chart_img = bar_chart(["Q1", "Q2", "Q3", "Q4"], [3, 6, 4, 5])
    page1.add_image(chart_img, position=(0.5, 0.5), scale=0.7)
    page1.add_image(circle(80, "green"), position=(0.85, 0.2))

    segments2 = parse_document(TEXT_HEAVY)
    page2 = Page()
    for seg in segments2:
        page2.add_segment(seg)

    doc = Document()
    doc.add_page(page1)
    doc.add_page(page2)

    canvas = Canvas()
    canvas.add_page(page1)
    canvas.add_page(page2)

    camera = Camera(zoom=1.2)

    renderer = Renderer(fps=24, output_dir="output")
    # Set duration long enough to showcase both pages
    renderer.render_canvas(canvas, camera, duration=15, audio_path=None)


if __name__ == "__main__":
    main()
