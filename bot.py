import discord


class NotFoundClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('$hi'):
            await message.channel.send('404 Not Found')

client = NotFoundClient()
client.run("")