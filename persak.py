import os
import subprocess

import click
from scripts.qemu_utilities import QemuConnection
from scripts.gdrive import sync_dir
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
        active_domains = conn.list_active_domain()
        if not active_domains:
            print("No active domains found...(did you sudo?)")
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
        if active_domains:
            for domain in active_domains:
                print("Shutting down \"" + str(domain) + "\" domain...")
                conn.shutdown_domain(domain)
        else:
            print('Not active domain found..')

        if down:
            click.echo("Shutdown!!")
            subprocess.run(['shutdown', '+1'])
        if reb:
            click.echo("Rebooting!!")
            subprocess.run(['shutdown', '-r', '+1'])


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


@cli.command()
# @click.option('--string', default='World')
def gdrive():
    """Backup"""
    click.echo('Hello World!')
    print(sync_dir("/volumes/share/Conducting", "1ggP6aU93RJT1HzgigtzIA6YLeMWAJtKD"))