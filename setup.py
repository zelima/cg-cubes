from ConfigParser import SafeConfigParser as ConfigParser
import os
from cubes import server


def read_slicer_config(config):
    if not config:
        return ConfigParser()
    elif isinstance(config, basestring):
        try:
            path = config
            config = ConfigParser()
            config.read(path)
        except Exception as e:
            raise Exception("Unable to load configuration: %s" % e)
    return config

def setup_config(config):
    config = read_slicer_config(config)

    # set server configurations: port
    config.set("server", "port", os.environ.get('PORT') or '5000')

    # set store configurations
    config.add_section('store')
    config.set("store", "type", "sql")
    if os.environ.get('CG_URL'):
        config.set("store", "url", os.environ.get('CG_URL'))
    else:
        raise Exception("No Database URL found. Please export CG_URL=postress://etc...")
    return config

config = setup_config('slicer.ini')
application = server.create_server(config)
