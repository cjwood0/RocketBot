from instagram_web_api import Client, ClientCompatPatch, ClientError
from RocketClient import RocketClient
import os
import discord
import random
from dotenv import load_dotenv

def get_rocket_urls():
    rocket_id =  os.getenv('ROCKET_ID')
    rocket_client = RocketClient(auto_patch=True, drop_incompat_keys=False)
    rocket_feed = rocket_client.user_feed(rocket_id, count=50)
    urls = []

    for rocket in rocket_feed:
        urls += [rocket['node']['images']['standard_resolution']['url']]

    cursor = rocket_feed[-1]['node']['edge_media_to_comment']['page_info']['end_cursor']
    while cursor:
        rocket_info = rocket_client.user_feed(rocket_id, count=50, end_cursor=cursor, query=cursor)
        for rocket in rocket_info:
            urls += [rocket['node']['display_resources'][-1]['src']]
        cursor = rocket_info[-1]['node']['edge_media_to_comment']['page_info']['end_cursor']
    return urls

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

rocket_urls = get_rocket_urls()

client = discord.Client()

@client.event
async def on_ready():
    print('Rocket is connected to Discord!')

@client.event
async def on_message(message):
    e = discord.Embed()

    if message.author == client.user:
        return

    if message.content.startswith('+rocket'):
        e.set_image(url=random.choice(rocket_urls))
        await message.channel.send(embed=e)

client.run(TOKEN)