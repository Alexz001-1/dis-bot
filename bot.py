import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} ✅')
    keep_alive.start()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@tasks.loop(hours=6)
async def keep_alive():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send("Bot is alive! 🔥")
                break
            except:
                continue

bot.run(os.getenv("DISCORD_TOKEN"))
