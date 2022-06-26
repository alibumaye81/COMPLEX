import re
from pprint import pprint

arp_entry = '''
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
'''

for arp_list  in [arp_entry.strip()]:
        new_arp = arp_list.splitlines()
#print(new_arp)

#print(new_arp)
new_dict = []
for net_display in new_arp:
        if 'Protocol' in net_display:
                continue
        #print(net_display)

        _, ip_addy, _, mac_addy, _, intf = net_display.split()
        arp_new = {'ip_addy': ip_addy,'mac_addy': mac_addy,'intf':intf
}
        new_dict.append(arp_new)
pprint(new_dict)

