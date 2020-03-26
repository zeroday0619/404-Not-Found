from discord.ext import commands
from Exts.config import Config

config = Config()

bot = commands.Bot(
    command_prefix=config["command_prefix"],
    case_insensitive=config["case_insensitive"],
    description=config["description"],
    owner_id=config["owner_id"]
)