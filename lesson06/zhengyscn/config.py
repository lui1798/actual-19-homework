import configparser


def ReadConfig(filename, section, key):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return 'config ini is empty.', False
    # print(config.sections())

    # sections = config.sections()
    # return config[section]
    # print(config.sections())
    # print(dir(config))
    # print(dir(config[section]))
    # print(config[section][key])

    if key in config[section]:
        return config[section][key], True
    else:
        return '', False

    # return config[section].get(key), True





