from mcstatus import JavaServer
import sys

def checkport(file):
    with open(file, encoding='utf-8') as portsfile:
        readedfile = portsfile.readlines()
        for row in readedfile:
            try:
                check = JavaServer.lookup(row)
                status = check.status
                print(f'{row} - latency: {status.latency} players: {status.players.online}')
            except (TimeoutError, ConnectionRefusedError) as e:
                print(f'{row} - isnt open')
            except Exception as e:
                print(e)
