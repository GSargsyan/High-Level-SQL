from project.lib.databases import Databases
from project.lib.tables import Tables
from project.lib.helper import syntax_err, error
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
        func(*args)


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
        allowed_mistakes = 4
        starting_word = 1
        found = None
        for i in range(starting_word, allowed_mistakes):
            if i >= len(self.query):
                break
            target = self.__get_target(self.query[i])
            if target != None:
                self.target = target
                found = True
                break
        if not found:
            syntax_err(' '.join(self.query[
                starting_word: i]))

    def __get_target(self, inp):
        for target in TARGETS:
            if inp == target:
                target = 'database' if target == 'db' else target
                return target
        return None

    def get_create_args(self):
        if self.target == 'table':
            if self.query[3].lower() != 'with':
                syntax_err(self.query[3])
            if self.query[4].lower() != 'meta':
                syntax_err(self.query[4])
            return [self.query[2],
                    ''.join(self.query[5].split())]
        elif self.target == 'database':
            return [self.query[2]]

    def get_select_args(self):
        error('not yet implemented')

    def get_insert_args(self):
        data_index = None
        data = None
        tb_name = None
        for cmd in self.query[1:]:
            if cmd[0] == '{' and cmd[-1] == '}':
                data = cmd
        if data is None:
            error('Please provide data for insertion')

        query_upper = self.__as_upper()
        for arg in ARGS['insert']:
            if arg in query_upper:
                tb_name = self.query[query_upper.index(arg) + 1]

        if tb_name is None:
            error('Table name was not found in insert statement')

        return [tb_name, data]

    def get_use_args(self):
        return [self.query[1]]

    def __as_upper(self):
        return [elem.upper() for elem in self.query] 

    def __as_lower(self):
        return [elem.lower() for elem in self.query] 
