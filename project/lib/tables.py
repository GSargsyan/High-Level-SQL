from project.lib.databases import *
from project.lib.io import Writer, Reader
from configs import DBS_PATH
import os
import json
import project

class Tables:
    data_types = ('text', 'number', 'boolean')

    def check_database(function):
        def wrapper(*args, **kwargs):
            if not hasattr(Tables, 'db'):
                error('No database selected')
            return function(*args, **kwargs)
        return wrapper

    @staticmethod
    @check_database
    def create_table(tb_name, meta_str):
        if os.path.exists(DBS_PATH + Tables.db.name + '/' + tb_name):
            error('Table ' + tb_name + ' already exists')
        try:
            meta = json.loads(meta_str)
        except:
            error('Invalid JSON provided')

        if Tables.is_valid_meta(meta):
            meta['id'] = {'type': 'serial'}
            mkdir(Tables.db.path + tb_name)
            # Reader().read_obj(path, tb_name)
            Writer().write(file_path=Tables.db.path + 'meta.json',
                    data={tb_name: meta})
        success('Created table ' + tb_name)

    @staticmethod
    def is_valid_meta(meta):
        from project.lib.commands import REFERENCE_TYPES, DATA_TYPES
        if not isinstance(meta, dict):
            error('Invalid meta provided')

        for col_name, data in meta.items():
            if 'type' not in data:
                error('Type of column ' + col_name ' is not specified')
            if data['type'] == 'mapping':
                if 'points' not in data:
                    error('Invalid meta provided for ' + col_name)
                elif not Tables.db.has_table(data['points']):
                    error('Table ' + data['points'] + ' doesn\'t exist')
            else:
                if data['type'] not in DATA_TYPES:
                    error('Unknown data type: ' + data['type'])
                elif 'reference' not in data:
                    error('Invalid meta provided for ' + col_name)
                elif data['reference'] not in REFERENCE_TYPES:
                    error('Unknown reference type: ' + data['reference'])
        return True

    @staticmethod
    def set_database(db_name):
        if hasattr(Tables, 'db') and Tables.db.name == db_name:
            warning('Already on ' + db_name)
        elif not os.path.exists(DBS_PATH + db_name):
            error('Database ' + db_name + ' doesn\'t exist')
        else:
            Tables.db = Database(db_name)
            success('Switched to database ' + db_name)

    @staticmethod
    def select_from_table(tb_name, *args, **kwargs):
        pass

    @staticmethod
    def insert_data(tb_name, data):
        table = Table(Tables.db, tb_name)
        table.insert(data)


class Table:
    def __init__(self, db, name):
        if not isinstance(db, Database):
            error('Provided database is not of type Database')
        if not os.path.exists(db.path + name):
            error('Table ' + name + ' doesn\'t exist')

        self.__db = db
        self.__name = name

    def insert(self, json_data):
        from project.lib.commands import REFERENCE_TYPES, DATA_TYPES
        try:
            data = json.loads(json_data)
        except:
            error('Failed parsing JSON data')
        tb_meta = Reader.read_obj(self.__db.path + 'meta.json', self.__name)
        for col_name, val in data:
            col_meta = tb_meta.get(col_name, None)
            col_type = col_meta['type']

            if col_meta is None:
                error('No column named ' + col_name)
            if col_type == 'text' and not isinstance(val, str):
                error('Expected string for column ' + col_name)
            elif col_type == 'bool' and not type(val) != type(True):
                error('Expected boolean for column ' + col_name)
            elif col_type == 'number' and not isinstance(val, (int, float))
                error('Expected number for column ' + col_name)
            # TODO: additional checkings ?

    def gen_id(tb)
        # TODO: implement concept of id
        pass

    def select(self, fields):
        pass
