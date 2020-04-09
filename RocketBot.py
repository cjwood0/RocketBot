from instagram_web_api import Client, ClientCompatPatch, ClientError
from MyClient import MyClient
import os
import discord
import random
from dotenv import load_dotenv

def get_rocket_urls():
    user_id =  os.getenv('ROCKET_ID')
    web_api = MyClient(auto_patch=True, drop_incompat_keys=False)
    user_feed_info = web_api.user_feed(user_id, count=50)
    urls = []

    for post in user_feed_info:
        urls += [post['node']['images']['standard_resolution']['url']]

    cursor = user_feed_info[-1]['node']['edge_media_to_comment']['page_info']['end_cursor']
    while cursor:
        feed_info = web_api.user_feed(user_id, count=50, end_cursor=cursor, query=cursor)
        for post in feed_info:
            urls += [post['node']['display_resources'][-1]['src']]
        cursor = feed_info[-1]['node']['edge_media_to_comment']['page_info']['end_cursor']
    return urls

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

rocket_urls = get_rocket_urls()

client = discord.Client()

@client.event
async def on_ready():
    print('Connected to Discord!')

@client.event
async def on_message(message):
    e = discord.Embed()

    if message.author == client.user:
        return

    if message.content.startswith('+rocket'):
        e.set_image(url=random.choice(rocket_urls))
        await message.channel.send(embed=e)

client.run(TOKEN)