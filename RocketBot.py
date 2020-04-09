from instagram_web_api import Client, ClientCompatPatch, ClientError
from RocketClient import RocketClient
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ROCKET_ID =  os.getenv('ROCKET_ID')

rocket_client = RocketClient()
rocket_urls = []
cursor = None

client = discord.Client()
e = discord.Embed()

while True: # get rocket urls until there's no cursor
  rocket_feed = rocket_client.user_feed(ROCKET_ID, count=50, end_cursor=cursor, query=cursor)
  for rocket in rocket_feed:
    rocket_urls += [rocket['node']['display_resources'][-1]['src']]
  cursor = rocket_feed[-1]['node']['edge_media_to_comment']['page_info']['end_cursor']
  if cursor == None:
    break

@client.event
async def on_ready():
  print('Rocket Launch!')

@client.event
async def on_message(message):
  if message.content.startswith('+rocket'):
    e.set_image(url=random.choice(rocket_urls))
    await message.channel.send(embed=e)

client.run(TOKEN)