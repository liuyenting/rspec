import click

@click.group()
@click.pass_context
def main(ctx, path):
    pass

@main.command(help="Delete a sepctrum from the database.")
@click.pass_context
def delete(ctx, path, name=None):
    pass

@main.command(name='import', help="Import a spectrum.")
@click.pass_context
def _import(ctx, path, name=None):
    pass

@main.command(name='list', help="List saved spectrum in the database.")
@click.pass_context
def _list(ctx, path, name=None):
    pass