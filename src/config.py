import os
import tomllib
from dotenv import load_dotenv


load_dotenv()

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

EXTENSIONS = config.get("extensions", {}).get("extensions")

OWNER_ID = int(os.environ["OWNER_ID"])
GUILD_ID = int(os.environ["GUILD_ID"])

TOKEN = os.environ["TOKEN"]
