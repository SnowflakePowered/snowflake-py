import json
import imp
import os
from collections import namedtuple

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


class PlatformInfo:
    def __init__(self, platform_id, full_name, short_name, company, release_date, emulator,
                 commandline, scrapers, file_extensions, images={}, metadata=[]):
        self.platform_id = platform_id
        self.full_name = full_name
        self.short_name = short_name
        self.company = company
        self.emulator = emulator
        self.commandline = commandline
        self.scrapers = scrapers
        self.file_extensions = file_extensions
        self.metadata = metadata
        self.release_date = release_date
        self.images = images

class RunnableGame():
    def __init__(self, uuid, filename, gameinfo):
        self.uuid = uuid
        self.filename = filename
        self.gameinfo = gameinfo


class SearchResult(namedtuple('SearchResult', 'game_title source_id')):
    pass


class Scraper:
    def __init__(self, name, filename):
        self.name = name
        self.scraper = imp.load_source('.'.join(['snowflake', 'scraper', name]), filename)

class EmulatorInfo:
    def __init__(self, emulator_name, emulator_path, emulator_config):
        self.emulator_name = emulator_name
        self.emulator_path = emulator_path
        self.emulator_config = emulator_config

