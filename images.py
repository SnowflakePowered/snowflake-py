import json
import shortuuid
import constants
import os
from urllib import request

class GameImages():
    def __init__(self, boxart_front="", boxart_back="", boxart_generic="", fanart=[], screenshots=[], banners=[]):
        self.boxart = {
            'ICELAKE_BOXART_FRONT': boxart_front,
            'ICELAKE_BOXART_BACK': boxart_back,
            'ICELAKE_BOXART_GENERIC': boxart_generic
        }
        self.fanart = fanart
        self.screenshots = screenshots
        self.banners = banners

    def __str__(self):
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize(cls, data):
        return json.loads(data)

class GameImage():
    def __init__(self, uuid):
        self.uuid = uuid
        self.cachepath = os.path.join(constants.image_cache, uuid)

    @classmethod
    def get_local_image(cls, uuid):
        return GameImage(uuid)

    @classmethod
    def get_remote_image(cls, url):
        uuid = shortuuid.uuid()
        cachepath = os.path.join(constants.image_cache, uuid)
        f = open(cachepath, 'wb')
        req = request.Request(url)
        req.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
        f.write(request.urlopen(req).read())
        f.close()
        return cls.get_local_image(uuid)


