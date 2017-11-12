import os
from project.lib.helper import *

class Databases:
    @staticmethod
    def create_database(name):
        if mkdir('databases/', name):
            success('Created database ' + name)
        else:
            error('Database ' + name + ' already exists')

    @staticmethod
    def create_db(name):
        create_database(name)


class Tables:
    @staticmethod
    def create_table(db, meta_str):
        try:
            meta = json.loads(meta_str)
        except:
            error('Failed to load meta of the table')
