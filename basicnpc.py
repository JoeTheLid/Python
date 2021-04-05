import random
import discord
import os
from dotenv import load_dotenv
load_dotenv()

def npcGender():
    randgend = (random.randint(1,100))
    if randgend < 49:
        gender = 'Male'
    elif randgend < 98:
        gender = 'Female'
    else:
        gender = 'Trans/Nonbinary'
    return gender
def npcAge():
#age
    randage = (random.randint(1,3))
    if randage == 1:
        age = 'Young'
    elif randage == 2:
        age = 'Middle Aged'
    else:
        age = 'Old'
    return(age)
def npcOrigin():
        #Nationality
        randnationality = (random.randint(1,100))
        if randnationality < 70:
            nationality = 'local parts'
        elif randnationality < 80:
            nationality = 'other parts of the country'
        elif randnationality < 90:
            nationality = 'a foreign neighbour'
        elif randnationality < 98:
            nationality = 'distant lands'
        else:
            nationality = 'inhuman realms'
        return(nationality)
def npcFeatures():
    #features
    randfeature = (random.randint(1,21))
    featureslist ={1: 'Unremarkable',
    2: 'Attractive',
    3: 'Stoop backed',
    4: 'Injured: Noticeable limp',
    5: 'Freckled',
    6: 'Extremely tanned',
    7: 'Speaking with a strong accent',
    8: 'Injured: Broken nose',
    9: 'Wild haired',
    10:'Bearing an untrustworthy smile',
    11:'Carrying a child',
    12:'Badly pockmarked',
    13:'Strangely attired',
    14:'Extremely tall',
    15:'Extremely short',
    16: 'Blind',
    17: 'Deaf',
    18: 'Mute',
    19: 'Surrounded by animals',
    20: 'Cursed',
    21: 'Blessed'}
    return(featureslist[randfeature])
def npcAttitude():
    #attitude
    randattitude = (random.randint(1,10))
    attitudelist = {
    1: 'Friendly (Seeking stories)',
    2: 'Indifferent (Busy)',
    3: 'Hostile (Bad attitude)',
    4: 'Friendly (Seeking companionship)',
    5: 'Hostile (Looking for a fight)',
    6: 'Indifferent (Selling something)',
    7: 'Friendly\Hostile (Mistakes you for an old acquaintance)',
    8: 'Indifferent (Bored)',
    9: 'Friendly (Needs help with something minor)',
    10: 'Hostile (Prejudiced against someone)'
    }
    return(attitudelist[randattitude])
def quicknpc():
    return 'A {} {} from {} who is {} and is {}'.format(npcAge(),npcGender(),npcOrigin(),npcFeatures(),npcAttitude())

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gender'):
        await message.channel.send('{}'.format(npcGender()))
    if message.content.startswith('$age'):
        await message.channel.send('{}'.format(npcAge()))
    if message.content.startswith('$origin'):
        await message.channel.send('{}'.format(npcOrigin()))
    if message.content.startswith('$feature'):
        await message.channel.send('{}'.format(npcFeatures()))
    if message.content.startswith('$attitude'):
        await message.channel.send('{}'.format(npcAttitude()))
    if message.content.startswith('$npc'):
        await message.channel.send('{}'.format(quicknpc()))

client.run(os.getenv('TOKEN'))
