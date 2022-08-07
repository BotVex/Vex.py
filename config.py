import os
from disnake import Intents
from dotenv import load_dotenv

load_dotenv()

OWNER_ID = 783120232134082580
GUILD_ID = 939585882883772436

INTENTS = Intents.default()
INTENTS.members = True
INTENTS.presences = True

EXTENSIONS = ['cogs.Events', 'cogs.Entertainment', 'cogs.Administration', 'cogs.Tools', 'cogs.Bot'] #https://github.com/aurelmegn/heroku-buildpack-google-chrome

TOKEN = os.environ['TOKEN']
