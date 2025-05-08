from mcstatus import JavaServer
import os
import threading
import lodestone
import random
import time

def servercheck():
    serverip = input("Enter Minecraft Server IP: ")
    server_port = input("Enter a Port: ")
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



def botjoining():
    # quest all things required
    server_ip = input('enter an server ip: ')
    server_port = input('enter an server port: ')
    bot_name = input('name of bots: ')
    bots_amount = int(input('amount of bots: '))
    bots_time = int(input('time in the servers: '))

    if bots_amount > 1:
        for bot_amount in range(bots_amount):
            # modify de bots name to a different name for each bot
            random_num = random.randint(1, 1000000)
            random_num = str(random_num)
            bot_name_new = bot_name+'_'+random_num
            print(bot_name_new)
            # create bots
            bot = lodestone.createBot(
                host=server_ip,
                port=server_port,
                username=bot_name_new,
                auth='offline'
            )
            # connect bots
            bot.connect()
            print(f'bot: {bot_name_new} join')
        time.sleep(bots_time)
        for bot_amount in range(bots_amount):
            print('disconnecting bots')
            bot.disconnect()
botjoining()
