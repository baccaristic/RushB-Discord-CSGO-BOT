from csgo.client import CSGOClient
from steam.client import SteamClient
import logging
from steam.enums import EResult
from csgo.enums import ECsgoGCMsg
import discord
from discord.ext import commands
import cloudscraper
import pycountry
import re
import requests
import json
import datetime
import valve.source
import valve.source.a2s
import valve.source.master_server
import valve.source.a2s
import os
import asyncio
import time
s = ""
def getcomp():
	sclient = SteamClient()
	cs = CSGOClient(sclient)
	@sclient.on('logged_on')
	def start_csgo():
		print("im logged on")
		cs.launch()
	@cs.on('ready')
	def gc_ready():
		print("im in csgo")
		cs.request_matchmaking_stats()
		s =cs.wait_event("matchmaking_stats",timeout = 3)
		cs.exit()
		sclient.logout()
		return str(s)
	sclient.login(username = "RushBot69",password = "toutoutn12")
	sclient.sleep(3)
	return gc_ready()
def getlevel(acc_id):
	data = ""
	sclient = SteamClient()
	cs = CSGOClient(sclient)
	@sclient.on('logged_on')
	def start_csgo():
		print("im logged on")
		cs.launch()
	@cs.on('ready')
	def gc_ready():
		print("im in csgo")
		cs.request_player_profile(acc_id)
		s = cs.wait_event('player_profile',timeout = 5)
		print(str(s))
		cs.exit()
		sclient.logout()
		return str(s)
	sclient.login(username = "RushBot69",password = "toutoutn12")
	sclient.sleep(3)
	return gc_ready()
def GetAccountID(id):
	return int(id) - 76561197960265728
def getID(link):
	data = {"input":link}
	s = requests.post("https://steamid.io/lookup",data = data).text
	ID = re.findall(r'<img class="cp" data-toggle="tooltip" data-placement="bottom" data-clipboard-text="(.+?)" src=',s)
	return ID[2]
def getName(link):
	data = {"input":link}
	s = requests.post("https://steamid.io/lookup",data = data).text
	return re.findall(r'<dd class="value">(.+?)</dd>',s)[1]
client = commands.Bot(command_prefix = '!rb ')
client.remove_command('help')
@client.event
async def on_guild_join(guild):
	print("just joined server with name", str(guild))
	headers = {"Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGkiOnRydWUsImlkIjoiMzEwNDcwMDgyNjc1MzQzMzYxIiwiaWF0IjoxNTk4NDc4MjcxfQ.6s73ILD59nepHTr9v__d-W-4Qau9CSETbOxyY4Zo3eM"}
	s = requests.post("https://discord.bots.gg/api/v1/bots/739094249055977473/stats",headers = headers , data = {"guildCount":len(client.guilds)}).text
@client.event
async def on_guild_remove(guild):
	print("just left server with name" , str(guild))
	headers = {"Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGkiOnRydWUsImlkIjoiMzEwNDcwMDgyNjc1MzQzMzYxIiwiaWF0IjoxNTk4NDc4MjcxfQ.6s73ILD59nepHTr9v__d-W-4Qau9CSETbOxyY4Zo3eM"}
	s = requests.post("https://discord.bots.gg/api/v1/bots/739094249055977473/stats",headers = headers , data = {"guildCount":len(client.guilds)}).text
def onfaceit(id):
	try:
		scraper = cloudscraper.create_scraper()
		s = scraper.get(f"https://faceitfinder.com/stats/{id}").text
		if "Players not found!" in s:
			return False
		else:
			return True
	except:
		scraper = cloudscraper.create_scraper()
		s = scraper.get(f"https://faceitfinder.com/stats/{id}").text
		if "Players not found!" in s:
			return False
		else:
			return True
@client.command(pass_context = True)
async def help(ctx):
	guilds = client.guilds
	s = 0
	for g in guilds:
		s = s+ len(g.members)
	print(f"server = {ctx.message.guild.name} | user = {ctx.message.author} | command = help")
	author = ctx.message.author
	embed = discord.Embed(title = "<:rushb:749050544798171219> RushB Bot is brought to you by Klepto Bots" , description = "I'm a **Counter Strike : Global Offensive bot** that **provides** quick and effortless **statistics/info** and other useful things.",color =0xffdd00 )
	embed.add_field(name = "Info" , value = "<:coding:739586798816067595>  **Developer:**SAL#5420\n<:web:750355219941949583>  **Website:**https://rb.gy/trx9vr\n<:discord:739880734315249816>  **Official Server:**https://discord.gg/mdEegrr\n<:Steam:739882491124383764>  **Steam:**/id/SAL9TN",inline = True)
	embed.add_field(name = "Stats",value = f"<:stat:739102514456035330>  **Servers:**`{len(guilds)}`\n<:public:740196972014731305>  **Users:**`{s}`",inline = True)
	embed.set_thumbnail(url = "https://upload-icon.s3.us-east-2.amazonaws.com/uploads/icons/png/17578817411582823579-512.png")
	#embed.set_footer(text = "70% of the data is gathered from steam API, since The API usage is limited. the rest of the info are scrapped from some CSGO stats sites such as the rank and the match history so the information you get are 60% valid because it all depends on the site's sync system")
	await ctx.send(author,embed = embed)
@client.event 
async def on_ready():
	s = len(client.guilds)
	print("bot is ready ,im running in {0} servers".format(s))
	await client.change_presence(status = discord.Status.idle , activity = discord.Game("!rb help"))
@client.command(pass_context = True)
async def profile(ctx,arg):
	levels = {'1': '<:r1:747091976704229467>', '2': '<:r2:747091979543773225>', '3': '<:r3:747091979162222623>', '4': '<:r4:747091979669733416>', '5': '<:r5:747091979627921428>', '6': '<:r6:747091980064129035>', '7': '<:r7:747091979833311280>', '8': '<:r8:747091980072386711>', '9': '<:r9:747091979401429093>', '10': '<:r10:747091980168724552>', '11': '<:r11:747091980562989148>', '12': '<:r12:747091980483559476>', '13': '<:r13:747091980466520065>', '14': '<:r14:747091981099859999>', '15': '<:r15:747092739983671298>', '16': '<:r16:747092740516347946>', '17': '<:r17:747092740961206383>', '18': '<:r18:747092741409865819>', '19': '<:r19:747092741464260629>', '20': '<:r20:747092741842010244>', '21': '<:r21:747092742135480320>', '22': '<:r22:747092742424756225>', '23': '<:r23:747092742412304406>', '24': '<:r24:747092742659768352>', '25': '<:r25:747092743305560244>', '26': '<:r26:747092743595229214>', '27': '<:r27:747092746724048926>', '28': '<:r28:747092747902648411>', '29': '<:r29:747092748087066625>', '30': '<:r30:747092748259164221>', '31': '<:r31:747092748229935126>', '32': '<:r32:747092747982471231>', '33': '<:r33:747092748016025672>', '34': '<:r34:747092749349552230>', '35': '<:r35:747092748590514306>', '36': '<:r36:747092748464553995>', '37': '<:r37:747092749102088202>', '38': '<:r38:747092749123059792>', '39': '<:r39:747092749152682055>', '40': '<:r40:747092749081378827>'}
	print(f"server = {ctx.message.guild.name} | user = {ctx.message.author} | command = profile")
	try:
		badgesz = {"Loyalty Badge":"<:lb:746510359346675743>","5 Year Veteran Coin":"<:5y:746510313192423565>","10 Year Veteran Coin":"<:10y:746510327734206464>","2017 Service Medal":"<:2017:746510359455596664>","2015 Service Medal":"<:2015:746509543604879462>","2016 Service Medal":"<:2016:746510358792896654>","2018 Service Medal":"<:2018:746510356267925668>","2019 Service Medal":"<:2019:746510358436511806>","2020 Service Medal":"<:2020:746531214843838512>"}
		ID = getID(arg)
		acc_id = GetAccountID(ID)
		s = getlevel(acc_id)
		if str(s) == None:
			exit()
		else:
			f = "".join(re.findall(r' cmd_friendly: (.+?)\n',str(s)))
			t = "".join(re.findall(r' cmd_teaching: (.+?)\n',str(s)))
			k = "".join(re.findall(r' cmd_leader: (.+?)\n',str(s)))
			level = "".join(re.findall(r'player_level: (.+?)\n',str(s)))
			XP = "".join(re.findall(r'player_cur_xp: (.+?)\n',str(s)))
			s = requests.get(f"https://steamcommunity.com/inventory/{ID}/730/2?l=english&count=5000").text
			if s =="null" or '"error":"EYldRefreshApp' in s:
				bch = "Cannot get badges , inventory is private"
				cch = ""
			else:
				if '"total_inventory_count":0' in s:
					bch = ""
					cch=""
				else:
					s = json.loads(requests.get(f"https://steamcommunity.com/inventory/{ID}/730/2?l=english&count=5000").text)['descriptions']
					coinss = {'Silver Operation Payback Coin': '<:Spay:746532021249114112>', 'Bronze Operation Payback Coin': '<:Bpay:746531998125785228>', 'Gold Operation Payback Coin': '<:Gpay:746532012021776445>', 'Silver Operation Bravo Coin': '<:Sbrav:746531998180573244>', "Operation Bravo Challenge Coin":"<:Sbrav:746531998180573244>", 'Bronze Operation Bravo Coin': '<:Bbrav:746532204930269264>', 'Gold Operation Bravo Coin': '<:Gbrav:746532257132445696>', 'Silver Operation Phoenix Coin': '<:Spho:746532253496115252>',"Operation Phoenix Challenge Coin":"<:Spho:746532253496115252>", 'Bronze Operation Phoenix Coin': '<:Bpho:746531983676538971>', 'Gold Operation Phoenix Coin': '<:Gpho:746532249297616957>', 'Silver Operation Breakout Coin': '<:Sbreak:746532020519436339>', 'Bronze Operation Breakout Coin': '<:Bbreak:746533275563982988>', 'Gold Operation Breakout Coin': '<:Gbreak:746532023962959953>', 'Silver Operation Vanguard Coin': '<:Svan:746531958422765658>', 'Bronze Operation Vanguard Coin': '<:Bvan:746532227705471076>',"Operation Vanguard Challenge Coin":"<:Gvan:746532923121074196>", 'Gold Operation Vanguard Coin': '<:Gvan:746532923121074196>', 'Silver Operation Bloodhound Coin': '<:Sbloo:746531974335955024>',"Operation Bloodhound Challenge Coin":"<:Sbloo:746531974335955024>", 'Bronze Operation Bloodhound Coin': '<:Bbloo:746533525301493820>', 'Gold Operation Bloodhound Coin': '<:Gbloo:746532150945251420>', 'Silver Operation Wildfire Coin': '<:Swil:746532216418598992>',"Operation Wildfire Challenge Coin":"<:Swil:746532216418598992>", 'Bronze Operation Wildfire Coin': '<:Bwil:746535116699861002>', 'Gold Operation Wildfire Coin': '<:Gwil:746532217127436378>','Operation Hydra Challenge Coin':'<:Sbhy:746534733852180510>', 'Silver Operation Hydra Coin': '<:Sbhy:746534733852180510>', 'Bronze Operation Hydra Coin': '<:Bhy:746534724297556008>', 'Gold Operation Hydra Coin': '<:Gbhy:746532226665021492>', 'Silver Operation Shattered Web Coin': '<:Ssh:746532144720904250>', 'Bronze Operation Shattered Web Coin': '<:Bsh:746532163314384938>', "Operation Shattered Web Challenge Coin":"<:Gsh:746531932321480745>",'Gold Operation Shattered Web Coin': '<:Gsh:746531932321480745>' , "Diamond Operation Shattered Web Coin":'<:Gsh:746531932321480745>'}
					coins = [d['name'] for d in s if "Operation" in d['name'] and "Coin" in d['name']]
					badges = [d['name'] for d in s if "Service Medal" in d['name'] or "Loyalty Badge" in d['name'] or "Year Veteran Coin" in d['name']]
					bch = ""
					for b in badges:
						bch = bch+badgesz[b]
					cch = ""
					for c in coins:
						cch = cch+coinss[c]
			maps = {"de_anubis":"<:de_anubis:751093329030021181>","de_chlorine":"<:chlorine:740236290036858931>","de_mirage_scrimmagemap":"<:mirage:739112185736986706>","de_mirage":"<:mirage:739112185736986706>","de_inferno":"<:inferno:739112165587550240>","de_dust2":"<:dust2:739112146851332149>","de_overpass":"<:overpass:739114863682388068>","de_cache":"<:cache:739112127654264923>","de_vertigo":"<:vertigo:740235949388333076>","de_nuke":"<:nuke:739112203059200020>","de_train":"<:traincs:739114315537317970>","cs_office":"<:officec:740911599635660902>"}
			deagle = {"kills":0,"shots":1,"hits":0}
			usp = {"kills":0,"shots":1,"hits":0}
			glock = {"kills":0,"shots":1,"hits":0}
			ak = {"kills":0,"shots":1,"hits":0}
			m4 = {"kills":0,"shots":1,"hits":0}
			awp = {"kills":0,"shots":1,"hits":0}
			scout = {"kills":0,"shots":1,"hits":0}
			is_faceit = onfaceit(ID)
			ranks = {"0":"Unranked / Uknown | zeaze ","1":"**Silver I** | <:SilverI:737685627801305128>" ,"2":"**Silver II** | <:SilverII:737685871570190406>","3":"**Silver III** | <:SilverIII:737686036108279818>","4":"**Silver IV** | <:SilverIV:737686254291779616>","5":"**Silver Elite** | <:SilverE:737686691808018492>","6":"**Silver Elite Master** | <:SilverEM:737686889267593236>","7":"**Gold Nova I** | <:GI:737687440453533807>","8":"**Gold Nova II** | <:GII:737692726988111902>","9":"**Gold Nova III** | <:GIII:737692911667511377>","10":"**Gold Nova Master** | <:GM:737693099966595112>","11":"**Master Guardian I** | <:MGI:737693657565626439>","12":"**Master Guardian II** | <:MGII:737693954601910293>","13":"**Master Guardian Elite** | <:MGE:737697559472111717>","14":"**Distinguished Master Guardian** | <:DMG:737698555103412345>","15":"**Lengendary Eagle** | <:LE:737698580432945163>","16":"**Lengendary Eagle Master** | <:LEM:737699375610069093>","17":"**Supreme Master First Class** | <:SMG:737701306843660340>","18":"**The Global Elite** | <:GE:737701327496544267>"}
			apisrc = json.loads(requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=2A51A32E929289CA0C9A621CB3DE99DA&steamid={ID}").text)['playerstats']['stats']
			scraper = cloudscraper.create_scraper()
			source = scraper.get(f"https://csgostats.gg/player/{ID}")
			name = re.findall(r'<meta name="twitter:title" content="Player statistics - (.+?)">',source.text)[0]
			kp = "Unknown"
			for c in apisrc:
				if c['name'] == 'total_kills':
					ttkills = c['value']
				elif c['name'] == 'total_deaths':
					ttdeaths = c['value']
				elif c['name'] == 'total_rounds_played':
					ttrounds = c['value']
				elif c['name'] =='total_damage_done':
					ttdamge = c['value']
				elif c['name'] == 'total_kills_headshot':
					tths = c['value']
				elif c['name'] == 'total_matches_won':
					ttmw = c['value']
				elif c['name'] == 'total_matches_played':
					ttmp = c['value']
				elif c['name'] == 'total_kills_enemy_blinded':
					blinded = c['value']
				elif c['name'] == 'total_mvps':
					mvp = c['value']
				elif c['name'] == 'total_shots_hit':
					tth = c['value']
				elif c['name'] =='total_shots_fired':
					ttf = c['value']
				elif c['name'] == 'total_kills_knife':
					kp = c['value']
				elif c['name'] == 'total_time_played':
					tttp = c['value']
				elif c['name'] == 'total_kills_glock':
					glock['kills'] = c['value']
				elif c['name'] == 'total_kills_hkp2000':
					usp['kills'] = c['value']
				elif c['name'] == 'total_kills_deagle':
					deagle['kills'] = c['value']
				elif c['name'] == 'total_kills_ak47':
					ak['kills'] = c['value']
				elif c['name'] == 'total_kills_m4a1':
					m4['kills'] = c['value']
				elif c['name'] == 'total_kills_awp':
					awp['kills'] = c['value']
				elif c['name'] == 'total_kills_ssg08':
					scout['kills'] = c['value']
				elif c['name'] == 'total_hits_deagle':
					deagle['hits'] = c['value']
				elif c['name'] == 'total_hits_awp':
					awp['hits'] = c['value']
				elif c['name'] == 'total_hits_glock':
					glock['hits'] = c['value']
				elif c['name'] == 'total_hits_ssg08':
					scout['hits'] = c['value']
				elif c['name'] == 'total_hits_hkp2000':
					usp['hits'] = c['value']
				elif c['name'] == 'total_hits_ak47':
					ak['hits'] =c['value']
				elif c['name'] == 'total_hits_m4a1':
					m4['hits'] = c['value']
				elif c['name'] == 'total_shots_deagle':
					deagle['shots'] = c['value']
				elif c['name'] == 'total_shots_awp':
					awp['shots'] = c['value']
				elif c['name'] == 'total_shots_glock':
					glock['shots'] = c['value']
				elif c['name'] == 'total_shots_ssg08':
					scout['shots'] = c['value']
				elif c['name'] == 'total_shots_hkp2000':
					usp['shots'] = c['value']
				elif c['name'] == 'total_shots_ak47':
					ak['shots'] = c['value']
				elif c['name'] == 'total_shots_m4a1':
					m4['shots'] = c['value']
			kd = round(ttkills / ttdeaths,2)
			adr = round(ttdamge/ttrounds,2)
			hs = round(tths/ttkills,2)*100
			wr = ttmw/ttmp*100
			timeplayed = datetime.timedelta(seconds = tttp)
			accuracy = round((tth / ttf)*100,2)
			#name = re.findall(r'  <meta name="twitter:title" content="Player statistics - (.+?) | ')
			if kd >= 1:
				emote = "<:up1:739145976325079103>"
			elif kd <1 and kd >=0.5:
				emote = "<:hyphen:739148726584606750>"
			else:
				emote = "<:down:739147421589700722>"
			compwins = re.findall(r'<span style="display:block; font-size:38px; color:#fff; font-family:\'Roboto Condensed\'; font-weight:bold;">(.+?)</span>',source.text)
			rankinfo = re.findall(r'"https://static.csgostats.gg/images/ranks/(.+?).png',source.text)
			rank = ''
			if len(rankinfo) == 0:
				rank = '0'
				p = rank
			else:
				rank = rankinfo[0]
				p = rank
			rank = ranks[rank]
			print(rank)
			embed1 = discord.Embed(title = "RushB profile Command",description = f"<:stat:739102514456035330> |Player statistics- __**{name}**__\nLevel: ***{level}*** {levels[level]} XP = ***{int(XP) - 327680000}***\n{f }<:friend:747085450325393428> {t} <:teach:747085449306046536> {k} <:king:747085450140844172>\n{bch}{cch}" , color=0xa29507)
			img = re.findall(r'<img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/(.+?)" width="120"',source.text)
			print(img)
			print(compwins)
			embed1.set_thumbnail(url=f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/{img[0]}")
			print("done")
			embed1.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
			print("done")
			embed1.add_field(name="<:KDA:739127711578062881> K/D", value=f" {kd} {emote}", inline=True)
			print("done")
			embed1.add_field(name="<:ADR:739110273800994896> ADR", value=f"{adr}", inline=True)
			print("done")
			embed1.add_field(name="<:hs:739101097108439100> HS%", value=f"{hs}%", inline=True)
			print("done")
			cwins = "".join(compwins)
			embed1.add_field(name="<:comp:739282904391090336> Comp Wins",value = f"{cwins} wins",inline = True)
			print("done")
			embed1.add_field(name="<:wr:739101731287334982> Winrate%", value=f"%.2f" % wr +"%", inline=True)
			print("done")
			embed1.add_field(name="  <:knife:739101211575451658> Knife Kills", value=f"{kp}", inline=True)
			print("done")
			embed1.add_field(name="  <:blind:739150286643265549> Blind Kills", value= blinded, inline=True)
			print("done")
			embed1.add_field(name="  <:faceit:739876531941277787> On Faceit", value= is_faceit, inline=True)
			print("done")
			embed1.set_footer(text = "Page 1/3 | Page : Player Stats Info")
			embed1.add_field(name="<:mvp:739153289542631435> MVPs",value = mvp ,  inline = True)
			print("done")
			embed1.add_field(name="<:accuracy:739289181393649798> Accuracy%",value = f"{accuracy}%" ,  inline = True)
			print("done")
			embed1.add_field(name="<:time:739158183532298270> Time Played",value=str(timeplayed),inline = True)
			print("done")
			embed1.add_field(name="<:rank:739292579157246013>  Rank", value= rank.split("|")[0], inline=True)
			print("done")
			embed1.set_image(url = f"https://static.csgostats.gg/images/ranks/{p}.png")
			embed2 = discord.Embed(title = "RushB profile Command",description = f"<:weapon:739263351183507457> | Weapons statistics For player __**{name}**__" , color=0xa29507)
			embed2.set_thumbnail(url=f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/{img[0]}")
			embed2.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
			embed2.add_field(name = "Glock <:glock:739101072068575265>",value = f"Total Kills <:kill:739291475094798446> = {glock['kills']} | accuracy <:accuracy:739289181393649798> = {round(glock['hits'] /glock['shots']*100) }%",inline = False)
			print("done")
			embed2.add_field(name = "Deagle <:deagle:739100831688818720>",value = f"Total Kills <:kill:739291475094798446> = {deagle['kills']} |  accuracy <:accuracy:739289181393649798> =  {round(deagle['hits'] /deagle['shots']*100) }%",inline = False)
			print("done")
			embed2.add_field(name = "USP <:usp:739101516375392296>",value = f"Total Kills <:kill:739291475094798446> = {usp['kills']} | accuracy <:accuracy:739289181393649798> = {round(usp['hits'] /usp['shots']*100) }%",inline = False)
			print("done")
			embed2.add_field(name = "Ak47 <:ak:739100662117433354>",value = f"Total Kills <:kill:739291475094798446> = {ak['kills']} | accuracy <:accuracy:739289181393649798> = {round(ak['hits'] /ak['shots']*100) }%",inline = False)
			print("done")
			embed2.add_field(name = "M4A1 <:m4a1:739101250511175760>",value = f"Total Kills <:kill:739291475094798446> = {m4['kills']} | accuracy <:accuracy:739289181393649798> = {round(m4['hits'] /m4['shots']*100) }%",inline = False)
			print("done")
			embed2.add_field(name = "AWP <:awp:739100741179801652>",value = f"Total Kills <:kill:739291475094798446> = {awp['kills']} | accuracy <:accuracy:739289181393649798> = {round(awp['hits'] /awp['shots']*100) }%",inline = False)
			print("done")
			embed2.add_field(name = "Scout <:scout:739101617294671903>",value = f"Total Kills <:kill:739291475094798446> = {scout['kills']} | accuracy <:accuracy:739289181393649798> = {round(scout['hits'] /scout['shots']*100) }%",inline = False)
			print("done")
			embed2.set_image(url = "https://cdn.discordapp.com/attachments/738388030309793837/739244757590474812/csgo-image.png")
			embed2.set_footer(text = "Page 2/3 | Page : Player's Weapons Stats")
			dates = re.findall(r'<td style="text-align:left; white-space:nowrap; position:relative;">\n                        (.+?)\n                    </td>',source.text)[0:11]
			data = re.findall(r'var stats = (.+?);',source.text)
			embed3 = discord.Embed(title = "RushB profile Command",description = f"<:history:739264155105755166> | Last {len(dates)} Games Stats player __**{name}**__" , color=0xa29507)
			if data[0] == 'false':
				embed3.add_field(name = "Info" , value = "No matches recorded for this player")
			else:
				data = json.loads(data[0])['past10']
				dates = dates[0:len(data)]
				j = len(dates) -1
				i = 1
				embed3 = discord.Embed(title = "RushB profile Command",description = f"<:history:739264155105755166> | Last {len(dates)} Games Stats player __**{name}**__" , color=0xa29507)
				for d in data:
					score = d['score']
					if (int(score.split(':')[0]) < int(score.split(':')[1])):
						e = "<:lost:739266511876915231>"
					elif (int(score.split(':')[0]) > int(score.split(':')[1])):
						e = "<:win:739265813156069538>"
					else:
						e = "<:tie:739266969693585416>"
					if not( d['map'] in maps):
						mamp = "<:DFM:751095092185530499>"
					else:
						mamp = maps[d['map']]
					embed3.add_field(name =f"Game {i} Played : {dates[j]}" , value =f"{mamp} **{d['map']}** | **{score}** {e} | Adr <:ADR:739110273800994896> : **{d['adr']}** | Headshots <:hs:739101097108439100> % : **{d['hs']}**% | KD <:kda:739127711578062881> : **{d['kd']}** | Rating : **{d['rating']}**",inline =False)
					i = i+1
					j = j -1
			embed3.set_footer(text = "Page 3/3 | Page : Player's History Stats")
			embed3.set_thumbnail(url=f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/{img[0]}")
			embed3.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
			embed3.set_image(url ="https://cdn.discordapp.com/attachments/691417976951537697/739296291393241128/csgo.png")
			message = await ctx.send(embed = embed1)
			await message.add_reaction('1️⃣')
			await message.add_reaction('2️⃣')
			await message.add_reaction('3️⃣')
			emoji = ""
			while True:
			    if emoji=='1️⃣':
			        await message.edit(embed=embed1)
			    if emoji=='2️⃣':
			    	await message.edit(embed=embed2)
			    if emoji =='3️⃣':
			    	await message.edit(embed=embed3)
			    reaction , user=await client.wait_for('reaction_add')
			    if str(user)!='RushB#8124' and str(user) == str(ctx.message.author): #Example: 'MyBot#1111'
			        emoji=str(reaction.emoji)
			        await message.remove_reaction(reaction,user)
			    print(emoji)
			await client.clear_reactions(message)
	except Exception as e:
		print(e)
		await ctx.send("```diff\nRequest ERROR TRY AGAIN And make sure that ur steam Profile Is Public !```")

		#await ctx.send("```diff\nRequest ERROR TRY AGAIN And make sure that ur steam Profile Is Public !```")
@client.command()
async def live(ctx,arg):
	ran = {"0":"<:unrank:746523188632092795>","1":"<:S1:737685627801305128>","2":"<:S2:737685871570190406>","3":"<:S3:737686036108279818>","4":"<:S4:737686254291779616>","5":"<:SE:737686691808018492>","6":"<:SEM:737686889267593236>","7":"<:GI:737687440453533807>","8":"<:GII:737692726988111902>","9":"<:GIII:737692911667511377>","10":"<:GM:737693099966595112>","11":"<:MGI:737693657565626439>","12":"<:MGII:737693954601910293>","13":"<:MGE:737697559472111717>","14":"<:DMG:737698555103412345>","15":"<:LE:737698580432945163>","16":"<:LEM:737699375610069093>","17":"<:SMG:737701306843660340>","18":"<:GE:737701327496544267>"}
	print(f"server = {ctx.message.guild.name} | user = {ctx.message.author} | command = live")
	maps = {"de_dust2_v2":"<:dust2:739112146851332149>","de_mirage_scrimmagemap":"<:mirage:739112185736986706>","de_mirage":"<:mirage:739112185736986706>","de_inferno":"<:inferno:739112165587550240>","de_dust2":"<:dust2:739112146851332149>","de_overpass":"<:overpass:739114863682388068>","de_cache":"<:cache:739112127654264923>","de_vertigo":"","de_nuke":"<:nuke:739112203059200020>","de_train":"<:train~1:739114315537317970>"}
	try:
		ID = getID(arg)
		scraper = cloudscraper.create_scraper()
		src = json.loads(scraper.get(f"https://csgostats.gg/player/{ID}/live").text)
		currentMap = re.findall(r'https://static.csgostats.gg/images/maps/screenshots/(.+?).jpg',src['map'].replace("\\",""))[0]
		Avatars= re.findall(r'<img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/(.+?)"',src['content'].replace("\\",""))
		names = re.findall(r'<span style="display:inline-block; vertical-align:middle; max-width:160px; text-overflow:ellipsis; overflow:hidden; margin-left:6px; padding-right:16px;">(.+?)<',src['content'].replace("\\",""))
		ranks = re.findall(r'<td><img src="https://static.csgostats.gg/images/ranks/(.+?).png"',src['content'].replace("\\",""))
		info  = re.findall(r'<td align="center">(.+?)</td>',src['content'].replace("\\",""))
		mpi = re.findall(r'https://static.csgostats.gg/images/maps/icons/(.+?).png',src['content'].replace("\\",""))[0]
		date = re.findall(r'<div style="font-weight:500;">(.+?)</div>',src['content'].replace("\\",""))[1]
		ids = re.findall(r'href="/player/(.+?)"',src['content'].replace("\\",""))
		i = 1
		allplayers = []
		player = []
		for c in info:
			if i==4:
				player.append(c)
				allplayers.append(player)
				player = []
				i = 1
			else:
				player.append(c)
				i = i+1
		s1 = re.findall(r'<div class="team-score-inner">\n                                    (.+?)\n                                </div>',src['content'].replace("\\",""))
		score = re.findall(r'<span style="letter-spacing:-0.05em;">(.+?)</span>',s1[0])[0] + ":" + s1[1]
		embedpages = []
		team1 = allplayers[0:5]
		team2 = allplayers[5:10]
		print(team1)
		print(team2)
		j = 1
		i = 0
		k = 0
		l = team1
		for id in ids:
			try:
				if i <5:
					j = 1
					colour = 0xff0000
				else:
					j = 2
					colour = 0x0040ff
				s = scraper.get(f"https://csgostats.gg/player/{id}")
				rank = re.findall(r'<img src="https://static.csgostats.gg/images/ranks/(.+?)" width="92" />',s.text)
				if len(rank )==0:
					rank = '0'
				else:
					rank = rank[0].split('.')[0]
				ispublic = "500 Internal Server Error" in requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=2A51A32E929289CA0C9A621CB3DE99DA&steamid={id}").text
				name = re.findall(r'<meta name="twitter:title" content="Player statistics - (.+?) | CS:GO Stats ">',s.text)
				embed = discord.Embed(title = "RushB Live Command" , description = f"<:stat:739102514456035330> **{name[0]}** Stats in game" ,color = colour)
				embed.set_thumbnail(url=f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/{Avatars[i]}")
				embed.set_image(url = f"https://static.csgostats.gg/images/ranks/{rank}.png")
				embed.add_field(name = "Kills <:kill:739291475094798446> " , value = allplayers[i][0],inline = True)
				embed.add_field(name = "Deaths <:dead:739861042447777842>" , value = allplayers[i][1],inline = True)
				embed.add_field(name = "Assists <:assist:739522793846210641> " , value = allplayers[i][2],inline = True)
				embed.add_field(name = "MVPs <:mvp:739153289542631435> " , value = allplayers[i][3],inline = True)
				embed.add_field(name= "SteamID <:Steam:739882491124383764>" , value =  f"http://steamcommunity.com/profiles/{id}" , inline = True)
				embed.add_field(name = "Is Public <:public:740196972014731305>" , value = not ispublic,inline = True)
				if i <5:
					team1[k].append(rank)
					team1[k].append(name[0])
				else:
					team2[k-5].append(rank)
					team2[k-5].append(name[0])
				embed.add_field(name="  <:faceit:739876531941277787> On Faceit", value= onfaceit(id), inline=True)
				embed.set_footer(text = f"Page {i+1}/10 | {name[0]} Stats in Game | Team {j}")
				embed.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
				embedpages.append(embed)
				i = i+1
				k = k+1
			except:
				if i <5:
					j = 1
					colour = 0xff0000
				else:
					j = 2
					colour = 0x0040ff
				s = scraper.get(f"https://csgostats.gg/player/{id}")
				rank = re.findall(r'<img src="https://static.csgostats.gg/images/ranks/(.+?)" width="92" />',s.text)
				if len(rank )==0:
					rank = '0'
				else:
					rank = rank[0].split('.')[0]
				ispublic = "500 Internal Server Error" in requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=2A51A32E929289CA0C9A621CB3DE99DA&steamid={id}").text
				name = re.findall(r'<meta name="twitter:title" content="Player statistics - (.+?) | CS:GO Stats ">',s.text)
				embed = discord.Embed(title = "RushB Live Command" , description = f"<:stat:739102514456035330> **{name[0]}** Stats in game" ,color = colour)
				embed.set_thumbnail(url=f"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/{Avatars[i]}")
				embed.set_image(url = f"https://static.csgostats.gg/images/ranks/{rank}.png")
				embed.add_field(name = "Kills <:kill:739291475094798446> " , value = allplayers[i][0],inline = True)
				embed.add_field(name = "Deaths" , value = allplayers[i][1],inline = True)
				embed.add_field(name = "Assists <:assist:739522793846210641> " , value = allplayers[i][2],inline = True)
				embed.add_field(name = "MVPs <:mvp:739153289542631435> " , value = allplayers[i][3],inline = True)
				embed.add_field(name= "SteamID <:Steam:739882491124383764>" , value = f"http://steamcommunity.com/profiles/{id}" , inline = True)
				embed.add_field(name = "Is Public <:public:740196972014731305>" , value = not ispublic,inline = True)
				if i <5:
					team1[k].append(rank)
					team1[k].append(name[0])
				else:
					team2[k -5].append(rank)
					team2[k -5].append(name[0])
				embed.set_footer(text = f"Page {i+1}/10 | {names[i]} Stats in Game | Team {j}")
				embed.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
				embedpages.append(embed)
				i = i+1
				k = k+1
		print(team1)
		print(team2)
		t1 = []
		t2 = []
		pages = {1:":one:",2:":two:",3:":three:",4:":four:",5:":five:",6:":six:",7:":seven:",8:":eight:",9:":nine:",10:":keycap_ten:"}
		i = 1
		for c in team1:
			r = ran[c[4]]
			ch = f"**➤{c[5]}** |{r} {pages[i]}"
			t1.append(ch)
			i = i+1
		for c in team2:
			r = ran[c[4]]
			ch = f"**➤{c[5]}** |{r} {pages[i]}"
			t2.append(ch)
			i = i+1
		t1 = "\n".join(t1)
		t2 = "\n".join(t2)
		mainembed = discord.Embed(title = "RushB Live Command" , description = f"<:live:739526527670157383> **{currentMap}** Competitive Live Game")
		mainembed.set_thumbnail(url = f"https://static.csgostats.gg/images/maps/icons/{mpi}.png")
		mainembed.set_image(url = f"https://static.csgostats.gg/images/maps/screenshots/{currentMap}.jpg")
		mainembed.add_field(name = "Live Game Score <:Score:739524791932813403>" , value = f"**{score}**")
		mainembed.add_field(name = "‏‏‎ ‎" , value = "‏‏‎ ‎")
		mainembed.add_field(name = "Time <:time:739528767701123180>" , value = f"**{date}**")
		mainembed.add_field(name = ":red_circle: Team1" , value = t1 , inline = True)
		mainembed.add_field(name = ":blue_circle: Team2" , value = t2, inline = True)
		mainembed.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
		mainembed.set_footer(text = f"Page 0/10 | Game Score , Time & Map")
		message = await ctx.send(embed = mainembed)
		await message.add_reaction('0️⃣')
		await message.add_reaction('1️⃣')
		await message.add_reaction('2️⃣')
		await message.add_reaction('3️⃣')
		await message.add_reaction('4️⃣')
		await message.add_reaction('5️⃣')
		await message.add_reaction('6️⃣')
		await message.add_reaction('7️⃣')
		await message.add_reaction('8️⃣')
		await message.add_reaction('9️⃣')
		await message.add_reaction('🔟')
		emoji = ""
		while True:
		    if emoji=='1️⃣':
		        await message.edit(embed=embedpages[0])
		    if emoji=='2️⃣':
		    	await message.edit(embed=embedpages[1])
		    if emoji =='3️⃣':
		    	await message.edit(embed=embedpages[2])
		    if emoji=='0️⃣':
		        await message.edit(embed=mainembed)
		    if emoji=='4️⃣':
		    	await message.edit(embed=embedpages[3])
		    if emoji =='5️⃣':
		    	await message.edit(embed=embedpages[4])
		    if emoji=='6️⃣':
		        await message.edit(embed=embedpages[5])
		    if emoji=='7️⃣':
		    	await message.edit(embed=embedpages[6])
		    if emoji =='8️⃣':
		    	await message.edit(embed=embedpages[7])
		    if emoji=='9️⃣':
		    	await message.edit(embed=embedpages[8])
		    if emoji =='🔟':
		    	await message.edit(embed=embedpages[9])
		    reaction , user=await client.wait_for('reaction_add')
		    print(reaction)
		    print(user)
		    if str(user)!='RushB#8124' and str(user) == str(ctx.message.author): #Example: 'MyBot#1111'
		        emoji=str(reaction.emoji)
		        await message.remove_reaction(reaction,user)
		    print(emoji)
		await client.clear_reactions(message)
	except Exception as e:
		print(e)
		await ctx.send("```diff\nError in command or this player is current not in a live match!\n```")
@client.command(pas_context = True)
async def faceit(ctx,arg):
	print(f"server = {ctx.message.guild.name} | user = {ctx.message.author} | command = faceit")
	ID = getID(arg)
	sub = {"Free membership":"<:Free:739872093448962218>","Premium membership":"<:faceitprem:739871450042728548>"}
	types = {"positive":"<:up1:739145976325079103>","negative":"<:down:739147421589700722>"}
	rankimg = {"1":"https://cdn.discordapp.com/attachments/739777799476478042/739844250103054457/skill_level_1_lg.png","2":"https://cdn.discordapp.com/attachments/739777799476478042/739844300845875250/skill_level_2_lg.png","3":"https://cdn.discordapp.com/attachments/739777799476478042/739844345397641327/skill_level_3_lg.png","4":"https://cdn.discordapp.com/attachments/739777799476478042/739844393128689664/skill_level_4_lg.png","5":"https://cdn.discordapp.com/attachments/739777799476478042/739844472451498044/skill_level_5_lg.png","6":"https://cdn.discordapp.com/attachments/739777799476478042/739844512154648696/skill_level_6_lg.png","7":"https://cdn.discordapp.com/attachments/739777799476478042/739844554676633621/skill_level_7_lg.png","8":"https://cdn.discordapp.com/attachments/739777799476478042/739844590445658202/skill_level_8_lg.png","9":"https://cdn.discordapp.com/attachments/739777799476478042/739844624604069978/skill_level_9_lg.png","10":"https://cdn.discordapp.com/attachments/739777799476478042/739844661341978644/skill_level_10_lg.png"}
	scraper = cloudscraper.create_scraper()
	s = scraper.get(f"https://faceitfinder.com/stats/{ID}").text
	if ">Stats unavailable<" in s:
		await ctx.send("Player didn't play on faceit")
	elif "Players not found!" in s:
		await ctx.send("Players is not on Faceit")
	else:
		scraper = cloudscraper.create_scraper()
		s = scraper.get(f"https://faceitfinder.com/stats/{ID}").text
		maininfo = re.findall(r'<span class="stats_totals_block_main_value_span (.+?)</span>',s)
		subInfo = re.findall(r'<span class="stats_totals_block_item_value">(.+?)<',s)
		other = re.findall(r'<span class="stats_totals_block_main_value_span">(.+?)<',s)
		kd = maininfo[0]
		winrate = maininfo[1]
		hltv = maininfo[2]
		elo = other[0]
		headshots = other[1]
		matches = other[2]
		kdinfo = subInfo[0:3]
		winrateinfo = subInfo[3:6]
		hltvinfo = subInfo[6:9]
		name = re.findall(r'<title>(.+?) detailed stats -',s)[0]
		eloinfo = subInfo[9:12]
		hsinfo = subInfo[12:15]
		matinfo = subInfo[15:18]
		mbs = re.findall(r'<span class="stats_profile_middle_span">(.+?)<',s)[0]
		embed = discord.Embed(title = "RushB Faceit Command" , description = f"<:stat:739102514456035330>Faceit Stats | Player  __**{name}**__ __*{mbs}*__ {sub[mbs]}" , color = discord.Color.orange())
		ranklink = re.findall(r'skill_level_(.+?)_lg.png',eloinfo[0].split('src="')[1].split('" alt=')[0])[0]
		avatar = re.findall(r'<img class="stats_profile_avatar" src="(.+?)"',s)[0]
		kdvalue = kd.split('">')[1]
		kdtype = kd.split('">')[0]
		wrvalue= winrate.split('">')[1]
		wrtype= winrate.split('">')[0]
		hltvvalue = hltv.split('">')[1]
		hltvtype = hltv.split('">')[0]
		embed.add_field(name = f"K/D <:kda:739127711578062881>: {kdvalue} {types[kdtype]}" , value = f"Avg kills <:kill:739291475094798446>=__*{kdinfo[0]}*__\nAvg deaths <:dead:739861042447777842>=__*{kdinfo[1]}*__\nReal K/D =__*{kdinfo[2]}*__" , inline = True)
		embed.add_field(name = f"Winrate <:wr:739101731287334982>:{wrvalue}{types[wrtype]}" , value = f"Matches <:Matches:739863613124247602>=__*{winrateinfo[0]}*__\nWon <:win:739265813156069538>= __*{winrateinfo[1]}*__\nLost <:lost:739266511876915231>= __*{winrateinfo[2]}*__" , inline = True)
		embed.add_field(name = f"HLTV <:hltv:739854453129347162>:{hltvvalue} {types[hltvtype]}" , value = f"Triple Kills <:triple:739856818939101296>=__*{hltvinfo[0]}*__\nQuad kills <:quadt:739858472899969054>= __*{hltvinfo[1]}*__\nAces <:Ace:739860438564470916>= __*{hltvinfo[2]}*__" ,inline = True)
		embed.add_field(name = f"ELO <:rank:739292579157246013>: {elo}" , value = f"Lowest 👎= __*{eloinfo[1]}*__\nHighest 👍= __*{eloinfo[2]}*__" ,inline = True)
		embed.add_field(name = f"Headshots <:hs:739101097108439100>:{headshots}",value = f"Kills <:kill:739291475094798446>= __*{hsinfo[0]}*__\nHeadshots <:hs:739101097108439100>= __*{hsinfo[1]}*__\nReal HS % = __*{hsinfo[2]}*__",inline = True)
		embed.add_field(name = f"Matches <:Matches:739863613124247602>={matches}",value = f"Kills <:kill:739291475094798446>=__*{matinfo[0]}*__\nDeaths <:dead:739861042447777842>=__*{matinfo[1]}*__\nAssists <:assist:739522793846210641>=__*{matinfo[2]}*__")
		embed.set_author(name = "Faceit CS:GO",icon_url = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/e7/e74d4f1f7730b917c5a33c492a1112973862bb47_full.jpg")
		if "faceit_avatar.jpg" in avatar:
			avatar = "https://cdn.discordapp.com/attachments/739777799476478042/739846650108837988/faceit_avatar.png"
		embed.set_thumbnail(url =avatar)
		embed.set_image(url=rankimg[ranklink])
		await ctx.send(embed= embed)
@client.command(pass_context = True)
async def inventory(ctx,arg):
	message = await ctx.send("Getting Data...")
	ID = getID(arg)
	try:
		s = requests.get(f"https://steamcommunity.com/inventory/{ID}/730/2?l=english&count=5000").text
		if s == "null":
			await ctx.send("Sorry But this profile's inventory is not public !")
		else:
			data = json.loads(s)['descriptions']
			total_skins = 0
			embedpages = []
			name = getName(arg)
			main  = discord.Embed(title = "RushB inventory command", description = f"<:inventory:743437848488968202>|Player's inventory stats - **{name}**",color = 0xffdd00)
			avatar = json.loads(requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2A51A32E929289CA0C9A621CB3DE99DA&steamids={ID}").text)['response']['players'][0]['avatarfull']
			main.set_thumbnail(url = avatar)
			main.set_image(url = "https://totalcsgo.com/blog/jpg/csbet-skins-2.jpg")
			high = 0
			low = 0
			j = 0
			for d in data:
				if "Gloves" in d['name'] or d['name'].split(' | ')[0].replace(" ","") in ["Soldier","GroundRebel","Enforcer","Operator","BSquadronOfficer","3rdCommandoCompany","Osiris","MarkusDelrow","Maximus","Dragomir","Buckshot","Prof.Shahmat","MichaelSyfers","'TwoTimes'McCoy","RezanTheReady","Blackwolf","TheEliteMr.Muhlik","Lt.CommanderRicksaw","'TheDoctor'Romanov","SpecialAgentAva"]or "Slingshot" in d['name'] or"Operator" in d['name'] or"Case" in d['name'] or "Graffiti" in d['name'] or "Medal" in d['name'] or "Sticker" in d['name'] or "Coin" in d['name'] or "Music Kit" in d['name'] or "Badge" in d['name']:
					pass
				else:
					print(d['name'])
					if (len(d['name'].split(' | ')) == 1):
						pass
					else:
						j+=1
						total_skins +=1
						await message.edit(content = f"Toltal Skins count : {j}")
						n1 = d['name'].split(' | ')[0]
						n2 = d['name'].split(' | ')[1]
						ln1 = n1.replace(" ","+")
						ln1 = "".join([c for c in ln1 if c.isalnum() or c == '-' or c ==' ' or c == '+'])
						print(ln1)
						if ln1[0] == '+':
							ln1 = ln1[1:len(ln1)]
						ln1 = ln1.replace("StatTrak+","").replace("Souvenir+","")
						ndn1 = n1.replace(" ",'-')
						ndn1 = "".join([c for c in ndn1 if c.isalnum() or c == '-' or c ==' '])
						if (ndn1[0] == '-' or ndn1[0] == '+'):
							ndn1 = ndn1[1:len(ndn1)]
						print(ndn1)
						ndn1 = ndn1.replace("StatTrak-","").replace("Souvenir-","")
						ndn2 = n2.replace(" ","-").replace(".","").replace("'","")
						print(ndn2)
						img = f"https://community.cloudflare.steamstatic.com/economy/image/{d['icon_url_large']}"
						s = requests.get(f"https://csgostash.com/weapon/{ln1}").text
						links = re.findall(rf'<a href="https://csgostash.com/skin/(.+?)/{ndn1}-{ndn2}',s)
						skinid = links[0]
						print(f"https://csgostash.com/skin/{skinid}/{ndn1}-{ndn2}")
						linkd = f"https://csgostash.com/skin/{skinid}/{ndn1}-{ndn2}"
						pricesource = requests.get(f"https://csgostash.com/skin/{skinid}/{ndn1}-{ndn2}").text
						prices = re.findall(rf'<p class="nomargin"><a href="{linkd}">(.+?)</a></p>',s)
						print(prices)
						minprice = prices[0].split(' - ')[0]
						print("done")
						if len(prices[0].split(' - ') )== 1:
							maxprice = minprice
						else:
							maxprice = prices[0].split(' - ')[1]
						print("done")
						description = d['descriptions'][2]['value']
						print("done")
						data = "".join(re.findall(r'ago">(.+?)<',pricesource))
						high+=float(maxprice.replace("$","").replace("€","").replace(",",".").replace("-","").replace(" ",""))
						low+=float(minprice.replace("$","").replace("€","").replace(",",".").replace("-","").replace(" ",""))
						embed = discord.Embed(title = "RushB inventory command" , description = f"Player's inventory stats | Weapon description: {description}" , color=0xffdd00)
						embed.set_thumbnail(url = avatar)
						embed.set_image(url = img)
						embed.add_field(name = "Name" , value = d['name'])
						embed.add_field(name = "Highest Price" , value = f"{maxprice}")
						embed.add_field(name = "Lowest Price" , value = f"{minprice}")
						embed.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
						embedpages.append(embed)
			main.add_field(name = "Highest Rate" , value = f"${high}")
			main.add_field(name = "Lowest Rate" , value = f"${low}")
			main.add_field(name = "Total Skins" , value = f"{total_skins}")
			main.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
			embedpages.insert(0,main)
			i = 1
			for e in embedpages:
				e.set_footer(text = f"page {i}/{len(embedpages)}")
				i+=1
			message = await ctx.send(embed = main)
			await message.add_reaction('◀️')
			await message.add_reaction('▶️')
			i = 0
			emoji = ""
			while True:
				if emoji == '◀️':
					if i>0:
						i -=1
						await message.edit(embed=embedpages[i])
				elif emoji == '▶️':
					if i<len(embedpages) -1:
						i+=1
						await message.edit(embed = embedpages[i])
				reaction , user=await client.wait_for('reaction_add')
				if str(user)!='RushB#8124' and str(user) == str(ctx.message.author): #Example: 'MyBot#1111'
					emoji=str(reaction.emoji)
					await message.remove_reaction(reaction,user)
			await client.clear_reactions(message)
	except Exception as e:
		print(e)
		await ctx.send("ERROR in command")
@client.command(pass_context = True)
async def servers(ctx,*args):
	t = ""
	print(args)
	print(len(args))
	if len(args) == 1:
		s= requests.get(f"https://www.gametracker.com/search/csgo/{args[0]}/?").text
	elif len(args) == 2:
		t = args[1]
		s = requests.get(f"https://www.gametracker.com/search/csgo/{args[0]}/?query={args[1]}").text
	ip = re.findall(r'<span class="ip">(.+?)<',s)
	port = re.findall(r'<span class="port">(.+?)<',s)
	l = [f"{ip[i]}{port[i]}" for i in range(len(ip))]
	flags = re.findall(r'/images/flags/(.+?).gif',s)
	players = re.findall(r'<td>\n					(.+?)\n',s)
	players = [c for c in players if c.count("/") == 1 and "<b>" not in c]
	names = re.findall(r'<a  href="/server_info/(.+?)</a>',s,re.DOTALL)
	names = [c.replace('\n','').replace('\t','').split('>')[1] for c in names]
	maps = re.findall(r'<span class="ip">(.+?)</tr>',s,re.DOTALL)
	maps = [re.findall(r'</span></td><td>(.+?)<',m.replace('\n','').replace('\t',''))[0] for m in maps]
	l = len(flags)
	country = pycountry.countries.get(alpha_2=args[0].upper())
	embed = discord.Embed(title = "RushB Servers command" , description = f"Top {l} **{t}** servers in **{country.name}** :flag_{args[0].lower()}:")
	embed.set_thumbnail(url = f"https://www.countryflags.io/{args[0]}/shiny/64.png")
	embed.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
	for i in range(l):
		if len(names[i] )> 20:
			name = names[i][0:20]+"..."
		else:
			name = names[i]
		embed.add_field(name = f"➤{i+1} {name}" , value = f"Players = <:Players:745436575386828801> {players[i]}  , <:IP:745437491569623110> __***{ip[i]}{port[i]}***__ [<:join_arrow:599612545002635274>](steam://connect/{ip[i]}{port[i]}), Map = **{maps[i]}**",inline = False)
	await ctx.send(embed = embed)
@client.command(pass_context = True)
async def status(ctx,arg):
	embed = discord.Embed(title = "RushB Status command" , description = f"Status for server with ip **{arg}**")
	SERVER_ADDRESS = (str(arg.split(':')[0]), int(arg.split(':')[1]))
	try:
		with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:
		    info = server.info()
		    players = server.players()
		name = info['server_name']
		if len(name)>50:
			name = name[0:46] + "..."
		embed.add_field(name = ":green_circle:‏‏‎"  , value = f"**➤Players <:Players:745436575386828801> :**{info['player_count']}/{info['max_players']}\n **➤Name :speech_balloon: :** __*{name}*__\n➤**Map :map: :** *{info['map']}*" , inline = True)
		i = 1
		c = []
		for player in sorted(players["players"],
		                     key=lambda p: p["score"], reverse=True):
			time = datetime.timedelta(seconds = round(player["duration"]))
			c.append(f"__**{player['name']}**__ | **➤Score** : __*{player['score']}*__ | :stopwatch:__*{time}*__\n")
			i = i+1
			if i>10:
				break
		playerz = "".join(c)
		if len(playerz) ==0:
			embed.add_field(name = f"Server is empty :(" , value = "There are no players on the server" , inline = False)	
		else:
			embed.add_field(name = f"Players Top {i}" , value = f"{playerz}" , inline = False)	
		embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/600px-Steam_icon_logo.svg.png")
		embed.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
		await ctx.send(embed = embed)
	except Exception as e:
		print(e)
		await ctx.send("Server is OFF or The ip provided is invalid")
@client.command(pass_context = True)
async def mm(ctx):
	data = getcomp()
	print(data)
	#
	playeron = re.findall(r'players_online: (.+?)\n',data)[0]
	servers = re.findall(r'servers_available: (.+?)\n',data)[0]
	playerser=re.findall(r'players_searching: (.+?)\n',data)[0]
	maatches=re.findall(r'ongoing_matches: (.+?)\n',data)[0]
	time=re.findall(r'search_time_avg: (.+?)\n',data)[0]
	ms = int(time) % 1000
	secondes = int(time) // 1000
	minutes = secondes //60
	secondes = secondes % 60
	time = datetime.timedelta(seconds = secondes)
	embed=discord.Embed(title = "RushB Matchmaking Command" , description = "Current Matchmaking Global stats")
	embed.set_author(name = "Game : Counter Strike Global Offensive",icon_url = "https://csgo-lobby.fr/wp-content/uploads/2018/10/logo.png")
	embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/600px-Steam_icon_logo.svg.png")
	embed.add_field(name = "Global Stats" , value = f"**<:online:313956277808005120>Players Online:** `{playeron}`\n**<:online:313956277808005120>Servers Count:** `{servers}`\n**:mag:Players Searching:** `{playerser}`\n**<:streaming:313956277132853248>On going Matches:** `{maatches}`\n**:stopwatch:Search time avg:** `{minutes}:{secondes}`")
	await ctx.send(embed = embed)
async def overwatch(c,u,p):
	sclient = SteamClient()
	cs = CSGOClient(sclient)
	async def start_csgo(c , r , sclient):
		def check(m):
				return m.channel == c
		is_2fa = (result in (EResult.AccountLoginDeniedNeedTwoFactor,
                                 EResult.TwoFactorCodeMismatch,
                                 ))
		if is_2fa:
			await c.send("2FA is enabled , Please provide the 2fa code recived!")
			code = await  client.wait_for('message',check = check, timeout=10)
			r = sclient.login(two_factor_code=code.content,username =  u.content,password = p.content)
			if r == EResult.OK:
				cs.launch()
				time.sleep(5)
				await worker(cs , c)
			elif r in (EResult.AccountLogonDenied,
                      EResult.AccountLoginDeniedNeedTwoFactor,
                      ):
				await start_csgo(c , r , sclient)
			else:
				await c.send("2FA is Invalid! Quiting...")
		else:
			await c.send("Email Guard is Enabled! please provide the code recived in your email!")
			code = await  client.wait_for('message',check = check, timeout=10)
			r = sclient.login(auth_code=code.content, username =  u.content,password = p.content)
			if r == EResult.OK:
				cs.launch()
				time.sleep(5)
				await worker(cs , c)
			elif r in (EResult.AccountLogonDenied,
                      EResult.AccountLoginDeniedNeedTwoFactor,
                      ):
				await start_csgo(c , r , sclient)
			else:
				await c.send("Guard is Invalid! Quiting...")
		#client.login(auth_code=code, username =  u.content,password = p.content)
	async def worker(cs ,c ):
		await c.send("getting a case ...")
		data = {"reason":1}
		cs.send(ECsgoGCMsg.EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate,data)
		resp=cs.wait_event(ECsgoGCMsg.EMsgGCCStrike15_v2_PlayerOverwatchCaseAssignment  ,timeout = 10)
		if not("suspectid" in str(resp)):
			await c.send("No cases availabe at the moment!")
		await c.send("Found a case!")
		print(resp)
		caseid = re.findall(r'caseid: (.+?)\n',str(resp))
		print(caseid)
		suspectid = re.findall(r'suspectid: (.+?)\n',str(resp))
		fractionid = re.findall(r'fractionid: (.+?)\n',str(resp))
		data = {"caseid":int("".join(caseid)) , "statusid":1}
		await c.send("Donwloading Demo ... ")
		time.sleep(30)
		cs.send(ECsgoGCMsg.EMsgGCCStrike15_v2_PlayerOverwatchCaseStatus,data)
		await c.send("Parsing the demo")
		time.sleep(120)
		await c.send("Done parsing , Sending Verdict ... ")
		data = {"caseid":int("".join(caseid)),"suspectid":int("".join(suspectid)),"fractionid":int("".join(fractionid)),"rpt_aimbot":1,"rpt_wallhack":1,"rpt_speedhack":0,"rpt_teamharm":0,"reason":3}
		cs.send(ECsgoGCMsg.EMsgGCCStrike15_v2_PlayerOverwatchCaseUpdate,data)
		await c.send("Verdict sent ! logging off...")
		time.sleep(5)
		await c.send("Logged off!")
	result = sclient.login(username =   u.content,password = p.content)
	if result in (EResult.AccountLogonDenied,
                      EResult.InvalidLoginAuthCode,
                      EResult.AccountLoginDeniedNeedTwoFactor,
                      EResult.TwoFactorCodeMismatch,
                      ):
		await start_csgo(c , result , sclient)

	sclient.sleep(9)
@client.command(pass_context = True)
async def start_overwatch(ctx):

	c =await  ctx.author.create_dm()
	await c.send("Account Username :")
	def check(m):
		return m.channel == c
	username = await client.wait_for('message',check = check, timeout=10)
	await c.send("Account Password :")
	password = await client.wait_for('message',check = check, timeout=10)
	await c.send(f"Logging in into [{username.content}]")
	await overwatch(c,username,password)

		#await c.send("Succesfully Logged into the account")


@client.command(pass_context = True)
async def commands(ctx):
	embed = discord.Embed(title = "<:rushb:749050544798171219> RushB Commands" , description = "All available commands ",color = 0xffdd00)
	embed.add_field(name = "!rb profile [STEAMID/URL]" , value = "player profile rank , stats,match history , weapons...[<:plis:749054114897592430>](https://media.giphy.com/media/j1zEvxdwqGo7Ezt2LQ/giphy.gif)",inline=False)
	embed.add_field(name = "!rb live [STEAMID/URL]" , value = "Live Game Information : Ranks , score , map...[<:plis:749054114897592430>](https://media.giphy.com/media/kbuyOvdps1oMoT201o/giphy.gif)",inline=False)
	embed.add_field(name = "!rb faceit [STEAMID/URL]" , value = "Faceit player profile : level , rating ,...[<:plis:749054114897592430>](https://i.imgur.com/BCuNr4U.png)",inline=False)
	embed.add_field(name = "!rb inventory [STEAMID/URL]" , value = "Display player's inventory : skins , price , description...[<:plis:749054114897592430>](https://media.giphy.com/media/J5jbM0Lpkmrr5dS38Q/giphy.gif)",inline=False)
	embed.add_field(name = "!rb servers [Country_Code] [Filter]" , value = "Top 15 servers in the country provided[<:plis:749054114897592430>](https://media.giphy.com/media/XZxFV5QcXhaicMTfN2/giphy.gif)",inline=False)
	embed.add_field(name = "!rb status [IP:PORT]" , value= "Server Status : map , Player count , Players info (name , score...)[<:plis:749054114897592430>](https://i.imgur.com/tBTHPQp.png)",inline=False)
	embed.add_field(name = "!rb mm" , value = "Matchmaking stats : players online , serves , matches ...[<:plis:749054114897592430>](https://i.imgur.com/UWeKyjd.png)",inline=False)
	embed.set_footer(text = "70% of the data is gathered from steam API, since The API usage is limited. the rest of the info are scrapped from some CSGO stats sites such as the rank and the match history so the information you get are 60% valid because it all depends on the site's sync system")
	await ctx.send(embed = embed)
#client.run(os.environ["token"])
client.run("{Your_Bots_Token_Here}")
# send request message
