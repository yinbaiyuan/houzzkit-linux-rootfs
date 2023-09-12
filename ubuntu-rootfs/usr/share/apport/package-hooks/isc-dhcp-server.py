#!/usr/bin/python

'''apport hook for dhcp server

(c) 2010 Canonical Ltd.
Author: Chuck Short <chuck.short@canonical.com>

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.  See http://www.gnu.org/copyleft/gpl.html for
the full text of the license.
'''

from apport.hookutils import *
from os import path
import re

def dhcp_leases(pattern):
    ''' Extract options from '/var/lib/dhcp/dhcpd.leases' which match a regex.
       pattern should be a "re" object. '''
    lines = ""
    if os.path.exists('/var/lib/dhcp/dhcpd.leases'):
        file = '/var/lib/dhcp/dhcpd.leases'
    else:
        return lines

    for line in open(file):
        if pattern.search(line):
            lines += line
    return lines

def add_info(report, ui):
    response = ui.yesno("The contents of your /etc/dhcp/dhclient.conf file may help developers diagnose your bug more quickly, however, it may contain sensitive information. Do you want to include it in your bug report?")

    if response == None: #user cancelled
        raise StopIteration

    elif response == True:
        attach_file_if_exists(report, '/etc/dhcp/dhcpd.conf', 'DHCPServerConf')

        attach_mac_events(report, '/usr/sbin/dhcpd')

        attach_related_packages(report, ['apparmor', 'libapparmor1',
            'libapparmor-perl', 'apparmor-utils', 'auditd', 'libaudit0'])

        attach_file(report, '/etc/apparmor.d/usr.sbin.dhcpd')

        leases = re.compile('option|renew|rebind|expire', re.IGNORECASE)
        report['DhServerLeases'] = dhcp_leases(leases)
