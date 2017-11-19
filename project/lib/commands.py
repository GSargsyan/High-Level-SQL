COMMANDS = {
        'select': ('SELECT', 'VIEW', 'SHOW', 'GET', 'BRING', 'DISPLAY', ),
        'create': ('CREATE', 'INSERT', 'MAKE', 'BUILD', 'INITIATE'),
        'delete': ('REMOVE', 'DROP', 'DELETE', 'ELIMINATE', 'CUT'),
        'update': ('UPDATE', 'CHANGE', 'ALTER', 'MODIFY', 'ADJUST', 'ALTERNATE', 'REMAKE')
        }

NONOBJECTIVE = (
        'select',
        )

TARGETS = (
        'database',
        'db',
        'table',
        'index',
        )

FIELDS = {
        'all': ('ALL', 'EVERY', 'SOME', 'THOSE'),
        'one': ('ONE', 'JUST ONE', 'SINGLE', 'THE ONLY'),
        'max': ('MAX', 'MAXIMUM', 'HIGHEST', 'MOST', 'GREATEST'),
        'min': ('MIN', 'MINIMUM', 'LOWEST', 'LEAST'),
        'avg': ('AVG', 'AVERAGE'),
        'sum': ('SUM'),
        }

FUNCTION_CLASSES = {
        'create_database': 'Databases',
        'create_db': 'Databases',
        'create_table': 'Tables'
        }

CONDITION_PRONOUNS = (
        'WHO',
        'WHICH',
        'WHOSE',
        'WITH',
        'THAT'
        )

FIELD_REFERENCES = {
        'general': ('IS', 'ARE', 'HAS', 'HAD', 'HAVE'),
        'name': ('CALLED', 'NAMED', 'IS', 'ARE', 'WAS', 'WERE'),
        'location': ('LOCATED', 'FROM', 'IN', 'ON', 'AT'),
        }
