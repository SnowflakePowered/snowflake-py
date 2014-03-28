#This file is not for production.

import yaml
import json
import database
import os
import glob
import sys
import constants
from scrapercommon import ScraperInfo


def serialize():
    snes = yaml.load(open('loadables/platforms/NINTENDO_SNES.yml'))
    print snes.file_extensions[0]
    #es = scraper.get_games_with_system("Super Mario World", "NINTENDO_SNES")[0]
    #data = scraper.get_game_datas(res.source_id)
    #return data

def db():
    db = database.GamesDatabase(os.path.dirname(__file__))
    db.create_database()
    db.add_game(serialize(), "smw_somefilename.smc")

def main():
    import platforms
    print constants.loadables.platforms[platforms.NINTENDO_SNES].__dict__

main()
