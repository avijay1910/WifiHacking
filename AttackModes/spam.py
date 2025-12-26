#!/usr/bin/env python

"""
WIFIHacker - Wireless Penetration Testing Tool
----------------------------------------------
"""

import subprocess
from rich.console import Console
from time import sleep
import sys,os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from includes import banner

console = Console()

def enable_monitor_mode(interface):
    try:
        subprocess.run(["ip", "link", "set", interface, "down"], check=True)
        subprocess.run(["iw", interface, "set", "monitor", "none"], check=True)
        subprocess.run(["ip", "link", "set", interface, "up"], check=True)
        console.print(f"[green]✅ {interface} is now in monitor mode.[/green]")
    except subprocess.CalledProcessError:
        console.print(f"[red]❌ Failed to enable monitor mode on {interface}[/red]")
        exit()

def get_ssid_input():
    ssid = input("📡 Enter WiFi name to spam: ").strip()
    if not ssid:
        console.print("[red]❌ SSID cannot be empty.[/red]")
        exit()
    return ssid


def get_ssid_count():
    try:
        count = int(input("🔢 How many WiFi networks to broadcast (max 100)? "))
        if not 1 <= count <= 100:
            console.print("[red]❌ Please enter a number between 1 and 100.[/red]")
            exit(1)
        return count
    except ValueError:
        console.print("[red]❌ Invalid number. Please enter a valid integer.[/red]")
        exit(1)




def generate_ssid_file(base_name, count):
    file_name = f"ssid.txt"
    with open(file_name, "w") as f:
        for i in range(1, count+1):
            f.write(f"{base_name}_{i}\n")
    console.print(f"[green]✅ SSID list saved to:[/green] [yellow]{file_name}[/yellow]")
    return file_name


def launch_attack(interface, ssid_file):
    console.print(f"\n[bold red]🚀 Launching WiFi spam on interface {interface} using {ssid_file}[/bold red]\n")
    sleep(1)
    try:
        subprocess.run(["mdk4", interface, "b", "-f", ssid_file, "-s", "100"])
    except KeyboardInterrupt:
        console.print("\n[bold red]⛔ Attack stopped by user.[/bold red]")


def main(interface):
    enable_monitor_mode(interface)
    attack_mode = "📶 Wifi SPAM"
    ssid_name = get_ssid_input()
    ssid_count = get_ssid_count()
    ssid_file = generate_ssid_file(ssid_name, ssid_count)
    banner.show_banner()
    banner.wifispam(interface,attack_mode,ssid_name,ssid_count)
    launch_attack(f"{interface}", ssid_file)

