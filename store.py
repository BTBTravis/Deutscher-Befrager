from sys import exit
import yaml
import scriptine as s

STORE_PATH = '.deutscher-befrager'

def _parse_raw_store(raw_txt):
    try:
        return yaml.load(raw_txt)
    except yaml.YAMLError as ymlexcp:
        print(f"Error parcing your {STORE_PATH}")
        print(ymlexcp)

def load_store():
    try:
        store_file = s.path(STORE_PATH)
        return _parse_raw_store(store_file.text())
    except FileNotFoundError:
        print(f"You don't have a {STORE_PATH} yet")
        should_create_file = input("Would you like me to create one y/n?")
        if should_create_file == 'y': _create_store(store_file)

def save_store(val):
    store_file = s.path(STORE_PATH)
    store_string = yaml.dump(val)
    store_file.write_text(store_string)

def _create_store(file):
    try:
        file.touch()
        print(f"Created blank store file {STORE_PATH}.")
    except:
        print("Problem creating store file :'(")
    print("Time to ask some questions!")
    exit(0)
