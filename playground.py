#This file is not for production.

import yaml
import json
import database
import os
import glob
import sys
import constants
from loadables import Loadables
from platforms import EmulatorInfo
from scraper import ScraperInfo


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
    loadables = Loadables.Instance()
    snes = loadables.platforms["NINTENDO_SNES"]
    loadables.emulators["retroarch"].execute_rom(snes.commandline, "smw.smc")
main()
