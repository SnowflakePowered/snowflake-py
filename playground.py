#This file is not for production.

from datastructures import Scraper

import yaml
import json
import database
import os
import glob
import sys
def serialize():
    snes = yaml.load(open('loadables/platforms\NINTENDO_SNES.yml'))
    print snes.file_extensions[0]
    #es = scraper.get_games_with_system("Super Mario World", "NINTENDO_SNES")[0]
    #data = scraper.get_game_datas(res.source_id)
    #return data

def db():
    db = database.GamesDatabase(os.path.dirname(__file__))
    db.create_database()
    db.add_game(serialize(), "smw_somefilename.smc")

def loadscraper():
    scrapersdir = os.path.join(os.getcwd(), "scrapers")
    scraperdef = glob.glob(os.path.join(scrapersdir, '*.yml'))
    s = yaml.load(open(scraperdef[0]))
    scrapers = []
    for scraper in scraperdef:
        info = yaml.load(open(scraper))
        scrapers.append(Scraper(info['name'], os.path.join(scrapersdir, info['name'], 'scraper.py')))
    print scrapers
    print scrapers[0].scraper.get_games_with_system("Super Mario World", "NINTENDO_SNES")[0]
    print yaml.dump(s)
    print scraperdef
    print scrapersdir

loadscraper()
