from project.lib.databases import Databases
from project.lib.tables import Tables

COMMANDS = {
        'select': ('SELECT', 'VIEW', 'SHOW', 'GET', 'BRING', 'DISPLAY', ),
        'create': ('CREATE', 'MAKE', 'BUILD', 'INITIATE'),
        'delete': ('REMOVE', 'DROP', 'DELETE', 'ELIMINATE', 'CUT'),
        'update': ('UPDATE', 'CHANGE', 'ALTER', 'MODIFY', 'ADJUST', 'ALTERNATE', 'REMAKE'),
        'insert': ('INSERT', 'ADD'),
        'use': ('USE')
        }

ARGS = {
        'insert': ('INTO', 'TO'),
        'delete': ('FROM')
        }

NONOBJECTIVE = (
        'select',
        'use',
        'insert',
        )

FUNCTIONS = {
        'create': {
                'database': Databases().create_database,
                'table': Tables().create_table
            },
        'use': Tables().set_database,
        'insert': Tables().insert_data
        }

TARGETS = (
        'database',
        'db',
        'table',
        'index',
        )

DATA_TYPES = (
        'text',
        'number',
        'bool'
        )

FIELDS = {
        'all': ('ALL', 'EVERY', 'SOME', 'THOSE'),
        'one': ('ONE', 'JUST ONE', 'SINGLE', 'THE ONLY'),
        'max': ('MAX', 'MAXIMUM', 'HIGHEST', 'MOST', 'GREATEST'),
        'min': ('MIN', 'MINIMUM', 'LOWEST', 'LEAST'),
        'avg': ('AVG', 'AVERAGE'),
        'sum': ('SUM'),
        }

CONDITION_PRONOUNS = (
        'WHO',
        'WHICH',
        'WHOSE',
        'WITH',
        'THAT'
        )

REFERENCE_TYPES = {
        'general': ('IS', 'ARE', 'HAS', 'HAD', 'HAVE', 'BEEN'),
        'name': ('CALLED', 'NAMED', 'IS', 'ARE', 'WAS', 'WERE'),
        'location': ('LOCATED', 'FROM', 'IN', 'ON', 'AT'),
        'age': ('YEAR OLD', 'IS', 'ARE')
        }
