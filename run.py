from App.bot import bot, config
from Exts.discord_presense_task import change_status


@bot.event
async def on_ready():
    print(f'[*] Logged is as [{bot.user.name}]')
    print(f'[*] CID: {str(bot.user.id)}')
    print(f'[*] zeroday0619 | Copyright (C) 2020 zeroday0619')
    await change_status.start()


bot.remove_command("help")
# Cog Extension

bot.loop.run_until_complete(bot.run(config["token"]))
