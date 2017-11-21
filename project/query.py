from project.lib.databases import Databases
from project.lib.tables import Tables
from project.lib.helper import syntax_err
from project.lib.commands import *


class Query:
    def __init__(self, query):
        if type(query) is not str:
            throw('Invalid argument supplied for Query()')
        self.query = query.strip().split()

    def execute(self):
        self.set_type()
        self.set_target()

        args = eval('self.get_' + self.type + '_args()')
        func = FUNCTIONS[self.type][self.target] if self.target != None \
            else FUNCTIONS[self.type]
        func(args)


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
        self.target = None
        if self.type in NONOBJECTIVE:
            return

        input = self.query[1]
        second = input.lower()
        for target in TARGETS:
            if second == target:
                target = 'database' if target == 'db' else target
                self.target = target
                return target
        syntax_err(input)

    def get_create_args(self):
        if self.target == 'table':
            if self.query[2].lower() != 'with':
                syntax_err(self.query[2])
            if self.query[3].lower() != 'meta':
                syntax_err(self.query[3])
            return '{}'.format(''.join(self.query[4].split()))
        elif self.target == 'database':
            return '{}'.format(self.query[2])

    def get_use_args(self):
        return self.query[1]
