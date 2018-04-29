#!/usr/bin/env python

from ncclient import manager
import sys

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

        # print all NETCONF capabilities
        print('***Here are the Remote Devices Capabilities***')
        for capability in m.server_capabilities:
            print(capability.split('?')[0])

if __name__ == '__main__':
    sys.exit(main())
