import hashlib, string, random, instagram_web_api

class RocketClient(instagram_web_api.Client):
  def __init__(self):
    super(RocketClient, self).__init__(auto_patch=True, drop_incompat_keys=False)

  @staticmethod
  def _extract_rhx_gis(html):
      options = string.ascii_lowercase + string.digits
      text = ''.join([random.choice(options) for _ in range(8)])
      return hashlib.md5(text.encode()).hexdigest()