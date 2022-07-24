import os
from disnake import Intents
from dotenv import load_dotenv

load_dotenv()

owner_id = 783120232134082580
guild_id = 939585882883772436

intents = Intents.default()
intents.members = True
intents.presences = True

extensions  = ['cogs.Events', 'cogs.Entertainment', 'cogs.Administration', 'cogs.Tools', 'cogs.Bot', 'cogs.Sfx']

TOKEN = os.environ['TOKEN']

