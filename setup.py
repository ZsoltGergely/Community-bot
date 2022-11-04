import discord
from discord.utils import get
from discord.ext import commands
import datetime
import asyncio
import mysql.connector
from classes import *
from db_functions import *
from discord_functions import *

colors = discord.Color
bot = commands.Bot(command_prefix='&')

mydb = mysql.connector.connect(
    host="IP",
    user="USERNAME",
    password="PASS",
    database="DB"
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

async def createcomm(message, name, *, mentions):
    guild_record = db_get_guild(message.guild.id)
    comm_guild = Comm_Guild_class(message.guild.id, int(guild_record[1]), int(guild_record[2]), message.guild)
    community = comm_guild.create_comm(name, message.mentions[0], message.role_mentions[0])
    db_insert_community(community.name, role_id, leader_id, guild_id)
    get_community_embed(name, leader_mention, role_mention, community_id)

#
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
