#! /usr/bin/env python3

from sys import exit
import scriptine as s
import time
import yaml

def hello_command(name, repeat=1):
    """Print nice greetings."""
    for i in range(repeat):
        print(f'Hello, {name}!')

def ask_command(question):
    """Ask a question to be answered later."""
    store = load_store()
    new_key = timestamp()
    new_val = {'Q': question}
    store[new_key] = new_val
    try:
        save_store(store)
    except:
        print("Could not save question to store")
    print(f"Added {new_val} to store")

def timestamp():
    return int(time.time()) 

STORE_PATH = '.deutscher-befrager'

def parse_raw_store(raw_txt):
    try:
        return yaml.load(raw_txt)
    except yaml.YAMLError as ymlexcp:
        print(f"Error parcing your {STORE_PATH}")
        print(ymlexcp)

def load_store():
    try:
        store_file = s.path(STORE_PATH)
        return parse_raw_store(store_file.text())
    except FileNotFoundError:
        print(f"You don't have a {STORE_PATH} yet")
        should_create_file = input("Would you like me to create one y/n?")
        if should_create_file == 'y': create_store(store_file)

def save_store(val):
    store_file = s.path(STORE_PATH)
    store_string = yaml.dump(val)
    store_file.write_text(store_string)

def create_store(file):
    try:
        file.touch()
        print(f"Created blank store file {STORE_PATH}.")
    except:
        print("Problem creating store file :'(")
    print("Time to ask some questions!")
    exit(0)

if __name__ == '__main__':
    s.run()
