#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import urllib2
import urllib
import re
import os
import yaml
import scrape_engine
import constants
from datastructures import SearchResult, GameInfo
__scrapername__ = "TheGamesDB"
__scraperauthor__ = ["Angelscry", "ron975"]
__scrapersite__ = "thegamesdb.net"
__scraperdesc__ = "Scrapes ROM information from TheGamesDB API"
__scraperfanarts__ = True
__scraperpath__ = os.path.dirname(os.path.realpath(__file__))
__scrapermap__ = yaml.load(open(os.path.join(__scraperpath__, "scrapermap.yml")))

def get_games_by_name(search):
    results = []
    try:
        req = urllib2.Request('http://thegamesdb.net/api/GetGamesList.php?name='+urllib.quote_plus(search))
        req.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
        f = urllib2.urlopen(req)
        page = f.read().replace("\n", "")
        games = re.findall("<Game><id>(.*?)</id><GameTitle>(.*?)</GameTitle>(.*?)<Platform>(.*?)</Platform></Game>",
                           page)
        for item in games:
            game = {}
            game["id"] = "http://thegamesdb.net/api/GetGame.php?id=" + item[0]
            game["title"] = item[1]
            game["system"] = item[3]
            game["order"] = 1
            if game["title"].lower() == search.lower():
                game["order"] += 1
            if game["title"].lower().find(search.lower()) != -1:
                game["order"] += 1
            results.append(game)
        results.sort(key=lambda result: result["order"], reverse=True)
        return [SearchResult(result["title"], result["id"]) for result in results]
    except:
        return None


def get_games_with_system(search, system):
    scraper_sysid = __scrapermap__[system]
    params = urllib.urlencode({"name": search, "platform": scraper_sysid})
    results = []
    try:
        req = urllib2.Request('http://thegamesdb.net/api/GetGamesList.php?name='+urllib.quote_plus(search)+'&platform='+urllib.quote_plus(scraper_sysid))
        req.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
        f = urllib2.urlopen(req)
        page = f.read().replace("\n", "")
        if system == "Sega Genesis":
            req = urllib2.Request('http://thegamesdb.net/api/GetGamesList.php?name='+urllib.quote_plus(search)+'&platform='+urllib.quote_plus('Sega Mega Drive'))
            req.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
            f2 = urllib2.urlopen(req)
            page = page + f2.read().replace("\n", "")
        games = re.findall("<Game><id>(.*?)</id><GameTitle>(.*?)</GameTitle>(.*?)<Platform>(.*?)</Platform></Game>",
                           page)
        for item in games:
            game = {}
            game["id"] = item[0]
            game["title"] = item[1]
            game["system"] = item[3]
            game["order"] = 1
            if game["title"].lower() == search.lower():
                game["order"] += 1
            if game["title"].lower().find(search.lower()) != -1:
                game["order"] += 1
            if game["system"] == scraper_sysid:
                game["system"] = system
                results.append(game)
        results.sort(key=lambda result: result["order"], reverse=True)
        return [SearchResult(result["title"], result["id"]) for result in results]
    except:
        return None


def get_game_datas(game_id):
    gamedata = {
        'title': "",
        'genre': "",
        'release': "",
        'publisher': "",
        'description': ""
    }

    try:
        req = urllib2.Request("http://thegamesdb.net/api/GetGame.php?id=" + game_id)
        req.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
        f = urllib2.urlopen(req)
        page = f.read().replace('\n', '')
        game_genre = ' / '.join(re.findall('<genre>(.*?)</genre>', page))
        if game_genre:
            gamedata["genre"] = scrape_engine.format_html_codes(game_genre)
        game_release = ''.join(re.findall('<ReleaseDate>(.*?)</ReleaseDate>', page))
        if game_release:
            gamedata["release"] = scrape_engine.format_html_codes(game_release)
        game_studio = ''.join(re.findall('<Publisher>(.*?)</Publisher>', page))
        if game_studio:
            gamedata["publisher"] = scrape_engine.format_html_codes(game_studio)
        game_plot = ''.join(re.findall('<Overview>(.*?)</Overview>', page))
        if game_plot:
            gamedata["description"] = scrape_engine.format_html_codes(game_plot)
        game_title = ''.join(re.findall('<GameTitle>(.*?)</GameTitle>', page))
        if game_title:
            gamedata["title"] = scrape_engine.format_html_codes(game_title)
        boxarts = re.findall(r'<boxart side="front" (.*?)">(.*?)</boxart>', page)[0][1]
        boxarts = "http://thegamesdb.net/banners/" + boxarts

        return GameInfo(
            title=gamedata["title"],
            publisher=gamedata["publisher"],
            description=gamedata["description"],
            release_date=[gamedata["release"].split("/")[2],
                          gamedata["release"].split("/")[0],
                          gamedata["release"].split("/")[1]],
            genre=gamedata["genre"],

            images={
                constants.key_boxarts: boxarts
            }
        )
    except UnboundLocalError:

        return None
