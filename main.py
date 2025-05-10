from mcstatus import JavaServer
import subprocess
import os
import sys

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
    serverip, server_port = ''.join(arg).split(':')
    subprocess.run(['python', 'commands//servercheck.py', serverip, server_port])

def do_domainsbruteforce(arg):
    serverip, wordlist = arg.split(':')
    subprocess.run(['python', 'commands//domainsbruteforce.py', serverip, wordlist])

def do_botsjoining(arg):
    serverip, server_port, version, bot_amount, bot_name, timein = arg.split(':')
    subprocess.run(['node', 'commands//botsjoining.js'] + arg)

def do_playercheck(arg):
    name = ''.join(arg)
    subprocess.run(['python', 'commands//playercheck.py', name])

def do_checkpassword(arg):
    serverip, server_port, version, bot_name, password = arg
    subprocess.run(['node', 'commands//checkpassword.js'] + arg)

def do_help():
    subprocess.run(['python', 'commands//help.py'])

actions = {
    'servercheck':do_servercheck,
    'domainsbruteforce':do_domainsbruteforce,
    'botsjoining': do_botsjoining,
    'playercheck': do_playercheck,
    'checkpassword': do_checkpassword,
    'help': do_help
}

print_penguinmc()

def menu():
    arg = input("PenguinMC> ").split()
    if arg[0] in actions and len(arg) <2:
        actions[arg[0]]()
    elif arg[0] in actions:
        actions[arg[0]](arg[1:])
    else:
        print(f'unknown command: {arg[0]} write help for list of commands')
while True:
    menu()