from redash import version_check

def symbol_count():
    return len([n for n in dir(version_check) if not n.startswith('_')])

def has(name):
    return hasattr(version_check, name)
