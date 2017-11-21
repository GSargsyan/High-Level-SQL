from project.lib.databases import *

class Tables:
    @staticmethod
    def create_table(meta_str):
        try:
            meta = json.loads(meta_str)
            print(meta_str)
        except:
            error('Invalid JSON provided')

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

    @staticmethod
    def set_database(db_name):
        if hasattr(Tables, 'db') and Tables.db.name == db_name:
            warning('Already on ' + db_name)
            return

        Tables.db = Database(db_name)
        success('Switched to database ' + db_name)
        

class Table:
    def __init__(self):
        pass
