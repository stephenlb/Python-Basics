from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")
table.add_column("Grade", justify="right", style="yellow")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952M", "A")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393M", "A")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332M", "A")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332M", "A")

console = Console()
console.print(table)
