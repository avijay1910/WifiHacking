#!/usr/bin/env python

"""
WIFIHacker - Wireless Penetration Testing Tool
----------------------------------------------
"""


from rich.console import Console
from rich.table import Table
from includes import banner
from rich.prompt import IntPrompt
from includes.portal import get_credentials_json
import os

console = Console()

def clear():
    os.system("clear")

def main_menu():
    try:
        table = Table(title="[bold green]Main Menu[/bold green]", show_header=True, header_style="bold blue")
        table.add_column("No.", style="bold cyan")
        table.add_column("Option", style="bold white")
        table.add_row("1", "📡 Wifi Phishing")
        table.add_row("2", "📶 Wifi SPAM ")
        table.add_row("3", "🚫 Wifi Deauth ")
        table.add_row("4", "📘 Learn Wifi Hacking (Coming Soon)")
        table.add_row("5", "🔐 View Captured Credentials")
        table.add_row("6", "❌ Exit")
        console.print(table)
        return IntPrompt.ask("\n👉 Select an option")
    except EOFError:
        console.print("[red]❌ No input received! Exiting...[/red]")
        exit(1)

