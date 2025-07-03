import discord
from discord.ext import commands
import os, random
import requests
from modelo import *
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

datos_curiosos_gatos = [
    "Los gatos pueden girar sus orejas 180 grados.",
    "Tienen cinco dedos en las patas delanteras, pero solo cuatro en las traseras.",
    "Un gato puede saltar hasta seis veces su longitud.",
    "Los gatos duermen entre 13 y 16 horas al día.",
    "Se comunican más con los humanos que con otros gatos mediante maullidos.",
    "Cada gato tiene un patrón de nariz único, como las huellas digitales humanas.",
    "Los bigotes de los gatos les ayudan a medir espacios y detectar cambios en el aire.",
    "Pueden ver en condiciones de luz muy baja gracias a una capa reflectante en sus ojos llamada tapetum lucidum.",
    "Los gatos no pueden saborear lo dulce.",
    "Ronronean tanto cuando están felices como cuando están estresados o heridos, posiblemente para curarse."
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ver_me(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            file_name = archivo.filename
            file_url = archivo.url
            await archivo.save(f"./img/{file_name}")
            await ctx.send(f"Su imagen se almaceno en la ruta: ./img/{file_url} ")
            class_name, confidence_score = get_class(f"./img/{file_name}")
            confidence_score = confidence_score*100
            respuesta = f"**Predicción:** {class_name}\n **Certeza: **{confidence_score:.0f} %"
            await ctx.send(respuesta)
            if class_name.strip() == "IMG_reales":
                await ctx.send(random.choice(datos_curiosos_gatos))
            else:
                await ctx.send("La imagen es IA")
    else:
        await ctx.send("No se ingresó ninguna imagen :( ")

            
bot.run("Test") 