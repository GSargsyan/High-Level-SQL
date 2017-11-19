import os
from project.lib.helper import *

class Databases:
    @staticmethod
    def create_database(name):
        if mkdir('databases/', name):
            success('Created database ' + name)
        else:
            error('Database ' + name + ' already exists')

        open('databases/' + name + '/meta.json', 'r'):

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

    @staticmethod
    def parse_meta(meta):
        if not isinstance(meta, dict):
            error('Invalid meta provided')

        for colname, data in meta.items():
            pass
         
    @staticmethod
    def parse_column(meta):
        if not isinstance(meta, dict):
            error('Invalid meta provided')
