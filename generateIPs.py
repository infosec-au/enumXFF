#!/usr/bin/env python3
import argparse
import iptools

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--range",
					help="IP range i.e. 0.0.0.0-255.255.255.255", required=True)
parser.add_argument("-o", "--output",
					help="If an IP address returns a higher content length, save IP address to file", 
						required=True)
args = parser.parse_args()

def generate_ips(ip_range):
	ip_start = ip_range.split("-")[0]
	ip_end = ip_range.split("-")[1]
	r = iptools.IpRange(ip_start, ip_end)
	return r

ip_addresses = generate_ips(args.range)
save_file = open(args.output, "a")

for ip in ip_addresses:
	ip_list = ("{0}, ".format(ip) * 50)[:-2]
	save_file.write(ip_list + "\n")