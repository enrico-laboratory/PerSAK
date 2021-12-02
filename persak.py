import os

import click
from scripts.qemu_utilities import QemuConnection
from dotenv import load_dotenv

load_dotenv()

@click.group()
# @click.option('--verbose', 'v', is_flag=True)
def cli():
    pass


@cli.command()
@click.option('--list', '-l', 'list_',
              is_flag=True,
              help="List all the active domains")
@click.option('--down-selected', '-s',
              type=str,
              multiple=True,
              help='Shutdown selected domain')
@click.option('--reb', '-r',
              is_flag=True,
              help="Reboot the VM host")
@click.option('--down', '-d',
              is_flag=True,
              help="Shutdown the VM host")
def off(list_, down_selected, reb, down):
    """Turn the VM host off or reboot it,
    also list the active VMs and can shutting down selected one"""

    click.echo("Establishing connection...")
    conn = QemuConnection()

    if list_:
        print('Active domains:')
        for domain in conn.list_active_domain():
            print(domain)
        click.echo("...closing connection.")
        conn.close_connection()

    if down_selected:
        for domain in down_selected:
            conn.shutdown_domain(domain)
            print("Shutting down \"" + domain + "\" domain...")
        click.echo("...closing connection.")
        conn.close_connection()

    if down or reb:
        click.echo("Shutting down all VMs except OPNSense...")
        active_domains = conn.list_active_domain()
        index = active_domains.index(os.environ.get("OPNSENSE_DOMAIN"))
        # removing OPNSense domain from list
        active_domains.pop(index)
        for domain in active_domains:
            print("Shutting down \"" + str(domain) + "\" domain...")
            conn.shutdown_domain(domain)
        if down:
            # TODO System shutdown
            click.echo("Shutdown!!")
        if reb:
            # TODO System reboot
            click.echo("Rebooting!!")


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
