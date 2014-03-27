import os
import glob
import yaml
from datastructures import Scraper

class Loadables:
    def __init__(self):
        self.scrapers = self.load_scrapers()

    def load_scrapers(self):
        scrapersdir = os.path.join(os.getcwd(), "scrapers")
        scraperdef = glob.glob(os.path.join(scrapersdir, '*.yml'))
        scrapers = {}
        for scraper in scraperdef:
            info = yaml.load(open(scraper))
            scrapers[info['name']] = Scraper(info['name'], os.path.join(scrapersdir, info['name'], 'scraper.py'))
        return scrapers