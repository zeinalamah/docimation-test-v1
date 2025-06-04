# agentic-coding-test-v1
# Animated Document Generator

This repository contains a small framework for creating animated document videos.
Documents mix Markdown and LaTeX using `||md` and `||ltx` markers. Pages can also contain images such as charts or shapes.  Text surrounded by `==` in markdown lines will be highlighted. Pages are rendered with Matplotlib and collected inside a `Canvas` which is filmed by a `Camera`. The `Renderer` then produces a video using MoviePy and may optionally add audio.

## Features

- Mixed Markdown and LaTeX content
- Simple text highlighting using `==text==`
- Embedding of charts and shapes as images
- Basic zoom animation controlled by a camera

## Usage

Install the dependencies listed in `requirements.txt` and run:

```bash
pip install -r requirements.txt
python3 src/main.py
```

The requirements include `matplotlib`, `moviepy`, `pillow`, and `numpy`.

The resulting video is saved to the `output/` folder.  A simple example is embedded in `src/main.py` and a modular multi-page demo can be run with:

```bash
PYTHONPATH=src python examples/three_page/main.py
```
