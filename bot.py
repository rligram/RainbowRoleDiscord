import asyncio
import random
import disnake
from disnake.ext import commands
from disnake.errors import Forbidden

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="r*", intents=intents)


@bot.event
async def on_ready():
  print("https://github.com/rligram")
  print("https://okrli.online")
  print("Credits to rli and original creators!")


@bot.slash_command(name='role',
                   description='Make your role a rainbow in your server!')
async def role(ctx, id: disnake.Role):
    if not ctx.author.guild_permissions.manage_roles:
        embed = disnake.Embed(
            description="You do not have permission to manage roles.",
            color=0x0c0c0c)
        await ctx.send(embed=embed)
        return
    try:
        if hasattr(bot.user, 'top_role'):
            if bot.user.top_role < id:
                embed = disnake.Embed(
                    description="I do not have permission to edit that role.",
                    color=0x0c0c0c)
                await ctx.send(embed=embed)
                return
        embed = disnake.Embed(description="Chill with your rainbow role!",
                                color=0x0c0c0c)
        await ctx.send(embed=embed)
        colours = [
            0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff,
            0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969
        ]
        role = disnake.utils.get(ctx.guild.roles, id=id.id)
        x = 0
        while (x != 1):
            await role.edit(colour=random.choice(colours))
            await asyncio.sleep(5)
    except Forbidden as e:
        print(e)

@bot.command()
async def role(ctx, id: disnake.Role):
          if not ctx.author.guild_permissions.manage_roles:
            embed = disnake.Embed(
                description="You do not have permission to manage roles.",
                color=0x0c0c0c)
            await ctx.send(embed=embed)
            return
          if hasattr(bot.user, 'top_role'):
             if bot.user.top_role < id:
               embed = disnake.Embed(
                   description="I do not have permission to edit that role.",
                   color=0x0c0c0c)
               await ctx.send(embed=embed)
               return

          embed = disnake.Embed(description="Chill with your rainbow role!",
                                color=0x0c0c0c)
          await ctx.send(embed=embed)
          colours = [
              0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff,
              0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969
          ]
          role = disnake.utils.get(ctx.guild.roles, id=id.id)
          x = 0
          while (x != 1):
            await role.edit(colour=random.choice(colours))
            await asyncio.sleep(5)

bot.run("token")
