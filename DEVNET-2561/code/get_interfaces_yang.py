#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom


# the variables below assume the user is leveraging the
# network programmability lab and accessing csr1000v
# use the IP address or hostname of your CSR1000V device
HOST = '127.0.0.1'
# use the NETCONF port for your CSR1000V device
PORT = 2223
# use the user credentials for your CSR1000V device
USER = 'vagrant'
PASS = 'vagrant'
# XML file to open
FILE = 'get_interfaces.xml'


# create a main() method
def get_configured_interfaces(xml_filter):
    """
    Main method that retrieves the interfaces from config via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        with open(xml_filter) as f:
            return(m.get_config('running', f.read()))


def main():
    """
    Simple main method calling our function.
    """
    interfaces = get_configured_interfaces(FILE)
    interfaces = xml.dom.minidom.parseString(interfaces.xml)
    interfaces = interfaces.getElementsByTagName("interfaces")
    print(interfaces[0].toprettyxml())


if __name__ == '__main__':
    sys.exit(main())