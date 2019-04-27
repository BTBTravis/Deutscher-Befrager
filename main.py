#! /usr/bin/env python3

from sys import exit
import scriptine as s
import time

def hello_command(name, repeat=1):
    """Print nice greetings."""
    for i in range(repeat):
        print(f'Hello, {name}!')

def ask_command(question):
    """Ask a question to be answered later."""
    load_store()
    # TODO: format question for saving
    # TODO: write question to file
# path.write_text
# int(time.time()) 

STORE_PATH = '.deutscher-befrager'

def load_store():
    try:
        store_file = s.path(STORE_PATH)
        raw_store = store_file.text()
        print(raw_store)
        # TODO: Parse store data
    except FileNotFoundError:
        print(f"You don't have a {STORE_PATH} yet")
        should_create_file = input("Would you like me to create one y/n?")
        if should_create_file == 'y': create_store(store_file)


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
