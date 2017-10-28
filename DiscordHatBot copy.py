import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
  
Client = discord.Client()
bot_prefix= "h!"
client = commands.Bot(command_prefix=bot_prefix)
  
@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def rules(ctx):
    await client.say("""Read in the #rules channel ya doofus""")
#command1
@client.command(pass_context = True)
async def invite(ctx):
    x = await client.invites_from(ctx.message.server)
    x = ["<" + y.url + ">" for y in x]
    print(x)
    embed = discord.Embed(title = "Invite Links", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
  
#command2
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
  
#command3
@client.command(pass_context=True)
async def hat(ctx):
    await client.say("""man42""")
  
#command4
@client.command(pass_context=True)
async def abouthat(ctx):
    await client.say("""**HatmanTheHat** is the creator of this Discord.""")
    
#command5
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
 
#command6
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to ban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
 
#command7
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFFDF00)
    return await client.say(embed = embed)
 
#command8
@client.command(pass_context = True)
async def listservers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
 
#command9
@client.command(pass_context = True)
async def info(ctx):
    await client.say("""**Useful Links:**
Discord Invite so you can invite friends here: https://discord.gg/3AtsZjN
 
Roles:
@OWNER - Hat himself, runs the server.
@Staff  - Helps moderate the server.
@Mod - Dunno, pretty much the same as Staff but a different role.
@CO-OWNER - Hes PokeTerrarian!
 
Any issues please **PM** HatmanTheHat directly.
 
Do you wanna see HatmanTheHats ROBLOX Profile? **Go here:** https://www.roblox.com/users/86121841/profile""")

#command10
@client.command(pass_context=True)
async def hi(ctx):
    await client.say("""hello!""")

#command11
@client.command(pass_context=True)
async def abouthatbot(ctx):
    await client.say("""**Hat Bot** is a bot programmed by HatmanTheHat.
The point of the bot is to mess around it. Thats all.""")

#command12
@client.command(pass_context=True)
async def pingstaff(ctx):
    await client.say("""Ping the staff yourself doofus.""")

#command13
@client.command(pass_context=True)
async def botbreaker3000(ctx):
    await client.say("""Dont try to break me motherfucker""")

#command14
@client.command(pass_context=True)
async def pizza(ctx):
    await client.say("""You seriously think im a pizza delivery bot?
Seriously?""")

#command15
@client.command(pass_context=True)
async def introduce(ctx):
    await client.say("""Hello! I am Hat Bot! I am in this server just to entertain you.

Now I dont know what to say anymore.""")

#command16
@client.command(pass_context=True)
async def discord(ctx):
    await client.say("""Im chatting there right now.""")

#command17
@client.command(pass_context=True)
async def ping(ctx):
    await client.say(""":ping_pong: Pong!""")

#command18
@client.command(pass_context=True)
async def spam(ctx):
    await client.say("""Hey! Dont do that motherfucker! Thats in the Hatcord Rules! Spam in #spam instead.""")

#command19
@client.command(pass_context=True)
async def python(ctx):
    await client.say("""Python is awesome! It was also used to program me to function.""")

#command20
@client.command(pass_context=True)
async def porn(ctx):
    await client.say("""I think im young to see porn. Join a fucking 18+ server.""")

#command21
@client.command(pass_context=True)
async def livestreams(ctx):
    await client.say("""how do you host a live stream""")

#command22
@client.command(pass_context=True)
async def discordtoken(ctx):
    await client.say("""You better not take my discord bot token.""")

#command23
@client.command(pass_context=True)
async def howwemakehatbot(ctx):
    await client.say("""**How We Make Hat Bot**

Hat Bot is a bot made by **HatmanTheHat**. It is not a public bot. It is in the HatCord Discord.

It is programmed with Python, discord.py.

**HatmanTheHat** programs the bot, he codes it. You can say commands to Hat Bot.

Yes, you cannot rename discord bots, so **Hat Bots** username is **Hat Robot instead of **Hat Bot**.

There is not much to say about this bot, this is the end of this. Ok bye""")

#command24
@client.command(pass_context=True)
async def hatminion(ctx):
    await client.say("""https://cdn.discordapp.com/attachments/339105189330157577/357620200058650625/anhatmanthehatminion.png""")

#command25
@client.command(pass_context=True)
async def gas(ctx):
    await client.say("""https://www.youtube.com/watch?v=atuFSv2bLa8""")

#command26
@client.command(pass_context=True)
async def discordremix(ctx):
    await client.say("""https://www.dropbox.com/s/vz54l782aafiupp/discordringtoneremix.mp3?dl=0 https://media.giphy.com/media/xT9IgvdW1TDCgWdyWQ/giphy.gif""")

#command27
@client.command(pass_context=True)
async def wumpus(ctx):
    await client.say("""https://pbs.twimg.com/profile_images/712436043014922240/fNa63qzP.jpg""")

#command27
@client.command(pass_context=True)
async def microchip(ctx):
    await client.say("""microchip is my friend ;)""")

#command28
@client.command(pass_context=True)
async def test(ctx):
    await client.say("""Testing123""")

#command29
@client.command(pass_context=True)
async def beep(ctx):
    await client.say("""boop""")

#command30
@client.command(pass_context=True)
async def house(ctx):
    await client.say("""You dont have a house, its a piece of land.
https://cdn.discordapp.com/attachments/333014727242416141/359831995028602880/house.png""")

#command31
@client.command(pass_context=True)
async def house2(ctx):
    await client.say("""Good job! Now you have a house :)
https://cdn.discordapp.com/attachments/333014727242416141/359683318641590282/house.png""")

#command32
@client.command(pass_context=True)
async def robloxremix(ctx):
    await client.say("""https://www.youtube.com/watch?v=QoPWhdRvScg&t""")

#command33
@client.command(pass_context=True)
async def fuckyou(ctx):
    await client.say("""Fuck you too. :middle_finger: """)

#command34
@client.command(pass_context=True)
async def howmanycommands(ctx):
    await client.say("""There is a small loan of a million commands in this bot. Not really though.""")

#command35
@client.command(pass_context=True)
async def hatbot(ctx):
    await client.say("""Thats me. Way better than dyno. Oh wait, im a useless bot. Not some bot that helps you. Fuck.""")

#command36
@client.command(pass_context=True)
async def CAPS(ctx):
    await client.say("""Please note the commands will not work if you type the commands in caps lock. It'll just show a python output error in Hats computer. Thank you.""")

#command37
@client.command(pass_context=True)
async def youranoutofideas(ctx):
    await client.say("""Thats hat when he types the billionth command for this bot.""")

#command38
@client.command(pass_context=True)
async def man42(ctx):
    await client.say("""hat""")

#command39
@client.command(pass_context=True)
async def fullhat(ctx):
    await client.say("""hatman42""")

#command40
@client.command(pass_context=True)
async def swoo(ctx):
    await client.say("""32""")

#command41
@client.command(pass_context=True)
async def batch(ctx):
    await client.say("""Batch command prompt files!""")

#command42
@client.command(pass_context=True)
async def vbs(ctx):
    await client.say("""Notepad scripting files!""")

#command43
@client.command(pass_context=True)
async def txt(ctx):
    await client.say("""Its a normal text file you can maybe use for your business work.""")

#command44
@client.command(pass_context=True)
async def hack(ctx):
    await client.say("""```
Hacking...
```
https://media.giphy.com/media/MGaacoiAlAti0/giphy.gif

**Done! You can hack here: http://hackertyper.net/**""")

#command45
@client.command(pass_context=True)
async def hatcordroblox(ctx):
    await client.say("""https://www.roblox.com/users/413383542/profile""")


client.run("your_own_code")
