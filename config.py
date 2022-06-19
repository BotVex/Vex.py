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
	'cogs.Entertainment',
	'cogs.Image',
	'cogs.Owner',
	'cogs.Administration',
	'cogs.Tools'
]

	
TOKEN = "ODI3NjEwMTk3MjQ1MTY1NTc4.GWD-a-.2X63PS7A1ZKB6XQfHn64XKBvXyvixXeZBVjB7s" #os.environ["TOKEN"]
