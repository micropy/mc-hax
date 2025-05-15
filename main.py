import subprocess
import os
import sys
from colorama import Fore

def set_terminal_title():
    if sys.platform == "win32":
        os.system("title PenguinMC - alpha")
    else:
        sys.stdout.write(f"\033]0;PenguinMC - alpha\007")
        sys.stdout.flush()

set_terminal_title()

def print_penguinmc():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⣾⠷⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⣅⠀⣘⡆⠀⢀⣙⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠉⠻⠷⠾⠿⢭⣍⡽⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⢃⡼⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⢀⠤⠤⠤⠤⠤⠒⠒⠉⠀⠀⠹⣦⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡟⣏⠓⠛⠿⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡏⠀⠀⠀⠀⠈⢳⡙⣧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣏⠤⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣯⠉⠛⠲⢦⣄⠀⣧⠘⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡠⢖⠿⠛⢻⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠉⢳⣏⣠⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠖⣫⠔⠁⠀⠀⣌⣀⡤⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⢞⡵⠊⠀⢀⣤⠴⠚⠉⠁⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡴⢃⠎⠀⣠⡶⠋⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡾⠁⡌⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡇⠀⣷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠳⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢀⠞⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠐⡇⠀⠀⠀⠀⣜⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⣇⠀⠀⠀⠀⡏⠉⠉⠓⠢⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣦⠀⠀⣀⣾⡤⠶⠖⠒⢳⡀⠀⣄⣀⣹⣶⠼⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣻⣃⠈⢳⠉⢀⡇⠀⠀⠀⠀⠈⠙⠚⠻⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠻⠶⣿⢀⠁⠉⠳⠤⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢛⠙⠉⠙⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀
          """)
def do_servercheck(arg):
    args = ''.join(arg)
    subprocess.run(['python', 'commands//servercheck.py', args])

def do_botsjoining(arg):
    serverip, server_port, version, bot_amount, bot_name, timein = arg.split(':')
    subprocess.run(['node', 'commands//botsjoining.js'] + arg)

def do_playercheck(arg):
    name = ''.join(arg)
    subprocess.run(['python', 'commands//playercheck.py', name])

def do_checkpassword(arg):
    serverip, server_port, version, bot_name, password = arg
    subprocess.run(['node', 'commands//checkpassword.js'] + arg)

def do_portschecker(arg):
    portsfile = ''.join(arg)
    subprocess.run(['python', 'commands//portschecker.py', portsfile])

def do_help():
    subprocess.run(['python', 'commands//help.py'])

actions = {
    'servercheck':do_servercheck,
    'botsjoining': do_botsjoining,
    'playercheck': do_playercheck,
    'checkpassword': do_checkpassword,
    'portschecker': do_portschecker,
    'help': do_help
}

print_penguinmc()

def menu():
    arg = input(f'{Fore.BLUE}PenguinMC{Fore.RESET}> ').split()
    if arg[0] in actions and len(arg) <2:
        actions[arg[0]]()
    elif arg[0] in actions:
        actions[arg[0]](arg[1:])
    else:
        print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET} Unknown command: "{arg[0]}" write {Fore.GREEN}help{Fore.RESET} for list of commands')
while True:
    menu()