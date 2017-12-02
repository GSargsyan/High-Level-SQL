from project.lib.databases import *
from project.lib.io import Writer, Reader
from configs import DBS_PATH
import json

class Tables:
    data_types = ('text', 'number', 'boolean')

    def check_database(function):
        def wrapper(*args, **kwargs):
            if not hasattr(Tables(), 'db'):
                error('No database selected')
            return function(*args, **kwargs)
        return wrapper

    @staticmethod
    @check_database
    def create_table(tb_name, meta_str):
        if os.path.exists(DBS_PATH + tb_name):
            error('Table ' + tb_name + ' already exists')
        try:
            meta = json.loads(meta_str)
        except:
            error('Invalid JSON provided')

        if Tables().is_valid_meta(meta):
            path = DBS_PATH + Tables().db.name + '/meta.json'
            # TODO: if tb exists don't create it
            # Reader().read_obj(path, tb_name)
            # Writer().write(path, {tb_name: meta})
        success('Created table ' + tb_name)


    @staticmethod
    def is_valid_meta(meta):
        from project.lib.commands import REFERENCE_TYPES
        if not isinstance(meta, dict):
            error('Invalid meta provided')

        for colname, data in meta.items():
            if data['type'] == 'mapping':
                if 'points' not in data:
                    error('Invalid meta provided for ' + colname)
                elif not Tables().table_exists(data['points']):
                    error('Table ' + data['points'] + 'doesm\'t exist')
            else:
                if data['type'] not in Tables().data_types:
                    error('Unknown data type: ' + data['type'])
                elif 'reference' not in data:
                    error('Invalid meta provided for ' + colname)
                elif data['reference'] not in REFERENCE_TYPES:
                    error('Unknown reference type: ' + data['reference'])
        return True

    @staticmethod
    def table_exists(tb_name):
        return os.path.exists(DBS_PATH + 'tb_name')

    @staticmethod
    def set_database(db_name):
        if hasattr(Tables, 'db') and Tables.db.name == db_name:
            warning('Already on ' + db_name)
        elif not os.path.exists(DBS_PATH + db_name):
            error('Database ' + db_name + ' doesn\'t exist')
        else:
            Tables.db = Database(db_name)
            success('Switched to database ' + db_name)
        

class Table:
    def __init__(self):
        pass
