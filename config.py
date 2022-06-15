import json
from random import choice
from disnake import Intents
import os
from dotenv import load_dotenv

load_dotenv()

owner_ids      = [
  783120232134082580,
  728409113847136341
  ]
guild_ids      = [
	957509903273046067
	]

intents = Intents.default()
intents.members = True
intents.presences = True



extensions  = [
	'cogs.Entertainment',
	'cogs.Image',
	'cogs.Owner',
	'cogs.Administration',
	'cogs.Tools'
]


TOKEN = os.environ["TOKEN"]