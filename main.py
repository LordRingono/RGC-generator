import discord
import os
from discord.ext import *
from random import *
import discord.ext.commands as commands
from discord.ui import Button, View
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '%', intents = intents)
token = os.environ['DISCORD_TOKEN']
classes = ["voleur(e)", "prêtre(esse)", "guerrier(re)", "mage", "inutile", "clerc(e?)", "roublard(e)", "barbare", "barde", "druide(esse)", "moine", "paladin(e)", "rôdeur(euse)", "ensorceleur(euse)", "occultiste"]
@bot.event
async def on_ready():
  print("Bot connecté en tant que {0.user} !".format(bot))

@bot.command()
async def ping(ctx):
   await ctx.respond("This is a button!")
@bot.command()
async def hello(ctx):
  await ctx.send(random.choice(classes))
  button = Button(label="clique moi", style=discord.ButtonStyle.primary)
  view = View()
  view.add_item(button)
  await ctx.send("hi", view=view)
  async def button_callback(interaction):
    await interaction.response.send_message("Hey")
  button.callback = button_callback
@bot.command()
async def generate(ctx):
  race = ""
  classe = random.choice(classes)
  humain = Button(label="Humain", style=discord.ButtonStyle.primary)
  elf = Button(label="Elfe", style=discord.ButtonStyle.primary)
  nain = Button(label="Nain", style=discord.ButtonStyle.primary)
  gnome = Button(label="Gnome", style=discord.ButtonStyle.primary)
  # ici, on crée les différents bouttons
  view = View()
  view.add_item(humain)
  view.add_item(elf)
  view.add_item(nain)
  view.add_item(gnome)
  # ici, je les ajoutes a ma variable view
  await ctx.send("choisis une race", view=view)
  async def button4_callback(interaction):
    race = "Gnome(ide) "
    humain.disabled = True
    elf.disabled = True
    nain.disabled = True
    gnome.disabled = True
    final = race + classe
    await interaction.message.edit(content=final, view=view)
   
    await interaction.response.send_message("")
    
  async def button3_callback(interaction):
    race = "Nain(e) "
    humain.disabled = True
    elf.disabled = True
    nain.disabled = True
    gnome.disabled = True
    final = race + classe
    await interaction.message.edit(content=final, view=view)
   
    await interaction.response.send_message("")
    
  async def button2_callback(interaction):
    race = "Elfe "
    humain.disabled = True
    elf.disabled = True
    nain.disabled = True
    gnome.disabled = True
    final = race + classe
    await interaction.message.edit(content=final, view=view)
   
    await interaction.response.send_message("")
    
    
  async def button1_callback(interaction):
    race = "Humain(e) "
    humain.disabled = True
    elf.disabled = True
    nain.disabled = True
    gnome.disabled = True
    final = race + classe
    await interaction.message.edit(content=final, view=view)
    await interaction.response.send_message("")
  # ici, nous avons les cifférents callbacks
  humain.callback = button1_callback
  elf.callback = button2_callback
  nain.callback = button3_callback
  gnome.callback = button1_callback
  # ici, on définis quel callback vas avec quel boutton
bot.run(token)
