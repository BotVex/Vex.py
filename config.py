import json
from random import choice
from disnake import Intents


prefix         = '-'
owner_ids      = [
  783120232134082580,
  728409113847136341
  ]

intents = Intents.default()
intents.members = True


def get_game():
	with open('data/games.json', 'r', encoding='utf8') as games:
		games = json.loads(games.read())
		return choice(games)


extensions  = [
	'cogs.adm.Clear',
	'cogs.basic.Ping',
	'cogs.entertainment.Anime',
	'cogs.Entertainment',
	'cogs.ImageFilter',
	'cogs.Owner',
	'cogs.Tools'
]

"""
extensions  = [
	'cogs.adm.Clear',
	'cogs.basic.Help',
	'cogs.basic.Ping',
	'cogs.entertainment.Anime',
	'cogs.entertainment.Mojis',
	'cogs.entertainment.Owofy',
	'cogs.entertainment.Rg',
	'cogs.image.Contrast',
	'cogs.image.Equalize',
	'cogs.image.Flip',
	'cogs.image.Mirror',
	'cogs.image.Invert',
	'cogs.image.Posterize',
	'cogs.image.Solarize',
	'cogs.image.Gray',
	'cogs.image.Sharpness',
	'cogs.tools.Color',
	'cogs.tools.Qr',
	'cogs.Owner'
]
"""



TOKEN = 'NzgzNzE2ODgyODk2OTEyNDA1.X8ezOQ.QuCeUnPJf2Mp9KHxdrELDcr0i7Y'


CDEFAULT = 0x000000
COWNER = 0xFF3889
CERROR = 0xFF4141