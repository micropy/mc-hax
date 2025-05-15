from rstatus import RStatusClient
import sys

def servercheck(args):
    try:
        # Get Java Server status
        client = RStatusClient(args)
        server_data = client.get_server_data(bot=False)
        if server_data:
                print(f"IP: {server_data.ip_address} Players Online: {server_data.players.online}")
    except Exception as e:
        print(e)
servercheck(sys.argv)