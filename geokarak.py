from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(":bust_in_silhouette: Georgios Karakostas", guide_style="bold cyan")
data_science_tree = tree.add(":snake: [link=https://www.linkedin.com/in/geokarak]MLOps Engineer", guide_style="green")
# data_science_tree.add("Machine Learning")
# data_science_tree.add("Storytelling")
# data_science_tree.add("Automation")
photographer_tree = tree.add(":camera: [link=https://www.georgios-karakostas.com]Photographer")
mountain_bike_tree = tree.add(":bicyclist: [link=https://www.strava.com/athletes/geokarak]Mountain biker")

about = """\
I am a mathematician by training and a photographer by heart, working professionally in the field of AI and Machine Learning since 2019."""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Bio", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
