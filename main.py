import hikari
import discord
import lightbulb
import typing
import os
import random

bot = lightbulb.BotApp(
    token = os.environ['TOKEN']
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started!')

#ping pong 
@bot.command()
@lightbulb.command('ping', 'Says Pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

#bonk name
@bot.command()
@lightbulb.option("name", "put someones name here", modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.command("bonk", "Bonk someone with a gif")
@lightbulb.implements(lightbulb.SlashCommand)
async def bonk(ctx: lightbulb.context) -> None:
    cur_dir = os.getcwd()
    h = random.choice(os.listdir(cur_dir+r"/gifs/"))
    await ctx.respond(hikari.File(cur_dir+r"/gifs/" + h))
    await ctx.respond(f"{ctx.options.name} was bonked by {ctx.author.mention}")

bot.run()