from PIL import Image, ImageDraw


def circle(diameter: int, color: str = "red") -> Image.Image:
    """Create a simple colored circle."""
    img = Image.new("RGBA", (diameter, diameter), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((0, 0, diameter - 1, diameter - 1), fill=color)
    return img
