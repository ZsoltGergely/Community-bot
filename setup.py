from classes import *
from db_functions import *
from discord_functions import *
import discord
from discord.utils import get
from discord.ext import commands
import datetime
import asyncio
import mysql.connector

colors = discord.Color
bot = commands.Bot(command_prefix='&')

mydb = mysql.connector.connect(
    host="89.37.194.114",
    user="testuser",
    password="h=ik.vREx+EMWuNyim!Zsd.c",
    database="communities_test"
)


mycursor = mydb.cursor(buffered=True)


@bot.event
async def on_ready():
    print('logged in as')
    # print(CLIENT.user.name)
    print(bot.user.name)
    await bot.change_presence(activity=discord.Activity(name="Testtiiing", type=1))
    if mydb:
        print('Mysql connection successfull')
    print('Done!')



@bot.command()
async def test(message, arg1, *, arg2):
    await message.send('You passed {} and the rest is {}'.format(arg1, arg2))
    print(message.author)
    print(message.message)
    print(message.guild)

async def createcomm(message, arg1, *, arg2):
    await message.send('You passed {} and the rest is {}'.format(arg1, arg2))
    print(message.author)
    print(message.message)
    print(message.guild)


# test = Comm_Guild_class(2, 5, 7584783048238)
# print(test.id)
# print(test.emotes)
# print(test.invite_channel_id)
# print("---------")
# try:
#     ass = test.create_comm("Hell")
# except UserNameAlreadyUsed:
#     print ("ass")
# print(ass.id)
# print(ass.name)
# print("---------")
# print(ass.Comm_Guild.id)
# print(ass.Comm_Guild.invite_channel_id)


bot.run('NjY4Mjc2Mjk1ODUwOTE3OTE4.XiO6zA.l7LV6fRbvDpFGuNkkS5DlFPSpSk')
