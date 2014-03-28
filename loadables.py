import os
import glob
import yaml
from scrapercommon import ScraperInfo
from singleton import Singleton

@Singleton
class Loadables:
    def __init__(self):
        self.scrapers = self.load_scrapers()
        self.platforms = self.load_platforms()

    def load_scrapers(self):
        scraperdef = self.get_loadables("scrapers")
        scrapers = {}
        for scraper in scraperdef[0]:
            info = yaml.load(open(scraper))
            scrapers[info['name']] = ScraperInfo(info['name'], os.path.join(scraperdef[1], info['name'], 'scraper.py'))
        return scrapers

    def load_platforms(self):
        platformdef = self.get_loadables("platforms")
        platforms = {}
        for platform in platformdef[0]:
            info = yaml.load(open(platform))
            platforms[info.platform_id] = info
        return platforms

    def get_loadables(self, type, ext='yml'):
        loadablesdir = os.path.join(os.getcwd(), "loadables", type)
        return (glob.glob(os.path.join(loadablesdir, '*.'+ext)), loadablesdir)
