from rich import print
from rich.table import Table
tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="left", style="red")
tabela.add_column("Preços", justify="center", style="blue")
tabela.add_row("Lapís","R$1,50")
tabela.add_row("Borracha","[green]R$5,00[/]")

print(tabela)
