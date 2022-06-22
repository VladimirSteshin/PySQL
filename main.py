import configparser
from engine import Customer


def keys():
    key_storage = {}
    config = configparser.ConfigParser()
    config.read("settings.ini")
    key_storage["db_name"] = config["Admin"]["db_name"]
    key_storage["login"] = config["Admin"]["user"]
    key_storage["password"] = config["Admin"]["password"]
    return key_storage


def user_task(task=input('Input command: ').lower()):
    tasks = ['add_person', 'add_phone', 'data_update', 'del_phone', 'del_person', 'find_person', 'exit']
    while True:
        if task not in tasks:
            print('Wrong command! Try again.')
            return user_task(task=input('Input command: ').lower())
        elif task == 'exit':
            return print('Have a nice day!')
        else:
            if task == 'add_person':
                return tabling.add_customer(str(input('Input name: ')), str(input('Input last_name: ')))
            elif task == 'add_phone':
                return tabling.add_phone(str(input('Input name: ')), str(input('Input last_name: ')),
                                         str(input('Input your telephone number: ')))
            elif task == 'update':
                return tabling.update(str(input('Input name: ')), str(input('Input last_name: ')),
                                      str(input('Input e-mail: ')))


tabling = Customer(keys())
tabling.create_db()
user_task()
tabling.shutdown()
