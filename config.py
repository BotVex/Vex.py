import os
from dotenv import load_dotenv

load_dotenv()

OWNER_ID = 783120232134082580
GUILD_ID = 939585882883772436

EXTENSIONS = ['events', 'errors', 'tools', 'misc', 'admin', 'bot', 'ctxs_menus']

TOKEN = os.environ['TOKEN']
