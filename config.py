import json
from random import choice
from disnake import Intents


prefix         = '-'
owner_ids      = [
  783120232134082580,
  728409113847136341
  ]
guild_ids      = [
	957509903273046067
	]

intents = Intents.default()
intents.members = True


extensions  = [
	'cogs.Entertainment',
	'cogs.Image',
	'cogs.Owner',
	'cogs.Administration',
	'cogs.Tools'
]


TOKEN = 'NzgzNzE2ODgyODk2OTEyNDA1.X8ezOQ.QuCeUnPJf2Mp9KHxdrELDcr0i7Y'