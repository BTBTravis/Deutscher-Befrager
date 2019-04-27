#! /usr/bin/env python3

def hello_command(name, repeat=1):
    """Print nice greetings."""
    for i in range(repeat):
        print(f'Hello, {name}!')

if __name__ == '__main__':
    import scriptine
    scriptine.run()
