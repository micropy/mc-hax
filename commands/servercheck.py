from mcstatus import JavaServer
import sys

def servercheck(serverip, server_port):
    try:
        # Get Java Server status
        server = JavaServer.lookup(f"{serverip}:{server_port}")
        status = server.status()
        if status.latency <100:
            print("Server State: Excellent")
        elif status.latency >100 <200:
            print("Server State: Average")
        elif status.latency <200:
            print("Server Status: Bad")
        print(f"Server Latency> {status.latency}")
        print(f"Online Players: {status.players.online}")
    except Exception as e:
        print(e)
servercheck(sys.argv[1], sys.argv[2])