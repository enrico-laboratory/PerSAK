import click
from scripts.qemu_connection import QemuConnection

click.echo('Creating connection\n')
conn = QemuConnection()

click.echo('Print Node info:')
node_info = conn.list_node_info()
for info in node_info:
    print(info)

click.echo('Print list active domains')
active_domains = conn.list_active_domain()
for k, v in active_domains.items():
    click.echo(str(k) + " " + v)

click.echo('Shutting down domains...')
domain = conn.shutdown_domain(1)
click.echo('Domain ' + domain + ' is down!')

closed = conn.close_connection()
if closed == 0:
    click.echo('Connection closed successfully!')
