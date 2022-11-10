from email import message
from http import server
from sys import prefix
from discord.ext import commands
import discord
from discord.utils import get
import time
import random

intents = discord.Intents.default()
intents.members = True
sentmessage = False
colorcount = 0
hicount = 0
prefix = "dg "
bot = discord.Client(intents=discord.Intents.all())

command_list = ('''
```diya's gf command list:

- john mulaney
- dg [rock,paper,scissors]
- perfect
- black
- rainbow,gay,fag
- faggot
- [kill myself,kms]
- kys
- cock
- ur mom
- disrespect```
''')

token = 'MTAyNjgwMzUxOTM4NDE5NTExMg.GCBYh7.FabSXReaBvuzpwgyrsjrnJ77CpiOSH1BrufTFI'

count = 0
dcount = 0
doingrainbow = False

@bot.event
async def on_ready():
    print("{0.user} is online!".format(bot))


@bot.event
async def on_message(message):
    global count
    global sentmessage
    global hicount
    global doingrainbow
    global dcount
    global scount
    global prefix
    global command_list
    if message.author.id == 1016285818777772032:
        scount = 0
        if scount == 0:
            scount = 1
            await message.channel.send("silence, ginger")
    elif message.author.id == 1026803519384195112:
        pass
    else:
        scount = 0
    if "disrespect" in message.content.lower():
        if scount == 0:
            scount = 1
            await message.channel.send("YOU DISRESPECC ME")
            await message.channel.send("YOU DISRESPECC MA FAMILY")
            await message.channel.send("YOU CALL US")
            time.sleep(1)
            await message.channel.send("**STINKY**")
            await message.channel.send("**POOPIE**")
            await message.channel.send("**BABIES**")
            await message.channel.send("YOU PUNCH MA WIFE")
            await message.channel.send("YOU KICK MA BABIE")
            await message.channel.send("YOU KICK MA FOOKIN BABY :sob:")
            await message.channel.send("YOU ATE OUR DOGGGG ")
            await message.channel.send("YOU ATE OUR HOUSEEE :whygodwhy:")
    elif "black" in message.content.lower():
        if scount == 0:
            scount = 1
            await message.channel.send("https://cdn.discordapp.com/attachments/1021393200138682388/1027550951164346459/frits_.jpg")
    elif message.content.lower() == "dg commands" or message.content.lower() == "dg cmds":
        if scount == 0:
            scount = 1
            await message.channel.send(command_list)
    elif "rainbow" in message.content.lower() or "gay" in message.content.lower() or "fag" in message.content.lower() or "faggot" in message.content.lower():
        if scount == 0:
            scount = 1
            if message.content.lower() == "faggot":
                await message.channel.send("https://cdn.discordapp.com/attachments/1027545759043813406/1027548643315679262/unknown.png")
            if doingrainbow == False:
                print("started rainbow sequence")
                doingrainbow = True
                member = message.author
                roletime = 0.01
                red = get(message.guild.roles, name="R")
                orange = get(message.guild.roles, name="O")
                yellow = get(message.guild.roles, name="Y")
                green = get(message.guild.roles, name="G")
                blue = get(message.guild.roles, name="B")
                purple = get(message.guild.roles, name="P")
                await member.add_roles(red)
                time.sleep(roletime)
                await member.remove_roles(red)
                await member.add_roles(orange)
                time.sleep(roletime)
                await member.remove_roles(orange)
                await member.add_roles(yellow)
                time.sleep(roletime)
                await member.remove_roles(yellow)
                await member.add_roles(green)
                time.sleep(roletime)
                await member.remove_roles(green)
                await member.add_roles(blue)
                time.sleep(roletime)
                await member.remove_roles(blue)
                await member.add_roles(purple)
                time.sleep(roletime)
                await member.remove_roles(purple)
                doingrainbow = False
                sentmessage = False
                print("stopped rainbow")
            else:
                if sentmessage == False:
                    sentmessage = True
        #elif message.author.id == 542077863503986709:
            #if scount == 0:
                    #scount = 1
                    #await message.channel.send("if u dont get the fuck back to our serial killer uwu marathon rn u fucking bitch ass faggot whore")
    elif "perfect" in message.content.lower():
        if scount == 0:
            scount = 1
            await message.channel.send("Perfect, Perfect, Perfect, Perfect")
    elif "kill myself" in message.content.lower() or "kms" in message.content.lower():
        if scount == 0:
            scount = 1
            if message.author.id == 542077863503986709:
                await message.channel.send("https://tenor.com/view/john-mulaney-no-mick-jagger-pointing-noo-gif-13962424")
            else:
                await message.channel.send("do it.")
    elif "kys" in message.content.lower():
        if message.author.id == 689948357510168623:
            if scount == 0:
                scount = 1
                await message.channel.send("diya actually shut the fuck up oh my fucking god")
        else:
            
            if scount == 0:
                scount = 1
                await message.channel.send("https://tenor.com/view/kys-keep-yourself-safe-low-tier-god-gif-24664025")

    elif "cock" in message.content.lower():
        if scount == 0:
            scount = 1
            if message.author.id == 689948357510168623:
                await message.channel.send("eat shit")
                dcount = dcount + 1
                if dcount == 10:
                    await message.channel.send("Shut the fuck up u fucking bottom stop trying to make me say balls")
                    dcount = 0
            else:
                await message.channel.send("Balls")
                member = message.author
            
                count = count + 1
                if count == 10:
                    await message.channel.send("Bro can u guys fucking stop :sob:")
                    count = 0

    elif message.content.lower() == "hi bot":
        if scount == 0:
            scount = 1
            hicount = hicount + 1
            if hicount == 1:
                await message.channel.send("the game")
            else:
                await message.channel.send("Hi!")

    elif "ur mom" in message.content.lower():
        if scount == 0:
            scount = 1
            n1 = random.randint(1,3)
            if n1 == 1:
                await message.channel.send("no, UR mom")
            elif n1 == 2:
                await message.channel.send("you know what, you know what")
                time.sleep(0.2)
                await message.channel.send("MY mom")
            elif n1 == 3:
                await message.channel.send("ur dad")
    elif message.content.lower() == prefix+"rock":
        if scount == 0:
            scount = 1
            n1 = random.randint(1,3)
            if n1 == 1:
                await message.channel.send("rock")
            elif n1 == 2:
                await message.channel.send("paper")
            elif n1 == 3:
                await message.channel.send("scissors")

    elif message.content.lower() == prefix+"paper":
        if scount == 0:
            scount = 1
            n1 = random.randint(1,3)
            if n1 == 1:
                await message.channel.send("rock")
            elif n1 == 2:
                await message.channel.send("paper")
            elif n1 == 3:
                await message.channel.send("scissors")

    elif message.content.lower() == prefix+"scissors":
        if scount == 0:
            scount = 1
            n1 = random.randint(1,3)
            if n1 == 1:
                await message.channel.send("rock")
            elif n1 == 2:
                await message.channel.send("paper")
            elif n1 == 3:
                await message.channel.send("scissors")
    
    elif "john mulaney" in message.content.lower():
        if scount == 0:
            scount = 1
            waittime = 0.3
            await message.channel.send("When i'm not with my girlfriend, you can do anything to me.")
            time.sleep(waittime)
            await message.channel.send("You can say anything to me.")
            time.sleep(waittime)
            await message.channel.send("Like, I will tolerate any treatment.")
            time.sleep(waittime)
            await message.channel.send("I travel alone sometimes and I’ll put up with anything.")
            time.sleep(waittime)
            await message.channel.send("I’ll book a ticket on some GARBAGE airline. And I don’t want to name an actual airline, so I’ll make one up- let’s call it like ‘Delta Airlines’.")
            time.sleep(waittime)
            await message.channel.send("So I’ll book a ticket on ‘Delta Airlines’.")
            time.sleep(waittime)
            await message.channel.send("And I’ll show up at the airport, and I’ll go, “Can I get on the plane now please?”.")
            time.sleep(waittime)
            await message.channel.send("And they go, “No! It’s delayed 9 hours!”.")
            time.sleep(waittime)
            await message.channel.send("And I go, “Okayyy~” And then I go to the bathroom.")
            time.sleep(waittime)
            await message.channel.send("And then I come out of the bathroom and I go, “Any updates?”.")
            time.sleep(waittime)
            await message.channel.send("And they go, “Yeah! We took off while you were in the bathroom! Because we hate you! Now take this meal voucher that doesn’t work, go fetch!”.")
            time.sleep(waittime)
            await message.channel.send("And I go, “Okayyy~” And I go over to the Wolfgang puck express and I go, “Can I have a sandwich, please?”.")
            time.sleep(waittime)
            await message.channel.send("And they go, “NO!!”.")
            time.sleep(waittime)
            await message.channel.send("And I go, “Okayyy~”.")
            time.sleep(waittime)
            await message.channel.send("And they go, “You’re a little fat girl, aren’t you?!” And I go. “Noooo~” And they go, “SAY IT!!” and I go, “I’m a little fat girl!”.")
            time.sleep(waittime)
            await message.channel.send("Then I go over to the Delta Helpdesk which is an oxymoron and I go, “Can I please go home on an airplane?”.")
            time.sleep(waittime)
            await message.channel.send("And they go, “No~! In fact- we’re gonna frame you for murder! And you’re going to jail for 30 years!!”.")
            time.sleep(waittime)
            await message.channel.send("And I go, “Why are you doing this to me??”.")
            time.sleep(waittime)
            await message.channel.send("And “they go, “Because we’re Delta airlines, and life if a fucking nightmare~!”.")
            time.sleep(waittime)


bot.run(token)