import re
from typing import List, Tuple

Segment = Tuple[str, str]

def parse_document(text: str) -> List[Segment]:
    """Parse text with ||md and ||ltx markers into segments.

    The markers should appear alone on a line. Content following a marker
    is associated with that type until the next marker or end of input.
    """
    segments: List[Segment] = []
    current_type = None
    buffer = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "||md":
            if buffer and current_type:
                segments.append((current_type, "\n".join(buffer).strip()))
            current_type = "md"
            buffer = []
        elif stripped == "||ltx" or stripped == "!& TX":
            if buffer and current_type:
                segments.append((current_type, "\n".join(buffer).strip()))
            current_type = "ltx"
            buffer = []
        else:
            buffer.append(line)
    if buffer and current_type:
        segments.append((current_type, "\n".join(buffer).strip()))
    return segments
