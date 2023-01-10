import os
import tomllib
from dotenv import load_dotenv


load_dotenv()

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

OWNER_ID = config.get('owner', {}).get('id')
GUILD_ID = config.get('server', {}).get('guild_id')

EXTENSIONS = config.get('extensions', {}).get('extensions')

TOKEN = os.environ['TOKEN']
