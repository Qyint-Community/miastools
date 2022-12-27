import discord
from discord.ext import commands
from discord import AllowedMentions
intents = discord.Intents.all()
import asyncio
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import ytdl
import random
import datetime
from datetime import datetime
def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id
    return commands.check(predicate)
client = commands.Bot(command_prefix = '>', intents=intents, help_command=None, allowed_mentions=AllowedMentions(users=False, everyone=False),)
@client.event
async def on_ready():
    print('[miastools / main] » bot online!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='the Children in my Basement'))
#BGN

#
# SYSCOMMANDS
#
@client.command(aliases=['help', 'h', 'i'])
async def info(ctx):
    await ctx.send('» open source discord.py bot\n» v. 8.0.0\n» <https://qyint-community.github.io>\n»\n» list of modules:\n» **sysinfo**\n» `>ping`, `>info`\n» **randomx**\n» `>randomx`\n» **lmr**\n» `>lmr`, `>archwiki`\n» **audio**\n» `>a1\n» **music**\n» `>play [song], `>stop`, `>leave`, `>nowplaying`, (`loop, queueloop & shuffle are broken!`)\n» **roles**\n» `>roles`\n» **emojis**\n» `>send [emojiname]`\n» **owow**\n» `>owow`\n» **moddms**\n» *(qyint only)*\n» `>initmoddm [user] [de/en]`, `>moddm [user] (message)`\n» \n» **`>dm [message]` to send modmail**')
@client.command(aliases=['ping', 'p', 'f', 'pfetch'])
async def fetch(ctx):
    timestamp = datetime.now()
    await ctx.send(f'\n» mtv.: `v8.0.0`\n» ping: `{round(client.latency * 1000)}ms`\n» time: `{timestamp.strftime(r"%H:%M @ %d.%m.%Y")}`\n» uuid: `{ctx.author.id}`')
@client.command(aliases=['nfetch', 'neof', 'nf', 'neo', 'n'])
async def neofetch(ctx):
    timestamp = datetime.now()
    embed = discord.Embed(
        color = 0x5800ff,
        description = ctx.author.mention
    )
    embed.set_author(name=str(ctx.author))
    embed.add_field(name="Net", value=f'Time: `{timestamp.strftime(r"%H:%M @ %d.%m.%Y")}`\nPing: `{round(client.latency * 1000)}ms` <:xTelekom:977960354757886012>')
    embed.add_field(name="User", value=f'Created: `{ctx.author.created_at.strftime(r"%d.%m.%Y")}`')
    role_string = ' '.join([r.mention for r in ctx.author.roles][1:])
    embed.add_field(name="Roles [{}]".format(len(ctx.author.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])
#    embed.add_field(name="Guild permissions", value=perm_string, inline=True)
    embed.set_footer(text='UUID: ' + str(ctx.author.id))
    return await ctx.send(embed=embed)

#
# RandomX
#
@client.command(aliases=['r', 'random'])
async def randomx(ctx):
    await ctx.send('» use this plugin to generate random numbers!\n» commands: `>random[1-20]`')
@client.command(aliases=['r2', 'flip', 'coin', 'coinflip', 'random2', '1d2'])
async def randomxtwo(ctx):
    responses = ['1', '2']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r3', 'random3', '1d3'])
async def randomxthree(ctx):
    responses = ['1', '2', '3']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r4', 'random4', '1d4'])
async def randomxfour(ctx):
    responses = ['1', '2', '3', '4']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r5', 'random5', '1d5'])
async def randomxfive(ctx):
    responses = ['1', '2', '3', '4', '5']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r6', 'dice', 'roll', 'diceroll', 'random6', '1d6'])
async def randomxsix(ctx):
    responses = ['1', '2', '3', '4', '5', '6']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r7', 'random7', '1d7'])
async def randomxseven(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r8', 'random8', '1d8'])
async def randomxeight(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r9', 'random9', '1d9'])
async def randomxnine(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r10', 'random10', '1d10'])
async def randomxten(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r11', 'random11', '1d11'])
async def randomxeleven(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r12', 'random12', '1d12'])
async def randomxtwelve(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r13', 'random13', '1d13'])
async def randomxthirteen(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r14', 'random14', '1d14'])
async def randomxfourteen(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r15', 'random15', '1d15'])
async def randomxfifteen(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14', '15']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r16', 'random16', '1d16'])
async def randomxsixteen(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14', '15', '16']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r17', 'random17', '1d17'])
async def randomxseventeen(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14', '15', '16', '17']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r18', 'random18', '1d18'])
async def randomxeighteen(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14', '15', '16', '17', '18']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r19', 'random19', '1d19'])
async def randomxnineteen(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
    await ctx.send(f'» {random.choice(responses)}')
@client.command(aliases=['r20', 'random20', '1d20'])
async def randomxtwenty(ctx):
    responses = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    await ctx.send(f'» {random.choice(responses)}')

#
# LINUX MASTERRACE
#
@client.command(aliases=['linuxmr', 'linuxmasterrace', 'linux'])
async def lmr(ctx):
    await ctx.send('» currently unavailable!')
@client.command(aliases=['aw', 'wiki', 'archw', 'awiki', 'rtfm', 'rtm', 'readthefuckingmanual', 'readthemanual', 'manual'])
async def archwiki(ctx):
    await ctx.send('» <https://wiki.archlinux.org>')

#
# AUDIO
#
@client.command(pass_context=True, aliases=['audio1', 'dumm', 'kannessein', 'kannesseindassdudummbist', 'kannesseindaßdudummbist', 'bistdudumm'])
async def a1(ctx):
    await ctx.send(file=discord.File(r'./audio1.mp3'))

#
# MUSIC
#
#@client.command(pass_context=True, aliases=['play'])
#async def music(ctx, url):
#    await ctx.send('» loading...\n» (this might take a while.)\n»[make sure youre in a voice channel and provided a youtube link!]\n» playlists are not supported! work in progress')
#    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
#    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#    voice = get(client.voice_clients, guild=ctx.guild)
#    with YoutubeDL(YDL_OPTIONS) as ydl:
#        info = ydl.extract_info(url, download=False)
#        URL = info['formats'][0]['url']
#    channel = ctx.message.author.voice.channel
#    vc = await channel.connect()
#    vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#
#@client.command(aliases=['leave', 'stop', 'fuckoff'])
#async def pause(ctx):
#    await ctx.send('» left!')
#    vc = discord.utils.get(client.voice_clients, guild=ctx.guild)
#    await vc.disconnect()

from discordSuperUtils import MusicManager
MusicManager = MusicManager(client, spotify_support=False)

@client.command(aliases=['music', 'sing', 'song']))
async def play(ctx, *, query: str):
    await ctx.send('» loading...\n» *this might take a while*')
    await MusicManager.join(ctx)
    player = await MusicManager.create_player(query)
    await MusicManager.queue_add(player=player, ctx=ctx)
    if not await MusicManager.play(ctx):
        await ctx.send("» added!")
@client.command()
async def loop(ctx):
    is_loop = await MusicManager.loop(ctx)
    await ctx.send(f"» loop toggled to `{is_loop}`")
@client.command(aliases=['pause']))
async def stop(ctx):
    ctx.voice_client.stop()
    await ctx.send('» stopped!')
@client.command(aliases=['fuckoff', 'disconnect'])
async def leave(ctx):
    if await MusicManager.leave(ctx):
        await ctx.send("» left!")
@client.command(aliases=['next']))
async def skip(ctx, index: int = None):
    await MusicManager.skip(ctx, index)
    await ctx.send('» skipped!')
@client.command(aliases=['nowplaying', 'currentlyplaying', 'playing']))
async def np(ctx):
    if player := await MusicManager.now_playing(ctx):
        await ctx.send(f"» now playing: `{player}`")


#
# ROLES
#
@client.command(aliases=['role'])
async def roles(ctx):
    await ctx.send('» **role-list**\n»\n» **qyint-community**\n» `>keyrole [role] [user]` (Staff Only)\n» - *vrf*\n» `>assign [role] [user]` (Admin Only)\n» - *friend*\n» - *cm*\n» `>unlock [role] [user]` (Admin Only)\n» - *wvk*\n» - *3*\n» `>prom [role] [user]` (Admin Only)\n» - *staff*\n» - *cm*')
# AUTOROLES
#   Qyint
#       Member
@client.event
async def on_member_join(member):
    if member.guild.id == 909206946580672533:
        role = discord.utils.get(member.guild.roles, name=f'👤┇Member')
        await member.add_roles(role)
# ASSIGNEDROLES
#   Qyint
#       Assign (General)
@client.command(pass_context=True, aliases=['a', 'ar', 'assignrole'])
@commands.has_role(f'🧭┇Admin')
@is_in_guild(909206946580672533)
async def assign(ctx, arg, user: discord.Member):
    qyint_keyrole_vrf = discord.utils.get(ctx.message.guild.roles, name=f'🗣┇Keyrole VRF')
    qyint_role_friend = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Friend')
    qyint_staff_cm = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Community Management')
    qyint_staff_staff = discord.utils.get(ctx.message.guild.roles, name=f'⚙️┇Staff')
    qyint_unlr_wvk = discord.utils.get(ctx.message.guild.roles, name=f'🎖┇Weltverdienstkreuz')
    qyint_unlr_p3 = discord.utils.get(ctx.message.guild.roles, name=f'🥉┇Ich-bin-eine-gute-Person-Preis')
    if arg == 'key_vrf':
        await discord.Member.add_roles(user, qyint_keyrole_vrf)
        await ctx.send('» assigned keyrole **vrf**!')
    if arg == 'friend':
        await discord.Member.add_roles(user, qyint_role_friend)
        await ctx.send('» assigned **friend**!')
    if arg == 'techie':
        await discord.Member.add_roles(user, qyint_staff_cm)
        await ctx.send('» assigned **community manager**!')
    if arg == 'staff':
        await discord.Member.add_roles(user, qyint_staff_staff)
        await ctx.send('» assigned **staff**!')
    if arg == 'pwvk':
        await discord.Member.add_roles(user, qyint_unlr_wvk)
        await ctx.send('» assigned **weltverdienstkreuz**!')
    if arg == 'p3':
        await discord.Member.add_roles(user, qyint_unlr_p3)
        await ctx.send('» assigned **ich-bin-eine-gute-person-preis**!')
    modchannel = client.get_channel(1056785708183982120)
    await modchannel.send(f'» {ctx.author.mention} granted {user.mention} `{arg}`')
#       Keyroles
@client.command(pass_context=True, aliases=['k', 'kr', 'key', 'assignkeyrole'])
@commands.has_role(f'⚙️┇Staff')
@is_in_guild(909206946580672533)
async def keyrole(ctx, arg, user: discord.Member):
    qyint_keyrole_vrf = discord.utils.get(ctx.message.guild.roles, name=f'🗣┇Keyrole VRF')
    qyint_role_friend = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Friend')
    qyint_staff_cm = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Community Management')
    qyint_staff_staff = discord.utils.get(ctx.message.guild.roles, name=f'⚙️┇Staff')
    qyint_unlr_wvk = discord.utils.get(ctx.message.guild.roles, name=f'🎖┇Weltverdienstkreuz')
    qyint_unlr_p3 = discord.utils.get(ctx.message.guild.roles, name=f'🥉┇Ich-bin-eine-gute-Person-Preis')
    if arg == 'vrf':
        await discord.Member.add_roles(user, qyint_keyrole_vrf)
        await ctx.send('» assigned keyrole **vrf**!')
        modchannel = client.get_channel(1056785708183982120)
    await modchannel.send(f'» {ctx.author.mention} granted {user.mention} `{arg}`')
#       Unlockable Roles
@client.command(pass_context=True, aliases=['u', 'ul', 'unl', 'un', 'unlr', 'unlockrole'])
@commands.has_role(f'🧭┇Admin')
@is_in_guild(909206946580672533)
async def unlock(ctx, arg, user: discord.Member):
    qyint_keyrole_vrf = discord.utils.get(ctx.message.guild.roles, name=f'🗣┇Keyrole VRF')
    qyint_role_friend = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Friend')
    qyint_staff_cm = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Community Management')
    qyint_staff_staff = discord.utils.get(ctx.message.guild.roles, name=f'⚙️┇Staff')
    qyint_unlr_wvk = discord.utils.get(ctx.message.guild.roles, name=f'🎖┇Weltverdienstkreuz')
    qyint_unlr_p3 = discord.utils.get(ctx.message.guild.roles, name=f'🥉┇Ich-bin-eine-gute-Person-Preis')
    if arg == 'wvk':
        await discord.Member.add_roles(user, qyint_unlr_wvk)
        await ctx.send('» assigned **weltverdienstkreuz**!')
    if arg == '3':
        await discord.Member.add_roles(user, qyint_unlr_p3)
        await ctx.send('» assigned **ich-bin-eine-gute-person-preis**!')
        modchannel = client.get_channel(1056785708183982120)
    await modchannel.send(f'» {ctx.author.mention} granted {user.mention} `{arg}`')
#       Promote
@client.command(pass_context=True, aliases=['pr', 'promote', 'assignpromotion'])
@commands.has_role(f'🧭┇Admin')
@is_in_guild(909206946580672533)
async def prom(ctx, arg, user: discord.Member):
    qyint_keyrole_vrf = discord.utils.get(ctx.message.guild.roles, name=f'🗣┇Keyrole VRF')
    qyint_role_friend = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Friend')
    qyint_staff_cm = discord.utils.get(ctx.message.guild.roles, name=f'👥┇Community Management')
    qyint_staff_staff = discord.utils.get(ctx.message.guild.roles, name=f'⚙️┇Staff')
    qyint_unlr_wvk = discord.utils.get(ctx.message.guild.roles, name=f'🎖┇Weltverdienstkreuz')
    qyint_unlr_p3 = discord.utils.get(ctx.message.guild.roles, name=f'🥉┇Ich-bin-eine-gute-Person-Preis')
    if arg == 'staff':
        await discord.Member.add_roles(user, qyint_staff_staff)
        await ctx.send('» assigned **staff**!')
        modchannel = client.get_channel(1056785708183982120)
    if arg == 'cm':
        await discord.Member.add_roles(user, qyint_staff_cm)
        await ctx.send('» assigned **community manager**!')
        modchannel = client.get_channel(1056785708183982120)
    await modchannel.send(f'» {ctx.author.mention} granted {user.mention} `{arg}`')

#
# EMOJIS
#
@client.command()
async def send(ctx, arg):
    if arg == 'upvote':
        await ctx.send('<:xVoteUpvote:912384569058160640>')
    elif arg == 'downvote':
        await ctx.send('<:xVoteDownvote:912384569423044618>')
    elif arg == 'revolution':
        await ctx.send('<:xRevolution:912384574225539072>')
    elif arg == 'uhwhatthefuck':
        await ctx.send('<:xUhWhatTheFuck:912384578830876702>')
    elif arg == 'kekw':
        await ctx.send('<:xKekw:912384579283877910>')
    elif arg == 'gulag':
        await ctx.send('<:xGulag:912384589450858526>')
    elif arg == 'coffee1':
        await ctx.send('<:xCoffee1:912384591220858881>')
    elif arg == 'gun':
        await ctx.send('<:xGun:912384591388622899>')
    elif arg == 'cofee2':
        await ctx.send('<:xCoffee2:912384592131014686>')
    elif arg == 'happy':
        await ctx.send('<:xHappy:912384592370085969>')
    elif arg == 'jesus':
        await ctx.send('<:xJesus:912384594333011979>')
    elif arg == 'uharmy':
        await ctx.send('<:xUhArmy:912384594349785098>')
    elif arg == 'hmmcommunism':
        await ctx.send('<:xHmmCommunism:912384594806972476>')
    elif arg == 'plusoneup':
        await ctx.send('<:xPlusOneUp:912384595108958229>')
    elif arg == 'uhlaw':
        await ctx.send('<:xUhLaw:912384595297730612>')
    elif arg == 'trolldespair':
        await ctx.send('<:xTrollDespair:1002954544721973328>')
    elif arg == 'why':
        await ctx.send('<:xWhy:1002954620613701735>')
    elif arg == 'destroyedanddominated':
        await ctx.send('<a:xDestroyedAndDominated:1002954723034411150>')
    elif arg == 'shutthefuckup':
        await ctx.send('<a:xShutTheFuckUp:1002954755523485759>')
    elif arg == 'stfu':
        await ctx.send('<a:xShutTheFuckUp:1002954755523485759>')
    elif arg == 'catjam':
        await ctx.send('<a:xCatJam:1002954918862270484>')
    elif arg == 'neutraldance':
        await ctx.send('<a:xNeutralDance:1002954953167491142>')
    elif arg == 'clapyay':
        await ctx.send('<a:xClapYay:1002954991310491679>')
    elif arg == 'leave':
        await ctx.send('<a:xLeave:1002955015259959326>')
    elif arg == 'sadjam':
        await ctx.send('<a:xSadjam:1002955038089560104>')
    elif arg == 'finger':
        await ctx.send('<a:xFinger:1002955066027802766>')
    elif arg == 'gigachad':
        await ctx.send('<a:xGigachad:1002955245116194887>')
    elif arg == 'blep':
        await ctx.send('<a:xBlep:1002955272781832263>')
    elif arg == 'grogusip':
        await ctx.send('<a:xGroguSip:1002955311541395587>')
    elif arg == 'catdisco':
        await ctx.send('<a:xCatDisco:1002955338288463925>')
    elif arg == 'hop':
        await ctx.send('<a:xHop:1002955360958689391>')
    elif arg == 'hahahayouresofunny':
        await ctx.send('<a:xHAHAHAYOURESOFUNNY:1002955420773666906>')
    elif arg == 'giggles':
        await ctx.send('<a:xGiggles:1002955443565502566>')
    elif arg == 'noted':
        await ctx.send('<a:xNoted:1002955481452654732>')
    elif arg == 'pugdance':
        await ctx.send('<a:xPugDance:1002955591720894574>')
    elif arg == 'clapwow':
        await ctx.send('<a:xClapWow:1002955667952386138>')
    elif arg == 'oe':
        await ctx.send('<a:xOE:1002956564870742056>')
    elif arg == 'ö':
        await ctx.send('<a:xOE:1002956564870742056>')
    elif arg == 'icon':
        await ctx.send('<:icon:1006413678926639194>')
    elif arg == 'wowicon':
        await ctx.send('<:icon:1006413678926639194>')
    elif arg == 'wow':
        await ctx.send('<:icon:1006413678926639194>')
    elif arg == 'wtfread':
        await ctx.send('<:xWTFRead:1021604922371866664>')
    elif arg == 'australiandance':
        await ctx.send('<a:xAustralianDance:1026880342482755716>')
    elif arg == 'techjesus':
        await ctx.send('<:xTechJesus:1026944407506792548>')
    elif arg == 'doubt':
        await ctx.send('<:xDoubt:1026944997959942255>')
    elif arg == 'techstare':
        await ctx.send('<:xTechStare:1026945006818300027>')
    elif arg == 'happyjam':
        await ctx.send('<a:xHappyJam:1026945984305053757>')
    elif arg == 'tux_ourlordandsavior':
        await ctx.send('<:xTux_OurLordAndSavior:1026946308021432411>')
    elif arg == 'ourlordandsavior':
        await ctx.send('<:xTux_OurLordAndSavior:1026946308021432411>')
    elif arg == 'tux':
        await ctx.send('<:xTux_OurLordAndSavior:1026946308021432411>')
    elif arg == 'thumbsup_yeahyougotit':
        await ctx.send('<:xThumbsUp_YeahYouGotIt:1029111175100768276>')
    elif arg == 'yeahyougotit':
        await ctx.send('<:xThumbsUp_YeahYouGotIt:1029111175100768276>')
    elif arg == 'thumbsup':
        await ctx.send('<:xThumbsUp_YeahYouGotIt:1029111175100768276>')
    elif arg == 'telekom':
        await ctx.send('<:xTelekom:977960354757886012>')
    elif arg == 'paindisappear':
        await ctx.send('<a:xPainDisappear:1029378721456603196>')
    elif arg == 'sadrain':
        await ctx.send('<a:xSadRain:1029380189412659200>')
    elif arg == 'arguing':
        await ctx.send('<a:xArguing:1029438187602452522>')
    elif arg == 'coolcat':
        await ctx.send('<a:xCoolCat:1029436973489848411>')
    elif arg == 'fbiopenup':
        await ctx.send('<a:xFBIOpenUp_Feds:1029437068352442460>')
    elif arg == 'fbiopenup_feds':
        await ctx.send('<a:xFBIOpenUp_Feds:1029437068352442460>')
    elif arg == 'feds':
        await ctx.send('<a:xFBIOpenUp_Feds:1029437068352442460>')
    elif arg == 'getfucked':
        await ctx.send('<a:xGetFucked:1029437608582979654>')
    elif arg == 'huh':
        await ctx.send('<a:xHUH:1029437193606934618>')
    elif arg == 'headslam':
        await ctx.send('<a:xHeadSlam:1029437019220349039>')
    elif arg == 'jesustpose':
        await ctx.send('<a:xJesusTPose:1029436427701850133>')
    elif arg == 'jesus':
        await ctx.send('<a:xJesusTPose:1029436427701850133>')
    elif arg == 'tpose':
        await ctx.send('<a:xJesusTPose:1029436427701850133>')
    elif arg == 'loading':
        await ctx.send('<a:xLoading:1029437699968487524>')
    elif arg == 'loses':
        await ctx.send('<a:xLoses_NO:1029436061753020446>')
    elif arg == 'no':
        await ctx.send('<a:xLoses_NO:1029436061753020446>')
    elif arg == 'loses_no':
        await ctx.send('<a:xLoses_NO:1029436061753020446>')
    elif arg == 'pugdance':
        await ctx.send('<a:xPugDance:1029437738447011871>')
    elif arg == 'staff':
        await ctx.send('<a:xStaff:1029437561199927416>')
    elif arg == 'stealcat':
        await ctx.send('<a:xStealCat:1029437142046363739>')
    elif arg == 'therockeyebrow':
        await ctx.send('<a:xTheRockEyebrow:1029436849699160144>')
    elif arg == 'tomscottvapedisappear':
        await ctx.send('<a:xTomScottVapeDisappear:1029435512295014400>')
    elif arg == 'walterdies':
        await ctx.send('<a:xWalterDies:1029436029498834954>')
    elif arg == 'whoo_yeahbaby':
        await ctx.send('<a:xWhoo_YeahBaby:1029436044413775942>')
    elif arg == 'whoo':
        await ctx.send('<a:xWhoo_YeahBaby:1029436044413775942>')
    elif arg == 'yeahbaby':
        await ctx.send('<a:xWhoo_YeahBaby:1029436044413775942>')
    elif arg == 'nerd':
        await ctx.send('<:xNerd:1055636476769075262>')
    else:
        await ctx.send('» *unknown emoji*\n» make sure your command is all lowercase!\n» make sure theres no "x" in the name\n» example: `>send australiandance`\n» owow flags are not supported')

#
# OWOW COMMANDS
#
#currently unavailable!
@client.command(aliases=['owowmap', 'wowmap', 'worldofwarmap', 'officialworldofwarmap', 'oworldofwarmap', 'officialwowmap', 'owowm', 'wowm', 'm'])
async def map(ctx):
    ctx.send('» currently unavailable.')
@client.command(aliases=['officialworldofwar', 'oworldofwar', 'worldofwar', 'wow', 'officialwow'])
async def owow(ctx):
    ctx.send('» currently unavailable.')
@client.command(aliases=['officialworldofwarkürzel', 'oworldofwarkürzel', 'worldofwarkürzel', 'wowkürzel', 'officialwowkürzel', 'owowk', 'wowk'])
async def owowkürzel(ctx):
    ctx.send('» currently unavailable.')
# Karten
@client.command(pass_context=True, aliases=['karte', 'owowkarte', 'worldofwarkarte', 'officialworldofwarkarte', 'oworldofwarkarte'])
async def wowkarte(ctx):
    ctx.send('» currently unavailable.')

#
# MODDMS
#
@client.command(pass_context=True)
@commands.has_role(f'⚙️┇Staff')
@is_in_guild(909206946580672533)
async def moddm(ctx, user: discord.Member, *, message):
    channel = client.get_channel(1056785708183982120)
    await user.send(f'» [staff]> {message}')
    await channel.send(f'» {ctx.author.mention} → {user.mention}\n» `{message}`')
    await ctx.send('» sent!')
@client.command(pass_context=True)
@commands.has_role(f'⚙️┇Staff')
@is_in_guild(909206946580672533)
async def initmoddm(ctx, user: discord.Member, arg):
    channel = client.get_channel(1056785708183982120)
    if arg == 'en':
        await user.send('» **QYINT-COMMUNITY**\n » **initialised moddms [en]**\n» *use `>dm [response]` in the dms to respond.*\n» ')
    if arg == 'de':
        await user.send('» **QYINT-COMMUNITY**\n » **initialisierte moddms [de]**\n» *nutze `>dm [antwort]` in den dms um zu antworten.*\n» ')
    await channel.send(f'» {ctx.author.mention} → {user.mention}\n» initialised moddms [{arg}]')
@client.command(pass_context=True)
async def dm(ctx, *, message):
    if ctx.guild:
        return
    channel = client.get_channel(1056785708183982120)
    await channel.send(f'» → {ctx.author.mention} →\n» `{message}`')
    await ctx.send('» initialised moddms!')

#
# Weird Util ShitTM
#
@client.command() # sends all emojiids of a server
@commands.has_role(f'🧭┇Admin')
@is_in_guild(909206946580672533)
async def sendallemojis(ctx):
    for emoji in ctx.guild.emojis:
        await ctx.send(f"\{emoji}")
    await ctx.send('» sent all emojis!')

#END
client.run('[bot token]')
