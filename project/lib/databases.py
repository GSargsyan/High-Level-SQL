from configs import DBS_PATH
from project.lib.helper import error, success, touch, mkdir
import os


class Databases:
    @staticmethod
    def create_database(db_name):
        path = DBS_PATH + db_name
        if mkdir(path):
            success('Created database ' + db_name)
        else:
            error('Database ' + db_name + ' already exists')
        touch(path + '/meta.json')


class Database:
    def __init__(self, name):
        self.name = name
        self.path = DBS_PATH + name + '/'

    def has_table(self, tb_name):
        return os.path.exists(self.path + tb_name)

    def get_meta(tb_name):
        return
