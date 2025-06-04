from io import BytesIO
from typing import List

import matplotlib.pyplot as plt
from PIL import Image


def bar_chart(labels: List[str], values: List[float], width: int = 400, height: int = 300) -> Image.Image:
    """Create a simple bar chart and return it as a PIL image."""
    fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
    ax.bar(labels, values, color="skyblue")
    ax.set_ylim(0, max(values) * 1.2)
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=100, bbox_inches="tight", transparent=True)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)
