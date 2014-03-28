import json


class RunnableGame():
    def __init__(self, uuid, filename, gameinfo):
        self.uuid = uuid
        self.filename = filename
        self.gameinfo = gameinfo

    def run(self):
        #platform = constants.loadables.platforms[self.gameinfo.platform] #todo load platforminfo
        #emulator = constants.loadables.emulators[platform.emulator] #todo load emulators
        #emulator.run(platform.commandline.replace('[rom]', self.filename))
        pass


class GameInfo:
    def __init__(self, title, publisher, description, genre,
                 release_date, platform="NINTENDO_SNES", images={}, metadata=[]):
        self.title = title
        self.publisher = publisher
        self.platform = platform
        self.description = description
        self.genre = genre
        self.release_date = release_date
        self.metadata = metadata
        self.images = images

    def serialize_releasedate(self):
        return '-'.join(str(value) for value in self.release_date)

    def serialize_images(self):
        return json.dumps(self.images).replace('"', "'")

    def serialize_metadata(self):
        return json.dumps(self.metadata).replace('"', "'")