import json

class Writer:
    def write(data):
        

class Reader:
    def read(file_path):
        with open(file_path) as f:
            try:
                return json.load(f)
            except:
                throw('Failed parsing file contents')
