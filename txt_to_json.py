#!/usr/bin/python3

import json


ip_asn = {}

with open('IPASN.txt') as f:
  for line in f:
    if "\t" not in line:
        continue
    ip, asn = map(str.strip, line.split("\t"))
    if asn not in ip_asn:
      ip_asn[asn] = []
    ip_asn[ip] = asn
    ip_asn[asn].append(ip)

with open('IPASN.json', "wt") as f:
  json.dump(ip_asn, f)
