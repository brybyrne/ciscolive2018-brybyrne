#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom

# the variables below assume the user is leveraging a
# local CSR1000V running as a vagrant box
# use the IP address or hostname of your CSR1000V device
HOST = '127.0.0.1'
# use the NETCONF port for your IOS-XE device
# by default NETCONF uses port 830 but our vagrant box
# remaps to 2223
PORT = 2223
# use the user credentials for your IOS-XE device
USER = 'vagrant'
PASS = 'vagrant'
FILE = 'get_config_filter.xml'


# create a main() method
def get_configured_interfaces(xml_filter):

    # Main method that retrieves the interfaces from config via NETCONF.

    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        with open(xml_filter) as f:
            return(m.get_config('running', f.read()))

def main():

    # Simple main method calling our function.

    results = get_configured_interfaces(FILE)
    print(xml.dom.minidom.parseString(results.xml).toprettyxml())


if __name__ == '__main__':
    sys.exit(main())
