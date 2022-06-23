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
    tasks = ['add_person', 'add_phone', 'update', 'del_phone', 'del_person', 'find', 'exit', 'clean']
    while True:
        if task not in tasks:
            print('Wrong command! Try again.')
            return user_task(task=input('Input command: ').lower())
        elif task == 'exit':
            return print('Have a nice day!')
        elif task == 'clean':
            print('It will delete all data. Are you sure? Y/N and press Enter:')
            decision = str(input()).upper()
            if decision == 'Y':
                return tabling.clean_before()
            elif decision == 'N':
                return print('Canceled')
            else:
                print('Incorrect command.')
        else:
            if task == 'add_person':
                return tabling.add_customer('John', 'Doe')
            elif task == 'add_phone':
                return tabling.add_phone('John', 'Doe', '123-45-67')
            elif task == 'update':
                return tabling.update('John', 'Doe', 'Jack', 'Slater', 'schwarz@big.com')
            elif task == 'del_phone':
                return tabling.del_phone('Jack', 'Slater', '123-45-67')
            elif task == 'del_person':
                return tabling.del_person('Jack', 'Slater')


tabling = Customer(keys())
tabling.create_db()
user_task()
tabling.shutdown()
