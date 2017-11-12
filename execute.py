#! /usr/bin/python3
import os
import sys
from configs import *

BASE_DIR = os.path.join(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

def get_execute_query():
    query = Query(input())
    query.execute()

from project.query import Query

if DEBUG_MODE == 1:
    get_execute_query()
else:
    try:
        query = Query(input())
        query.execute()
    except Exception as ex:
        print(str(ex))


