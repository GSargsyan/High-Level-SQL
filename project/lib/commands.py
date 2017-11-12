COMMANDS = {
        'select': ('SELECT', 'VIEW', 'EXHIBIT', 'SHOW', 'GET', 'BRING'),
        'create': ('CREATE', 'INSERT'),
        'delete': ('REMOVE', 'DROP', 'DELETE'),
        'update': ('UPDATE', 'CHANGE', 'ALTER')
        }

NONOBJECTIVE = (
        'select'
        )

TARGETS = (
        'database',
        'db',
        'table'
        'index',
        )

FIELDS = {
        'all': ('ALL', 'EVERY')
        }

FUNCTION_CLASSES = {
        'create_database': 'Databases',
        'create_db': 'Databases',
        'create_table': 'Tables'
        }
