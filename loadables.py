import os
import glob
import yaml
from scraper import ScraperInfo
from singleton import Singleton
import constants


@Singleton
class Loadables:
    def __init__(self):
        self.scrapers = self.load_scrapers()
        self.platforms = self.load_platforms()
        self.emulators = self.load_emulators()

    def load_scrapers(self):
        #load scrapers from yml files
        scraperdef = self.get_loadables("scrapers")
        scrapers = {}
        for scraper in scraperdef[0]:
            info = yaml.load(open(scraper))
            scrapers[info['name']] = ScraperInfo(info['name'], os.path.join(scraperdef[1], info['name'], 'scraper.py'))
        return scrapers

    def load_platforms(self):
        #load platforms from yml file
        platformdef = self.get_loadables("platforms")
        platforms = {}
        for platform in platformdef[0]:
            info = yaml.load(open(platform))
            platforms[info.platform_id] = info
        return platforms

    def load_emulators(self):
        emulatordef = self.get_loadables("emulators")
        emulators = {}
        for emulator in emulatordef[0]:
            info = yaml.load(open(emulator))
            emulators[info.name] = info
        return emulators

    def get_loadables(self, type, ext='yml'):
        #get yml loadables
        loadablesdir = os.path.join(constants.loadables_path, type)
        return glob.glob(os.path.join(loadablesdir, '*.'+ext)), loadablesdir
