import mysql.connector
from rich import print as printc
from rich.console import Console
console = Console()
  
def dbconfig():
  try:
    db = mysql.connector.connect(
      host ="localhost",
      user ="root",
      passwd ="Emill2325!"
    )
  except Exception as e:
    printc("[red][!] An error occurred while trying to connect to the database[/red]")
    console.print_exception(show_locals=True)

  return db