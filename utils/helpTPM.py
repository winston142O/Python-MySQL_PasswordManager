from utils.dbconfig import dbconfig
import utils.aesutil
import pyperclip
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64
from rich import print as printc
from rich.console import Console
from rich.table import Table

def helpTPM():
    printc(
        "\n [purple3]----- Terminal-Password-Manager COMMANDS ------[/purple3]"+
        "\n"+
        "\n [bright_blue]FOR DATABASE CREATION: [/bright_blue]"+
        "\n"+
        "\n 1. Create Database and assign Master Password: [green_yellow]config.py make[/green_yellow]"+
        "\n 2. Delete current existing Database: [green_yellow]config.py delete[/green_yellow]"+
        "\n 3. Re-make Database: [green_yellow]config.py remake[green_yellow]"
        "\n"+
        "\n[bright_blue] MANAGER COMMANDS: [/bright_blue]"+
        "\n"+
        "\n [bright_cyan]1. Add entry:[/bright_cyan] [green_yellow]pm.py add -s sitename -u siteurl -e email -l loginname[/green_yellow]"
        "\n"+
        "\n [bright_cyan]2. Delete entry:[/bright_cyan] [green_yellow]pm.py d -s sitename -u siteurl -e email -l loginname[/green_yellow]"
        "\n"+
        "\n [bright_cyan]3. Show all entries:[/bright_cyan] [green_yellow]pm.py e[/green_yellow]"
        "\n"+
        "\n [bright_cyan]4. Show a specific entry:[/bright_cyan] [green_yellow]pm.py e -s sitename[/green_yellow]"
        "\n"+
        "\n [bright_cyan]5. Copy password to clipboard:[/bright_cyan] [green_yellow]pmpy e -s sitename[/green_yellow]"
        "\n"+
        "\n [bright_cyan]6. Automatically generate a password:[/bright_cyan] [green_yellow]pm.py g --lenght[/green_yellow]"
           )