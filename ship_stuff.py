#!/usr/bin/env python

def ship_servers(location):
  servers = ['HOST-32L', 'HOST-64L', 'HOST-128L', 'HOST-32H', 'SP-32', 'SP-64', 'SP-128', 'EG-16', 'EG-32', 'EG-64', 'FS-12T']

  return "Shipping {servers} to {location}".format(servers=servers, location=location)



def ship_network_equipment(location):
  network_equipment = ['ASR-9000', 'Nexus 7K', 'Cisco 6K', 'Cisco 3650', 'Arbor', 'Tilera', 'NCS 5K']

  return "Shipping {network_equipment} to {location}".format(network_equipment=network_equipment, location=location)



locations = ['AMS', 'FRA', 'WAR', 'SFO', 'ASH', 'SIN', 'LDN']

for location in locations:
  print ship_servers(location)
  print ship_network_equipment(location)
