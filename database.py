import sqlite3
import json
import os
import shortuuid
from games import GameInfo


class GamesDatabase():
    def __init__(self, path, new=False):
        self.database = sqlite3.connect(os.path.join(path, "games.db"))

    def create_database(self):
        self.database.cursor().execute('''CREATE TABLE IF NOT EXISTS games(
                                          uuid TEXT,
                                          filename TEXT,
                                          title TEXT,
                                          publisher TEXT,
                                          description TEXT,
                                          genre TEXT,
                                          release_date TEXT,
                                          platform TEXT,
                                          images TEXT,
                                          metadata TEXT
                                          );'''
        )
        self.database.commit()

    def add_game(self, game, filename):
        query = '''INSERT INTO games VALUES(
                                          "{uuid}",
                                          "{filename}",
                                          "{title}",
                                          "{publisher}",
                                          "{description}",
                                          "{genre}",
                                          "{release_date}",
                                          "{platform}",
                                          "{images}",
                                          "{metadata}"
                                      );'''.format(
                **{
                    'uuid': shortuuid.uuid(),
                    'filename': filename,
                    'title': game.title,
                    'publisher': game.publisher,
                    'description': game.description,
                    'genre': game.genre,
                    'release_date': game.serialize_releasedate(),
                    'platform': game.platform,
                    'images': game.serialize_images(),
                    'metadata': game.serialize_metadata()
                }
            )

        print query
        self.database.cursor().execute(query
        )

        self.database.commit()






