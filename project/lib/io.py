import json
import ijson


class Writer:
    @staticmethod
    def write(file_path, data, mode='a', is_json=True):
        with open(file_path, mode) as f:
            try:
                if is_json:
                    json.dump(data, f)
                else:
                    f.write(data)
            except Exception:
                throw('Failed writing data to file')

    @staticmethod
    def change_val(file_path, obj_name, new_value):
        content = Reader.read(file_path)
        content[obj_name] = new_value
        Writer.write(file_path, content, 'w')

    def add_val(file_path, val):
        content = Reader.read(file_path)
        content.append(val)
        Writer.write(file_path, content, 'w')


class Reader:
    def read(file_path):
        with open(file_path) as f:
            try:
                return json.load(f)
            except Exception:
                throw('Failed parsing file contents')

    @staticmethod
    def read_obj(file_path, obj_name):
        f = open(file_path, 'rb')
        gen_obj = ijson.items(f, obj_name)
        return next(gen_obj)

    @staticmethod
    def read_list(file_path):
        f = open(file_path, 'rb')
        return ijson.items(f, 'items')
