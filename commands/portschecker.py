from rstatus import RStatusClient
import sys

def checkport(file):
    with open(file, encoding='utf-8') as portsfile:
        readedfile = portsfile.readlines()
        for row in readedfile:
            row = row.strip()
            try:
                client = RStatusClient(row)
                server_data = client.get_server_data(bot=False)
                print(f'{row} - IP Adress: {server_data.ip_address} Players: {server_data.players.online}')
            except (TimeoutError, ConnectionRefusedError) as e:
                print(f'{row} - isnt open')
            except Exception as e:
                print(e)
checkport(sys.argv[1])