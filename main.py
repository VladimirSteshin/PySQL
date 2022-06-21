import psycopg2
import configparser


def keys():
    key_storage = {}
    config = configparser.ConfigParser()
    config.read("settings.ini")
    key_storage["db_name"] = config["Admin"]["db_name"]
    key_storage["login"] = config["Admin"]["user"]
    key_storage["password"] = config["Admin"]["password"]
    return key_storage


with psycopg2.connect(database=keys()['db_name'], user=keys()['login'], password=keys()['password']) as conn:
    pass
