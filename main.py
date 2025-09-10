import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN= os.getenv("DISCORD_TOKEN")
SUBDOMINIO = os.getenv("SUBDOMINIO")
URL = os.getenv("URL")

handler= logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members= True

bot= commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Jaime está preparado para abrir el Consum!", bot.user.name)

@bot.event
async def on_message(message):
    # Ignorar mensajes del propio bot
    if message.author.bot:
        return
    if message.content.lower() == "que tal jaime?":
        await message.channel.send(f"Estoy muy chill {message.author.mention}, preparado para abrir {SUBDOMINIO.upper()} cuando me lo pidas.")
        print(message.author.mention)

    await bot.process_commands(message)

@bot.command()
async def ip(ctx):
    embed= discord.Embed(
        title="IP del Servidor",
        description=URL,
        color= 0x00ff00
    )
    await ctx.send(embed=embed)

@bot.command()
async def consumcraft(ctx):
    embed = discord.Embed(
        title=f"{SUBDOMINIO.upper()} Server",
        description=f"Entra en el siguiente enlace e introduce el nombre del servidor ({SUBDOMINIO}) para iniciarlo:",
        color=0x0099ff
    )
    embed.add_field(
        name=" 🔗 Enlace:", 
        value="[Iniciar Servidor](https://falixnodes.net/startserver)", 
        inline=False
    )
    await ctx.send(embed=embed)

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
