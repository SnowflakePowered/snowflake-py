import json

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