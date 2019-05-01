import click
import interviewer.store as store
import interviewer.util as utils
from sys import exit

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
              # help='The person to greet.')
# def hello(count, name):
    # """Simple program that greets NAME for a total of COUNT times."""
    # for x in range(count):
        # click.echo('Hello %s!' % name)
@click.group()
def cli():
    pass

@click.command()
def answer():
    click.echo('TODO: parse answer')

@click.command()
@click.argument('question')
def ask(question):
    """Ask a question to be answered later."""
    local_store = store.load_store()
    new_key = utils.timestamp()
    new_val = {'Q': question}
    if local_store == None:
        local_store = dict()
    local_store[new_key] = new_val
    try:
        store.save_store(local_store)
    except:
        click.echo("Could not save question to store")
    click.echo(f"Added {new_val} to store")

cli.add_command(ask)
cli.add_command(answer)


if __name__ == '__main__':
    cli()
