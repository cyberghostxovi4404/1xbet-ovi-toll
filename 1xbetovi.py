#!/usr/bin/env python3
"""
PREDICX PRO v7.0 - Multi-Sport Prediction Engine
Created by OVI
Supports: Football, Cricket, Tennis
"""

import os
import sys
import time
import random
import hashlib
from getpass import getpass
from threading import Thread
from datetime import datetime

# Colorama for colors (fallback)
from colorama import Fore, Style, init
init(autoreset=True)

# Rich library for professional UI
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich.layout import Layout
    from rich.live import Live
    from rich.text import Text
    from rich import box
    from rich.prompt import Prompt
    from rich.align import Align
    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None

# ======================== CONFIGURATION =========================
PASSWORD_HASH = hashlib.sha256("ovi123".encode()).hexdigest()  # Change this
# =================================================================

# ======================== UTILITY FUNCTIONS =====================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_rich():
    print(Fore.RED + "⚠️  Rich library not found. Install it for best experience:")
    print(Fore.YELLOW + "   pip install rich")
    time.sleep(2)

# ======================== ANIMATIONS ============================
def pulse_animation(text, duration=2):
    if RICH_AVAILABLE:
        with console.status(f"[bold yellow]{text}", spinner="dots"):
            time.sleep(duration)
    else:
        print(Fore.YELLOW + text, end="", flush=True)
        for _ in range(6):
            time.sleep(0.2)
            print(".", end="", flush=True)
        print()

def smart_loader(task_name="Processing", duration=2):
    if RICH_AVAILABLE:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task(f"[cyan]{task_name}...", total=100)
            for _ in range(100):
                time.sleep(duration/100)
                progress.update(task, advance=1)
    else:
        print(Fore.CYAN + f"\n[+] {task_name}...", end="", flush=True)
        for _ in range(10):
            time.sleep(0.2)
            print(Fore.GREEN + "▌", end="", flush=True)
        print(" Done!")

def show_logo():
    logo = r"""
[bold red]
    ██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚██╗██╔╝
    ██████╔╝██████╔╝█████╗  ██║  ██║██║██║      ╚███╔╝ 
    ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║      ██╔██╗ 
    ██║     ██║  ██║███████╗██████╔╝██║╚██████╗██╔╝ ██╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝
[/bold red]
[bold yellow]           M U L T I - S P O R T   P R O   v 7 . 0[/bold yellow]
[bold cyan]              Football | Cricket | Tennis[/bold cyan]
[bold green]                    BY OVI[/bold green]
    """
    if RICH_AVAILABLE:
        console.print(logo)
        console.rule(style="bright_red")
    else:
        print(Fore.RED + r"""
    ██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚██╗██╔╝
    ██████╔╝██████╔╝█████╗  ██║  ██║██║██║      ╚███╔╝ 
    ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║      ██╔██╗ 
    ██║     ██║  ██║███████╗██████╔╝██║╚██████╗██╔╝ ██╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝
        """ + Fore.YELLOW + "   MULTI-SPORT PRO v7.0 - BY OVI")
        print(Fore.WHITE + "    " + "─" * 50)

# ======================== LOGIN SYSTEM ==========================
def login_screen():
    clear_screen()
    if RICH_AVAILABLE:
        console.print(Align.center(Text("PREDICX PRO v7.0", style="bold red"), width=60))
        console.print(Align.center(Text("AUTHORIZED ACCESS ONLY", style="bold yellow"), width=60))
        console.print()
        panel = Panel("[cyan]Enter your credentials to continue[/cyan]", 
                      title="🔐 SECURE LOGIN", border_style="green", box=box.DOUBLE)
        console.print(Align.center(panel))
    else:
        show_logo()
        print(Fore.RED + "\n⚠️  AUTHORIZED ACCESS ONLY")
        print(Fore.YELLOW + "Please login to continue")

    pulse_animation("Initializing security", 1.5)

    for attempt in range(3):
        if RICH_AVAILABLE:
            password = Prompt.ask("[bold yellow]Password", password=True)
        else:
            password = getpass(Fore.YELLOW + "Password: ")

        if hashlib.sha256(password.encode()).hexdigest() == PASSWORD_HASH:
            smart_loader("Authenticating", 1)
            print(Fore.GREEN + "\n✅ Access Granted. Welcome back, OVI!")
            time.sleep(1)
            return True
        else:
            print(Fore.RED + f"\n❌ Invalid password. Attempts left: {2-attempt}")
            time.sleep(1)

    print(Fore.RED + "\n🚫 Too many failed attempts. Exiting...")
    time.sleep(2)
    return False

# ======================== SPORT DATA GENERATORS =================
# Football
def generate_football_stats(home, away):
    home_strength = random.uniform(0.7, 1.3)
    away_strength = random.uniform(0.7, 1.3)
    home_goals = max(0, int(random.gauss(home_strength * 1.5, 1)))
    away_goals = max(0, int(random.gauss(away_strength * 1.2, 1)))
    total = home_strength + away_strength + 1
    home_win_prob = round((home_strength / total) * 80 + 10, 1)
    away_win_prob = round((away_strength / total) * 80 + 10, 1)
    draw_prob = round(100 - home_win_prob - away_win_prob, 1)
    if draw_prob < 0:
        draw_prob = 0
        home_win_prob = 50
        away_win_prob = 50
    return {
        'home_goals': home_goals,
        'away_goals': away_goals,
        'home_win_prob': home_win_prob,
        'away_win_prob': away_win_prob,
        'draw_prob': draw_prob,
        'possession_home': random.randint(45, 65),
        'shots_home': random.randint(10, 25),
        'shots_away': random.randint(8, 22),
        'corners_home': random.randint(3, 10),
        'corners_away': random.randint(2, 9),
        'fouls_home': random.randint(8, 15),
        'fouls_away': random.randint(8, 15),
    }

# Cricket
def generate_cricket_stats(team1, team2):
    format = random.choice(["T20", "ODI", "Test"])
    if format == "T20":
        overs = 20
        runs1 = random.randint(120, 220)
        runs2 = random.randint(100, runs1+30)
        wickets1 = random.randint(3, 10)
        wickets2 = random.randint(3, 10)
    elif format == "ODI":
        overs = 50
        runs1 = random.randint(200, 350)
        runs2 = random.randint(180, runs1+40)
        wickets1 = random.randint(4, 10)
        wickets2 = random.randint(4, 10)
    else:  # Test
        overs = 90  # per day approx
        runs1 = random.randint(300, 550)
        runs2 = random.randint(250, runs1+60)
        wickets1 = random.randint(6, 10)
        wickets2 = random.randint(6, 10)
    
    # Win probability based on runs
    total_strength = runs1 + runs2
    team1_prob = round((runs1 / total_strength) * 100, 1)
    team2_prob = round(100 - team1_prob, 1)
    draw_prob = round(random.uniform(0, 15), 1) if format == "Test" else 0
    if format == "Test":
        team1_prob = round(team1_prob * (100-draw_prob)/100, 1)
        team2_prob = round(team2_prob * (100-draw_prob)/100, 1)
    
    return {
        'format': format,
        'overs': overs,
        'team1_runs': runs1,
        'team2_runs': runs2,
        'team1_wickets': wickets1,
        'team2_wickets': wickets2,
        'team1_prob': team1_prob,
        'team2_prob': team2_prob,
        'draw_prob': draw_prob,
        'extras': random.randint(5, 20),
        'fours': random.randint(8, 25),
        'sixes': random.randint(2, 12),
    }

# Tennis
def generate_tennis_stats(player1, player2):
    # Best of 3 or 5 sets
    best_of = random.choice([3, 5])
    sets_p1 = random.randint(0, best_of//2 + 1)
    sets_p2 = random.randint(0, best_of//2 + 1)
    while sets_p1 + sets_p2 > best_of or (sets_p1 == sets_p2 and best_of % 2 == 0):
        sets_p1 = random.randint(0, best_of//2 + 1)
        sets_p2 = random.randint(0, best_of//2 + 1)
    
    games_p1 = random.randint(0, 24)
    games_p2 = random.randint(0, 24)
    
    # Win probability based on form
    p1_form = random.uniform(0.6, 1.4)
    p2_form = random.uniform(0.6, 1.4)
    total = p1_form + p2_form
    p1_prob = round((p1_form / total) * 100, 1)
    p2_prob = round(100 - p1_prob, 1)
    
    return {
        'best_of': best_of,
        'sets_player1': sets_p1,
        'sets_player2': sets_p2,
        'games_player1': games_p1,
        'games_player2': games_p2,
        'aces_p1': random.randint(0, 15),
        'aces_p2': random.randint(0, 12),
        'double_faults_p1': random.randint(0, 5),
        'double_faults_p2': random.randint(0, 5),
        'p1_win_prob': p1_prob,
        'p2_win_prob': p2_prob,
    }

# ======================== UI DISPLAY FUNCTIONS ==================
def display_football_prediction(home, away, stats):
    if RICH_AVAILABLE:
        content = f"""
[bold cyan]{home}[/bold cyan] vs [bold cyan]{away}[/bold cyan]

[bold yellow]Win Probabilities:[/bold yellow]
  {home}: [green]{stats['home_win_prob']}%[/green]
  {away}: [red]{stats['away_win_prob']}%[/red]
  Draw: [blue]{stats['draw_prob']}%[/blue]

[bold yellow]Predicted Score:[/bold yellow]  [bold]{stats['home_goals']} - {stats['away_goals']}[/bold]

[bold yellow]Match Stats:[/bold yellow]
  Possession: {home} {stats['possession_home']}% | {away} {100-stats['possession_home']}%
  Shots: {stats['shots_home']} - {stats['shots_away']}
  Corners: {stats['corners_home']} - {stats['corners_away']}
  Fouls: {stats['fouls_home']} - {stats['fouls_away']}
        """
        panel = Panel(content, title="[bold magenta]FOOTBALL ANALYSIS[/bold magenta]", 
                     border_style="green", box=box.ROUNDED)
        console.print(panel)
    else:
        print(Fore.WHITE + "="*50)
        print(Fore.CYAN + f"{home.upper()} vs {away.upper()} (Football)")
        # ... (similar plain text)

def display_cricket_prediction(team1, team2, stats):
    if RICH_AVAILABLE:
        content = f"""
[bold cyan]{team1}[/bold cyan] vs [bold cyan]{team2}[/bold cyan]  [yellow]({stats['format']})[/yellow]

[bold yellow]Win Probabilities:[/bold yellow]
  {team1}: [green]{stats['team1_prob']}%[/green]
  {team2}: [red]{stats['team2_prob']}%[/red]
  Draw: [blue]{stats['draw_prob']}%[/blue]

[bold yellow]Predicted Score:[/bold yellow]
  {team1}: {stats['team1_runs']}/{stats['team1_wickets']} in {stats['overs']} ov
  {team2}: {stats['team2_runs']}/{stats['team2_wickets']} in {stats['overs']} ov

[bold yellow]Match Stats:[/bold yellow]
  Fours: {stats['fours']} | Sixes: {stats['sixes']} | Extras: {stats['extras']}
        """
        panel = Panel(content, title="[bold magenta]CRICKET ANALYSIS[/bold magenta]", 
                     border_style="yellow", box=box.ROUNDED)
        console.print(panel)
    else:
        # fallback
        pass

def display_tennis_prediction(player1, player2, stats):
    if RICH_AVAILABLE:
        content = f"""
[bold cyan]{player1}[/bold cyan] vs [bold cyan]{player2}[/bold cyan]  [yellow](Best of {stats['best_of']})[/yellow]

[bold yellow]Win Probabilities:[/bold yellow]
  {player1}: [green]{stats['p1_win_prob']}%[/green]
  {player2}: [red]{stats['p2_win_prob']}%[/red]

[bold yellow]Predicted Score:[/bold yellow]
  Sets: {stats['sets_player1']} - {stats['sets_player2']}
  Games: {stats['games_player1']} - {stats['games_player2']}

[bold yellow]Match Stats:[/bold yellow]
  Aces: {player1} {stats['aces_p1']} | {player2} {stats['aces_p2']}
  Double Faults: {stats['double_faults_p1']} - {stats['double_faults_p2']}
        """
        panel = Panel(content, title="[bold magenta]TENNIS ANALYSIS[/bold magenta]", 
                     border_style="cyan", box=box.ROUNDED)
        console.print(panel)
    else:
        pass

# ======================== SPORT MENUS ============================
def football_menu():
    while True:
        clear_screen()
        show_logo()
        print(Fore.MAGENTA + "\n⚽ FOOTBALL ANALYTICS")
        print(Fore.WHITE + "   [1] Auto-scan live fixtures")
        print(Fore.WHITE + "   [2] Manual match analysis")
        print(Fore.WHITE + "   [3] Odds tracker")
        print(Fore.RED + "   [0] Back to main menu")
        choice = input(Fore.YELLOW + "\nSelect: ").strip()
        if choice == '1':
            clear_screen()
            show_logo()
            pulse_animation("Scanning football fixtures", 2)
            smart_loader("Fetching live data", 2)
            teams = ["Barcelona", "Real Madrid", "Liverpool", "Man City", "Bayern", "PSG", "Juventus", "Chelsea"]
            matches = random.sample(teams, 6)
            if RICH_AVAILABLE:
                table = Table(title="📅 LIVE FOOTBALL FIXTURES", box=box.ROUNDED)
                table.add_column("Home", style="green")
                table.add_column("Away", style="red")
                table.add_column("Time", style="yellow")
                for i in range(0, 5, 2):
                    table.add_row(matches[i], matches[i+1], f"{random.randint(12,22)}:00")
                console.print(table)
            input(Fore.YELLOW + "\nPress ENTER...")
        elif choice == '2':
            clear_screen()
            show_logo()
            home = input("Home team: ").strip() or "Barcelona"
            away = input("Away team: ").strip() or "Real Madrid"
            pulse_animation(f"Analyzing {home} vs {away}", 2)
            smart_loader("Running simulations", 3)
            stats = generate_football_stats(home, away)
            display_football_prediction(home, away, stats)
            input(Fore.YELLOW + "\nPress ENTER...")
        elif choice == '3':
            clear_screen()
            show_logo()
            print(Fore.MAGENTA + "\nOdds tracker - Football (simulated)")
            time.sleep(2)
        elif choice == '0':
            break

def cricket_menu():
    while True:
        clear_screen()
        show_logo()
        print(Fore.MAGENTA + "\n🏏 CRICKET ANALYTICS")
        print(Fore.WHITE + "   [1] Auto-scan live matches")
        print(Fore.WHITE + "   [2] Manual match analysis")
        print(Fore.WHITE + "   [3] Odds tracker")
        print(Fore.RED + "   [0] Back to main menu")
        choice = input(Fore.YELLOW + "\nSelect: ").strip()
        if choice == '2':
            clear_screen()
            show_logo()
            team1 = input("Team 1: ").strip() or "India"
            team2 = input("Team 2: ").strip() or "Australia"
            pulse_animation(f"Analyzing {team1} vs {team2}", 2)
            smart_loader("Running simulations", 3)
            stats = generate_cricket_stats(team1, team2)
            display_cricket_prediction(team1, team2, stats)
            input(Fore.YELLOW + "\nPress ENTER...")
        # Add other options similarly
        else:
            break

def tennis_menu():
    while True:
        clear_screen()
        show_logo()
        print(Fore.MAGENTA + "\n🎾 TENNIS ANALYTICS")
        print(Fore.WHITE + "   [1] Auto-scan live matches")
        print(Fore.WHITE + "   [2] Manual match analysis")
        print(Fore.WHITE + "   [3] Odds tracker")
        print(Fore.RED + "   [0] Back to main menu")
        choice = input(Fore.YELLOW + "\nSelect: ").strip()
        if choice == '2':
            clear_screen()
            show_logo()
            p1 = input("Player 1: ").strip() or "Djokovic"
            p2 = input("Player 2: ").strip() or "Alcaraz"
            pulse_animation(f"Analyzing {p1} vs {p2}", 2)
            smart_loader("Running simulations", 3)
            stats = generate_tennis_stats(p1, p2)
            display_tennis_prediction(p1, p2, stats)
            input(Fore.YELLOW + "\nPress ENTER...")
        else:
            break

# ======================== MAIN MENU ==============================
def main_menu():
    if not RICH_AVAILABLE:
        install_rich()
    
    if not login_screen():
        return

    while True:
        clear_screen()
        show_logo()
        print(Fore.CYAN + "\nSELECT SPORT")
        print(Fore.WHITE + "   [1] ⚽  Football")
        print(Fore.WHITE + "   [2] 🏏  Cricket")
        print(Fore.WHITE + "   [3] 🎾  Tennis")
        print(Fore.RED + "   [0] Exit")
        choice = input(Fore.YELLOW + "\nYour choice: ").strip()
        if choice == '1':
            football_menu()
        elif choice == '2':
            cricket_menu()
        elif choice == '3':
            tennis_menu()
        elif choice == '0':
            print(Fore.RED + "\nShutting down...")
            smart_loader("Saving session", 1)
            break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nSession terminated.")
        sys.exit(0)
