#! /usr/bin/env python3

from sys import exit
import scriptine as s
import time
import yaml
import store
import answerer


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

def answer_command():
    """Retrive a question to answer"""
    local_store = store.load_store()
    next_key = answerer.next_question(local_store)
    try:
        answer = input(local_store[next_key]['Q'] + "\n")
    except:
        exit()

    if 'A' not in local_store[next_key]:
        local_store[next_key]['A'] = [answer]
    else:
        local_store[next_key]['A'].append(answer)

    try:
        store.save_store(local_store)
    except:
        print("Could not save answer to store")
    print(f"Added {answer} to store")

    


if __name__ == '__main__':
    s.run()
