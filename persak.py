import click


@click.group()
# @click.option('--verbose', 'v', is_flag=True)
def cli():
    pass


@cli.command()
# @click.option('--string', default='World')
# @click.argument('out', type=click.File('w'), default='-'
#                   required=False)
def off():
    """Turn the pc off or reboot it"""
    pass


@cli.command()
# @click.option('--string', default='World')
def mc():
    """Start and stop Minecraft server"""
    click.echo('Hello World!')


@cli.command()
# @click.option('--string', default='World')
def backup():
    """Backup"""
    click.echo('Hello World!')
