from pathlib import Path
from typing import List

from .canvas import Canvas
from .camera import Camera

import numpy as np
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, vfx
from PIL import Image

if not hasattr(Image, "ANTIALIAS"):
    Image.ANTIALIAS = Image.Resampling.LANCZOS


class Renderer:
    def __init__(self, fps: int = 24, output_dir: str = "output") -> None:
        self.fps = fps
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def render_images(
        self,
        images: List[Image.Image],
        zoom: float = 1.2,
        duration: float = 5.0,
        audio_path: str | None = None,
    ) -> Path:
        """Create a simple zoom animation from images."""

        clips = []
        for img in images:
            clip = ImageClip(np.array(img)).set_duration(duration)
            clip = clip.fx(vfx.resize, lambda t: 1 + (zoom - 1) * t / duration)
            clips.append(clip)
        video = concatenate_videoclips(clips, method="compose")

        if audio_path:
            audio = AudioFileClip(audio_path)
            video = video.set_audio(audio)

        output_path = self.output_dir / "animated_document.mp4"
        video.write_videofile(
            str(output_path), fps=self.fps, codec="libx264", audio=bool(audio_path)
        )
        return output_path

    def render_canvas(
        self,
        canvas: Canvas,
        camera: Camera,
        zoom: float = 1.2,
        duration: float = 5.0,
        audio_path: str | None = None,
    ) -> Path:
        images = canvas.render_images()
        final_zoom = zoom * camera.zoom
        return self.render_images(images, final_zoom, duration, audio_path)
