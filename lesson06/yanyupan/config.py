import configparser
from utils.print_msg import *


def ReadConfig(filename, section):
    config = configparser.ConfigParser()
    config.read(filename)
    options_dict = {}
    try:
        options = config.options(section)
    except Exception as e:
        WarnMsg(e)
        return
    for option in options:
        options_dict.setdefault(option, config.get(section, option))

    return options_dict, True
