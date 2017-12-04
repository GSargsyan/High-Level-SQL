import os
from project.lib.helper import *
from configs import DBS_PATH

class Databases:
    @staticmethod
    def create_database(db_name):
        path = DBS_PATH + db_name
        if mkdir(path):
            success('Created database ' + db_name)
        else:
            error('Database ' + db_name + ' already exists')

        open(path + '/meta.json', 'w')


class Database:
    def __init__(self, name):
        self.name = name
        self.path = DBS_PATH + '/' + name + '/'
        self.meta_path = self.path + 'meta.json'

    def has_table(self, tb_name):
        return os.path.exists(self.path + tb_name)
