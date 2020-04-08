from instagram_web_api import Client, ClientCompatPatch, ClientError
from MyClient import MyClient
import os
import discord
from dotenv import load_dotenv

def get_rocket_url():
    user_id = '8380370132'
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

client = discord.Client()

@client.event
async def on_ready():
    print(client.user + ' has connected to Discord!')

client.run(TOKEN)