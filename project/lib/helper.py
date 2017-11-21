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

def warning(msg):
    print(colored(msg, 'yellow'))

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False
