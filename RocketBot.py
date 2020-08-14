import os, discord, random, RocketClient, aiohttp, cv2
import numpy
from PIL import Image
import io
from dotenv import load_dotenv
from rocket_detection import detect_common_objects

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ROCKET_ID =  os.getenv('ROCKET_ID')

client = discord.Client()
e = discord.Embed()

rocket_client = RocketClient.RocketClient()
rocket_urls = []
cursor = None

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
  dogs_requested = 0
  if '+1' in message.content:
    dogs_requested = 1
  elif '+2' in message.content:
      dogs_requested = 2
  elif '+3' in message.content:
      dogs_requested = 3

  if message.content.startswith('+rocket'):
    if dogs_requested > 0:
      while True:
        rocket_url = random.choice(rocket_urls)
        async with aiohttp.ClientSession() as session:
          async with session.get(rocket_url) as resp:
            if resp.status != 200:
              return await channel.send('Could not download file...')
            res = Image.open(io.BytesIO(await resp.read()))
            res = numpy.array(res)

            dogs = detect_common_objects(res)
            if dogs == dogs_requested:
              e.set_image(url=rocket_url)
              await message.channel.send(embed=e)
              break
    else:
      e.set_image(url=random.choice(rocket_urls))
      await message.channel.send(embed=e)

client.run(TOKEN)