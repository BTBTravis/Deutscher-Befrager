#! /usr/bin/env python3

from sys import exit
import scriptine as s
import time
import yaml
import store
import functools as fun
from random import shuffle, uniform


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
    next_key = next_question(local_store)
    answer = input(local_store[next_key]['Q'])
    if 'A' not in local_store[next_key]:
        local_store[next_key]['A'] = list(answer)
    else:
        local_store[next_key]['A'].append(answer)

    try:
        store.save_store(local_store)
    except:
        print("Could not save answer to store")
    print(f"Added {answer} to store")

    

def next_question(questions):
    """Determin the next question"""
    # len(dictview)
    bump_pairs = list(
        map( 
            lambda k: (k, bump_for_answers(questions[k])), 
            questions.keys()
        )
    )        
    bump_pairs = sorted(bump_pairs, key=lambda p: p[0]) # sort by key

    age_acc = 0
    aged_bump_pairs = []
    for pair in bump_pairs:
        key, bump = pair
        new_bump = bump + age_acc
        aged_bump_pairs.append((key, new_bump))
        age_acc = age_acc + 0.1

    bump_pairs = aged_bump_pairs
        
    # print(bump_pairs)

    def min(acc, pair):
        key, bump = pair
        if bump < acc: 
            return bump
        return acc

    def max(acc, pair):
        key, bump = pair
        if bump > acc: 
            return bump
        return acc

    def remap(old_value, old_max, old_min, new_max, new_min):
        old_range = (old_max - old_min)
        new_value = new_min
        if (old_range != 0):
            new_range = (new_max - new_min)  
            new_value = (((old_value - old_min) * new_range) / old_range) + new_min
        return new_value

    bump_min = fun.reduce(min, bump_pairs, 0)
    bump_max = fun.reduce(max, bump_pairs, 0)

    def remap_pair(pair):
        key, bump = pair
        return (key, remap(bump, bump_max, bump_min, 1, 0))

    final_pairs = list(map(remap_pair, bump_pairs))
    shuffle(final_pairs)
    random_bump = uniform(0, 1.0)
    final_key = final_pairs[0][0] 
    for pair in final_pairs:
        key, bump = pair
        if bump < random_bump:
            final_key = key
            break

    # print(f'bump_pairs: {bump_pairs}')
    # print(f'final_pairs: {final_pairs}')
    # print(random_bump)
    # print(final_key)
    return final_key


def bump_for_answers(q):
    if 'A' in q:
        return len(q['A'])
    return 0

if __name__ == '__main__':
    s.run()
