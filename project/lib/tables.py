from project.lib.databases import Database
from project.lib.io import Writer, Reader
from project.lib.helper import success, error, mkdir, warning, touch
from configs import DBS_PATH
import os
import json


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
        if os.path.exists(Tables.db.path + tb_name):
            error('Table ' + tb_name + ' already exists')
        try:
            meta = json.loads(meta_str)
        except Exception:
            error('Invalid JSON provided')

        if Tables.is_valid_meta(meta):
            mkdir(Tables.db.path + tb_name)
            count_path = Tables.db.path + 'counters.json'
            if not os.path.exists(count_path):
                touch(count_path)
                Writer.write(count_path, data=[{tb_name: 1}])
            else:
                Writer.add_val(count_path, val={tb_name: 1})

            Writer.write(file_path=Tables.db.path + 'meta.json',
                         data={tb_name: meta}, mode='a')
        success('Created table ' + tb_name)

    @staticmethod
    def is_valid_meta(meta):
        from project.lib.commands import REFERENCE_TYPES, DATA_TYPES
        if not isinstance(meta, dict):
            error('Invalid meta provided')

        for col_name, data in meta.items():
            if 'type' not in data:
                error('Type of column ' + col_name + ' is not specified')
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

    @check_database
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
        try:
            data = json.loads(json_data)
        except Exception:
            error('Failed parsing JSON data')
        tb_meta = Reader.read_obj(self.__db.path + 'meta.json', self.__name)
        for col_name, val in data:
            col_meta = tb_meta.get(col_name, None)
            col_type = col_meta['type']

            if col_meta is None:
                error('No column named ' + col_name)
            if col_type == 'text' and not isinstance(val, str):
                error('Expected string for column ' + col_name)
            elif col_type == 'bool' and not isinstance(val, bool):
                error('Expected boolean for column ' + col_name)
            elif col_type == 'number' and not isinstance(val, (int, float)):
                error('Expected number for column ' + col_name)

        data['id'] = self.__get_next_id()
        self.__increment_id()
        # TODO: write inserted data to some file.


    def __get_next_id(self):
        counters = Reader.read_list(self.__db.path + 'counters.json') 
        for item in counters:
            if self.__name in item:
                return item[self.__name] + 1

    def __increment_id(self):
        counters = Reader.read_list(self.__db.path + 'counters.json') 
        for item in counters:
            if self__name in item:
                counters[counters.index(item)] =\
                        {self__name: item[self__name] + 1}
                Writer.write(self__db.path + 'counters.json',
                             data=counters, mode='w')
