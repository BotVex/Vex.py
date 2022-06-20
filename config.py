from disnake import Intents
import os
from dotenv import load_dotenv

load_dotenv()

owner_ids      = [
  783120232134082580,
  728409113847136341
  ]
guild_ids      = [
	939585882883772436
	]

intents = Intents.default()
intents.members = True
intents.presences = True



extensions  = [
	'cogs.Events',
	'cogs.Entertainment',
	'cogs.Image',
	'cogs.Owner',
	'cogs.Administration',
	'cogs.Tools'
]

	
TOKEN = os.environ['TOKEN']
