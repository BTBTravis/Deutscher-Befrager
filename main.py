#! /usr/bin/env python3

from sys import exit
import scriptine as s
import time
import yaml
import store

def hello_command(name, repeat=1):
    """Print nice greetings."""
    for i in range(repeat):
        print(f'Hello, {name}!')

def ask_command(question):
    """Ask a question to be answered later."""
    local_store = store.load_store()
    new_key = timestamp()
    new_val = {'Q': question}
    local_store[new_key] = new_val
    try:
        store.save_store(local_store)
    except:
        print("Could not save question to store")
    print(f"Added {new_val} to store")

def timestamp():
    return int(time.time()) 

if __name__ == '__main__':
    s.run()
