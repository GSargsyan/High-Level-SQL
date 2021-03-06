#! /usr/bin/python3
import os
import sys
from configs import DEBUG_MODE
from project.query import Query

BASE_DIR = os.path.join(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


def get_execute_query():
    inp = input()
    if inp != '':
        query = Query(inp)
        query.execute()


while True:
    if DEBUG_MODE == 1:
        get_execute_query()
    else:
        try:
            get_execute_query()
        except Exception as ex:
            print(str(ex))
