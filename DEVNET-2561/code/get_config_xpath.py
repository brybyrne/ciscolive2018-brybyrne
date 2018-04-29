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

# create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        results = m.get_config('running' , filter=('xpath' , "interfaces/interface[name='GigabitEthernet2']"
                                                   ))
        print(xml.dom.minidom.parseString(results.xml).toprettyxml())

if __name__ == '__main__':
    sys.exit(main())