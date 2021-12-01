# Example-1.py
import sys
import os
import libvirt
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    connection_name = os.environ.get("QEMU_CONNECTION")
    conn = None
    try:
        conn = libvirt.open(connection_name)
    except libvirt.libvirtError as e:
        print(repr(e), file=sys.stderr)
        exit(1)

    return conn


class QemuConnection:

    def __init__(self):
        self.conn = create_connection()

    def list_node_info(self) -> list:
        node_info = self.conn.getInfo()
        host = self.conn.getHostname()
        info = ['Hostname: ' + host + '\n',
                'Model: ' + str(node_info[0]),
                'Memory size: ' + str(node_info[1]) + 'MB',
                'Number of CPUs: ' + str(node_info[2]),
                'MHz of CPUs: ' + str(node_info[3]),
                'Number of NUMA nodes: ' + str(node_info[4]),
                'Number of CPU sockets: ' + str(node_info[5]),
                'Number of CPU cores per socket: ' + str(node_info[6]),
                'Number of CPU threads per core: ' + str(node_info[7]) + '\n'
                ]
        return info

    def list_active_domain(self) -> dict:
        active_domains = {}
        domain_ids = self.conn.listDomainsID()
        if domain_ids is None:
            print('Failed to get a list of domain IDs', file=sys.stderr)
        if len(domain_ids) == 0:
            print('No active domains found', file=sys.stderr)
        else:
            for domain_id in domain_ids:
                domain_name = self.conn.lookupByID(domain_id).name()
                active_domains[int(domain_id)] = domain_name

            return active_domains

    def shutdown_domain(self, domain_id: int) -> str:
        domain = self.conn.lookupByID(domain_id)
        if domain is None:
            print('Failed to get the domain object', file=sys.stderr)
        else:
            print("Shutting down \"" + str(domain.name()) + "\" domain...")
            domain.shutdown()
            return domain.name()

    def close_connection(self) -> bool:
        print('CLosing connection...')
        return self.conn.close()
