import os
from termcolor import colored

def throw(msg):
    raise Exception(msg)

def error(msg):
    throw(colored(msg, 'red'))

def syntax_err(msg):
    error("Invalid syntax near '{}'".format(msg))

def success(msg):
    print(colored(msg, 'green'))

def mkdir(path, dir_name):
    if not os.path.exists(path + name):
        os.makedirs(path + name)
        return True
    return False
