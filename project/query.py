from project.lib.db import Databases, Tables
from project.lib.helper import syntax_err
from project.lib.commands import *


class Query:
    def __init__(self, query):
        if type(query) is not str:
            throw('Invalid argument supplied for Query()')
        self.query = query.split()

    def execute(self):
        if self.set_type() not in NONOBJECTIVE:
            self.set_target()
        
        f_name = self.type + '_' + self.target
        if f_name in FUNCTION_CLASSES:
            eval(FUNCTION_CLASSES[f_name] + '().' + f_name + '()')

    def call(func_name, args):
        pass
        
    def set_type(self):
        input = self.query[0]
        first = input.upper() 
        self.type = None
        for command, alts in COMMANDS.items():
            if first in alts:
                self.type = command
                return command
        syntax_err(input)

    def set_target(self):
        input = self.query[1]
        second = input.lower()

        self.target = None
        for target in TARGETS:
            if second == target:
                self.target = target
                return target
        syntax_err(input)
