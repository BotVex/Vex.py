import os
from disnake import Intents
from dotenv import load_dotenv

load_dotenv()

OWNER_ID = 783120232134082580
GUILD_ID = 939585882883772436

EXTENSIONS = ['cogs.Events', 'cogs.Entertainment', 'cogs.Administration', 'cogs.Tools', 'cogs.Bot', 'cogs.ContextMenus']

TOKEN = os.environ['TOKEN']
