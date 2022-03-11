import discord
from pynput.keyboard import Key, Controller
from time import sleep
from discord.ext import commands




keyboard = Controller()


client = discord.Client()


client.gamble = int(input("the money x"))


client.index_1 = 0
client.index_2 = 0
client.fmoney = ""


sleep(4)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)

    client.index_1 = 0
    client.index_2 = 0
    client.fmoney = ""

    if message.author == client.user:
        return

    if "$" in user_message and "437981" in user_message and username == "IdleRPG#8939":
        sleep(6)



        client.index_1 = user_message.index("!",user_message.index("!") + 1) -2
        client.index_2 = user_message.index("$")+1

        for i in range(client.index_2 , client.index_1):
            client.fmoney = client.fmoney + user_message[i]


        if "lost" in user_message:

            client.fmoney = str(int(client.fmoney) * 2)

            for i in range(len("$flip ")):
                keyboard.press("$flip "[i])
                keyboard.release("$flip "[i])

            for i in range(len(str(client.fmoney))):
                keyboard.press(client.fmoney[i])
                keyboard.release(client.fmoney[i])

            keyboard.press(Key.enter)
            keyboard.release(Key.enter)



        if "won" in user_message:

            for i in range(len("$flip ")):

                keyboard.press("$flip "[i])
                keyboard.release("$flip "[i])

            for i in range(len(str(client.gamble))):
                keyboard.press(str(client.gamble)[i])
                keyboard.release(str(client.gamble)[i])

            keyboard.press(Key.enter)
            keyboard.release(Key.enter)










TOKEN = "TYPE YOUR TOKEN HERE"



client.run(TOKEN)
