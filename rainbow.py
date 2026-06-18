import colorsys
from rich.console import Console
from rich.color import Color
from rich.style import Style

console = Console()

for i in range(100):
    hue = int(i * 30.0)
    color = Color.from_rgb(
        *[int(c * 255) for c in colorsys.hls_to_rgb(hue / 360, 0.5, 1.0)]
    )
    console.print("█" * 69, style=Style(color=color))
