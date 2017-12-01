from project.lib.databases import *
from project.lib.commands import DATA_TYPES
from configs import DBS_PATH
import json

class Tables:
    def check_database(function):
        def wrapper(*args, **kwargs):
            if not hasattr(Tables(), 'db'):
                error('No database selected')
            return function(*args, **kwargs)
        return wrapper

    @staticmethod
    @check_database
    def create_table(meta_str):
        try:
            meta = json.loads(meta_str)
        except:
            error('Invalid JSON provided')

        if Tables().is_valid_meta(meta):
            pass

    @staticmethod
    def is_valid_meta(meta):
        if not isinstance(meta, dict):
            error('Invalid meta provided')

        for colname, data in meta.items():
            if data['type'] == 'mapping':
                if 'points' not in data:
                    error('Invalid meta provided for ' + colname)
                elif not Tables().table_exists(data['points']):
                    error('Table ' + data['points'] + 'doesm\'t exist')
            else:
                if data['type'] not in DATA_TYPES:
                    error('Unknown data type: ' + data['type'])
                elif 'reference' not in data:
                    error('Invalid meta provided for ' + colname)
                elif data['reference'] not in REFERENCE_TYPES:
                    error('Unknown reference type: ' + data['reference'])


            Tables().parse_column(data)

    @staticmethod
    def table_exists(tb_name):
        pass

    @staticmethod
    def set_database(db_name):
        if hasattr(Tables, 'db') and Tables.db.name == db_name:
            warning('Already on ' + db_name)
        elif not os.path.exists(DBS_PATH + db_name):
            print(DBS_PATH + db_name)
            error('Database ' + db_name + ' doesn\'t exist')
        else:
            Tables.db = Database(db_name)
            success('Switched to database ' + db_name)
        

class Table:
    def __init__(self):
        pass
