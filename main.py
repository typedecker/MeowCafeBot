import discord, os, traceback

intents = discord.Intents(guilds = True, dm_messages = True, members = True, messages = True, guild_messages = True, invites = True)
client = discord.Client(chunk_guilds_at_startup = True, intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    game = discord.Game("Welcoming people to the MeowCafe!")
    await client.change_presence(activity = game)
    return

@client.event
async def on_member_join(member) :
    try :
        if member.dm_channel == None :
            await member.create_dm()
        await member.dm_channel.send('hello welcome to MeowCafe!')
        await member.guild.system_channel.send('hello ' + member.name + ' welcome to MeowCafe!')
    except Exception as err :
        print('Some error occured in the on_member_join function', Exception, err)
        traceback.print_exc()
    return

@client.event
async def on_member_remove(member) :
    return

@client.event
async def on_message(message):
    return

client.run(os.environ['BOT_TOKEN'])
