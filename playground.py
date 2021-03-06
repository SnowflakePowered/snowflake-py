#This file is not for production.

import yaml
import json
import gameinfo
import os
import glob
import sys
import constants
from loadables import Loadables
from platforms import EmulatorInfo
import platformids
from scraper import ScraperInfo
import database


def serialize():
    snes = yaml.load(open('loadables/platforms/NINTENDO_SNES.yml'))
    print (snes.file_extensions[0])
    scraper = Loadables.Instance().scrapers['thegamesdb']

    scrapercore = scraper.scraper
    res = scrapercore.get_games_with_system("A Link to the Past",platformids.NINTENDO_SNES)[0]
    data = scrapercore.get_game_datas(res.source_id)
    return data

def dab():
    db = database.GamesDatabase(os.path.dirname(__file__))
    db.create_database()
    db.add_game(serialize(), "ali.smc")

import images

def main():
  #  loadables = Loadables.Instance()
  #  db = gameinfo.GamesDatabase(os.path.dirname(__file__))
   # dab()
   # game = db.get_game('mTbUQtQz8eYowBqV6o62uj')
    #game.run()
   # games = db.get_games_for_platform("NINTENDO_SNES")
   # games[2].run()
    #snes = loadables.platforms["NINTENDO_SNES"]
    #loadables.emulators["retroarch"].execute_rom(snes.commandline, "smw.smc")
    image = images.GameImage.get_remote_image('http://thegamesdb.net/banners/boxart/original/front/1318-1.jpg')
    print (image.cachepath)
