from redash.utils import configuration

def callables():
    return len([n for n in dir(configuration) if callable(getattr(configuration, n, None)) and not n.startswith('_')])
