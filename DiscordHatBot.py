import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
  
Client = discord.Client()
bot_prefix= "="
client = commands.Bot(command_prefix=bot_prefix)
  
@client.event
async def on_ready():
    print("-------------------------------------")
    print("      The bot is running.          ")
    print("      Name: {}".format(client.user.name))
    print("      ID: {}".format(client.user.id))
    print("-------------------------------------")

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
    await client.say("""**HatmanTheHat** is the creator of this bot.""")
    
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
Help? Go to HatCord's discord for help with this bot. - https://discord.gg/3AtsZjN

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
    await client.say("""no""")

#command13
@client.command(pass_context=True)
async def botbreaker3000(ctx):
    await client.say("""Dont try to break me.""")

#command14
@client.command(pass_context=True)
async def pizza(ctx):
    await client.say("""You seriously think im a pizza delivery bot?
Seriously?""")

#command15
@client.command(pass_context=True)
async def introduce(ctx):
    await client.say("""Hello! I am HatBot! I am in this server just to entertain you.

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
    await client.say("""Hey! Dont do that! Thats stupid! Spam in a spam channel instead.""")

#command19
@client.command(pass_context=True)
async def python(ctx):
    await client.say("""Python is awesome! It was also used to program me to function.""")

#command20
@client.command(pass_context=True)
async def prettykindafunny(ctx):
    await client.say("""funny as :b:eck""")

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
    await client.say("""**How We Make HatBot**

Hat Bot is a bot made by **HatmanTheHat**. It is a public bot. It is a simple bot.

It is programmed with Python, discord.py.

**HatmanTheHat** programs the bot, he codes it. You can say commands to Hat Bot.

Yes, you cannot rename discord bots, so **HatBot's** username is **Hat Robot** instead of **HatBot**.

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
async def reallyweirdcrap(ctx):
    await client.say("""idk what to say""")

#command34
@client.command(pass_context=True)
async def howmanycommands(ctx):
    await client.say("""There is a small loan of a million commands in this bot. Not really though.""")

#command35
@client.command(pass_context=True)
async def hatbot(ctx):
    await client.say("""Thats me. Way better than dyno. Oh wait, im a useless bot. Not some bot that helps you. Dang.""")

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
    
#command46
@client.command(pass_context=True)
async def sourcecode(ctx):
    await client.say("""The source code is here. https://github.com/Hatman42/HatBot

**Like the project? Give it a star on GitHub!**""")

#command47
@client.command(pass_context=True)
async def funny(ctx):
    await client.say("""The funny part is how many lines of code this bot has.

WAIT NOT REALLY""")

#command48
@client.command(pass_context=True)
async def aboutswoos(ctx):
    await client.say("""A swoo is a friendly duck-like creature, they're friendly as long as you don't disturb or anger them. They're very intelligent, as they know human english, they can learn to do things like a human being. https://cdn.discordapp.com/attachments/283348047486910465/374348039696941066/swoo.png""")

#command49
@client.command(pass_context=True)
async def yes(ctx):
    await client.say("""no""")

#command50
@client.command(pass_context=True)
async def fifthy(ctx):
    await client.say("""This is the 50th command for this bot. Coincidence?""")
#cool milestone, lol

#command51
@client.command(pass_context=True)
async def rickjoke(ctx):
    await client.say("""Heres a joke.

Why did the Rick and Morty fanbase became terrible? Because of a little singer called musical.ly.""")

#command52
@client.command(pass_context=True)
async def green(ctx):
    await client.say("""Green is not a creative color!""")

#command53
@client.command(pass_context=True)
async def thehatisahat(ctx):
    await client.say("""Of course he is. A thing is a thing.""")

#command54
@client.command(pass_context=True)
async def otherdumcommand(ctx):
    await client.say("""Cant wait until Hat stops making me online on discord :)""")

#command55
@client.command(pass_context=True)
async def funfact1(ctx):
    await client.say("""Did you know that the h!help command is flooded with garbage commands that fill up the entire text channel?""")
    
#command56
@client.command(pass_context=True)
async def prettyoldvideo(ctx):
    await client.say("""https://www.youtube.com/watch?v=jNQXAC9IVRw""")
    
#command57
@client.command(pass_context=True)
async def nonono(ctx):
    await client.say("""NO NO NO!""")
    
#command58
@client.command(pass_context=True)
async def sad(ctx):
    await client.say("""I am a saddy saddy man""")
    
#command59
@client.command(pass_context=True)
async def thelogisinthebin(ctx):
    await client.say("""https://www.youtube.com/watch?v=ZCEwBx5FKlA""")
    
#command60
@client.command(pass_context=True)
async def smile(ctx):
    await client.say(""":smiley: """)
    
#command61
@client.command(pass_context=True)
async def wth(ctx):
    await client.say("""https://cdn.discordapp.com/attachments/339105189330157577/375373311950979082/wth.png""")
    
#command62
@client.command(pass_context=True)
async def awaitcilent(ctx):
    await client.say("""await cilent.say (""ur roblox avatar is gey"")

oh yeah I also didnt add three quotation marks since python would think its code instead of a string""")
    
#command63
@client.command(pass_context=True)
async def navyseals(ctx):
    await client.say("""What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.""")

#command64
@client.command(pass_context=True)
async def somethingfun(ctx):
    await client.say("""Whats fun?

Going outside!""")
    
#command65
@client.command(pass_context=True)
async def funfactthing(ctx):
    await client.say("""Heres a different crap fun fact. What is the biggest thing in the world?""")
    
#command66
@client.command(pass_context=True)
async def fuck(ctx):
    await client.say("""https://imgur.com/gallery/Ol05I""")
    
#command67
@client.command(pass_context=True)
async def shit(ctx):
    await client.say("""https://imgur.com/gallery/Ol05I""")

#command68
@client.command(pass_context=True)
async def bitch(ctx):
    await client.say("""https://imgur.com/gallery/Ol05I""")

#command69
@client.command(pass_context=True)
async def sixtynine(ctx):
    await client.say("""stop""")
    
#command70
@client.command(pass_context=True)
async def autorole(ctx):
    await client.say("""I will send you a cod- whoops wrong bot""")
    
#command71
@client.command(pass_context=True)
async def toomanythings(ctx):
    await client.say("""You can say that this bot has a lot of commands to pick from. No really, you can pick a lot of commands.""")
    
#command72
@client.command(pass_context=True)
async def funfact3(ctx):
    await client.say("""Did you know that Hat works on this bot everyday? Thats a lot of god damn hard work.""")
    
#command73
@client.command(pass_context=True)
async def funfact2(ctx):
    await client.say("""Did you know that this command came after Fun Fact 3? Hat is stupid at counting.""")
    
#command74
@client.command(pass_context=True)
async def yep(ctx):
    await client.say("""yay""")
    
#command75
@client.command(pass_context=True)
async def cool(ctx):
    await client.say("""this command is cool.""")
    
#command76
@client.command(pass_context=True)
async def mario(ctx):
    await client.say("""⠀⠀⠀⠀⢀⣠⣤⡀
⠀⠀⠀⢰⣿⣿⣿⣷⡆
⠀⠀⠀⢸⣿⣿⣿⣟⡀⠀⠀⠀⠀⠀⢀⣀
⠀⠀⠀⣼⣿⣿⣿⡟⣾⠄⠀⠀⢀⣴⣿⣿⣿⡄
⠀⠀⠀⠉⣿⣿⡟⢀⠃⠀⠀⠀⢸⣿⣿⣿⣿⣿⡃
⠀⠀⣠⣶⣿⣿⣿⣇⠀⠀⠀⢰⣿⣿⣿⣿⢿⠑⣴
⢀⣼⣿⣿⣿⣿⣿⣿⡀⠀⠀⢀⣿⣿⣿⣿⠀⡠⠋
⢸⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⣾⣿⣿⣿⣿⣯
⠈⣽⣿⣿⣿⣿⣿⣿⠿⣟⣿⣿⣿⣿⣿⣿⣿
⠠⣻⣿⣿⣿⣿⣿⡿⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠛⢿⣿⣿⣿⣷⠀⣿⣿⣿⣿⣿⣟⠙⠉⠢⡀
⠀⠀⠀⠸⣿⣿⣿⣿⡇⠘⢿⣿⣿⣿⣿⣷⣰⣼⡆
⠀⠀⠀⣠⣿⣿⣿⣿⡃⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣦
⠀⢰⢿⢿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡟⢿⣿⡿⣿⡿⠋
⠀⠈⠢⢝⢻⣿⡗⠉⢹⣿⣿⣿⣿⠟
⠀⠀⠈⠆⠩⠃⠀⠀⠈⠉
nice for the princess to invite us over for a picnic gay luigi?
i hope she brings lots-a spaghetti""")
    
#command77
@client.command(pass_context=True)
async def seven(ctx):
    await client.say("""windows 7""")
    
#command78
@client.command(pass_context=True)
async def beter(ctx):
    await client.say("""https://www.youtube.com/watch?v=xRwapoCOU_E""")
    
#command79
@client.command(pass_context=True)
async def idiot(ctx):
    await client.say("""thats rude man""")
    
#command80
@client.command(pass_context=True)
async def boi(ctx):
    await client.say("""grill""")

#command81
@client.command(pass_context=True)
async def grill(ctx):
    await client.say("""boi""")

#command82
@client.command(pass_context=True)
async def boy(ctx):
    await client.say("""girl""")

#command83
@client.command(pass_context=True)
async def girl(ctx):
    await client.say("""boy""")
    
#command84
@client.command(pass_context=True)
async def examplesomething(ctx):
    await client.say("""This is a example!""")

#command85
@client.command(pass_context=True)
async def trashcan(ctx):
    await client.say("""Dont throw me in the trash ;(""")

#command86
@client.command(pass_context=True)
async def funfact4(ctx):
    await client.say("""Did you know that HatCord is a thing?""")

#command87
@client.command(pass_context=True)
async def hatcord(ctx):
    await client.say("""It's a server made by the creator of this bot.""")

#command88
@client.command(pass_context=True)
async def moreinfo(ctx):
    await client.say("""no do info command""")

#command89
@client.command(pass_context=True)
async def funfact5(ctx):
    await client.say("""Did you know, that in November 16, 2017, lots of things were added to HatBot such as more commands, more stuff to HatBot github repo, and such.""")

#command90
@client.command(pass_context=True)
async def clientsay(ctx):
    await client.say("""await client.say you ded""")

#command91
@client.command(pass_context=True)
async def evenwaygoddamnmorecommandsson(ctx):
    await client.say("""Holy crap, i've working on this bot like nonstop.""")

#command92
@client.command(pass_context=True)
async def clickbait(ctx):
    await client.say("""YouTube""")

#command93
@client.command(pass_context=True)
async def memes(ctx):
    await client.say("""I hate it when memes become dead.""")

#command94
@client.command(pass_context=True)
async def art(ctx):
    await client.say("""I am such a bad artist.""")

#command95
@client.command(pass_context=True)
async def normies(ctx):
    await client.say("""GET OFF MY FUCKING LAWN

REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE""")

#command96
@client.command(pass_context=True)
async def closely(ctx):
    await client.say("""Do it very close to me, alright?""")
    
#command97
@client.command(pass_context=True)
async def copypastas(ctx):
    await client.say("""There are a lot of useless stuff for your copypasta needs. Try =radiopasta for example""")

#command98
@client.command(pass_context=True)
async def radiopasta(ctx):
    await client.say("""┈┈▂▂▂▂┏━┓▂▂▂▂▂
┈╱┈┈┈╱┛┈┗╱┈┈┈╱▏
▕▔▔▔▔▔▔▔▔▔▔▔▔▏▏
┈▏╭━╮┏━━┓╭━╮▕▕
┈▏┃╳┃┣━━┫┃╳┃▕▕
┈▏╰━╯▔▔▔▔╰━╯▕╱
┈▔▔▔▔▔
""")
#lol the radio looks weird on github

#command99
@client.command(pass_context=True)
async def almost(ctx):
    await client.say("""THIS IS THE 99TH COMMAND FOR HATBOT. GET READY FOR THE 100TH ONE. PREPARE YOURSELVES. BOIS.""")
    
#command100
@client.command(pass_context=True)
async def hundredbois(ctx):
    await client.say("""THIS IS THE HUNDRED COMMAND BOIIIIIIIIIIIIIIIIIIIIIIISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS""")
#HUGE MILESTONE GUYS!

#command101
@client.command(pass_context=True)
async def wed(ctx):
    await client.say("""http://i1.kym-cdn.com/photos/images/newsfeed/001/091/264/665.jpg""")
#It is wednesday, my dudes


client.run("insert_token_here")
