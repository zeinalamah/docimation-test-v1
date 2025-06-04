from animation import (
    Document,
    Canvas,
    Camera,
    Renderer,
    highlight_text_frames,
    typing_frames,
    fade_in_frames,
)
from .pages import page1, page2, page3


def main() -> None:
    p1 = page1.make_page()
    p2 = page2.make_page()
    p3 = page3.make_page()

    doc = Document()
    doc.add_page(p1)
    doc.add_page(p2)
    doc.add_page(p3)

    canvas = Canvas(width=p1.width * 3, height=p1.height)
    canvas.add_page(p1, position=(0, 0))
    canvas.add_page(p2, position=(p1.width, 0))
    canvas.add_page(p3, position=(p1.width * 2, 0))

    composite = canvas.render_composite()
    fade_seq = fade_in_frames(composite, steps=8)

    # Highlight the first heading character by character
    bbox = (
        int(p1.width * 0.05),
        int(p1.height * 0.05),
        int(p1.width * 0.5),
        int(p1.height * 0.15),
    )
    highlight_seq = highlight_text_frames(
        p1.render_image(), bbox, text="Sales Overview", color="yellow"
    )

    # Demonstrate typing effect on page3
    typing_seq = typing_frames(
        p3.render_image(),
        (int(p3.width * 0.05), int(p3.height * 0.6)),
        "Typing demo",
        color="blue",
    )
    images = [*fade_seq, p1.render_image(), *highlight_seq, *typing_seq]

    renderer = Renderer(fps=24, output_dir="output")
    renderer.render_images(images, zoom=1.2, duration=5)


if __name__ == "__main__":
    main()
