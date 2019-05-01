import click

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
def ask():
    click.echo('Was?')

@click.command()
def answer():
    click.echo('Bitte answort')

cli.add_command(ask)
cli.add_command(answer)

# @click.command()
# def cli():
    # """Example script."""
    # click.echo('Hello World!')

if __name__ == '__main__':
    cli()
