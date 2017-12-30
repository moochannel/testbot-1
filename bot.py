import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client.user.id}: {client.user.name}')
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await client.send_message(message.channel, 'Hello world!')


if __name__ == '__main__':
    client.run('BOT_USER_TOKEN_HERE')
