import json
import ijson

class Writer:
    @staticmethod
    def write(file_path, data, is_json=True):
        with open(file_path, 'a') as f:
            try:
                if is_json:
                    json.dump(data, f)
                else:
                    f.write(data)
            except:
                throw('Failed writing data to file')


class Reader:
    def read(file_path):
        with open(file_path) as f:
            try:
                return json.load(f)
            except:
                throw('Failed parsing file contents')

    @staticmethod
    def read_obj(file_path, obj_name):
        f = open(file_path, 'rb')
        gen_obj = ijson.items(f, obj_name)
        return next(gen_obj)
