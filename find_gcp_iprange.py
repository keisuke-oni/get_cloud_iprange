#!/usr/bin/env python

import re
import dns.resolver

gcp_host = '_cloud-netblocks.googleusercontent.com'

# define global variable
includes = []
ip4s = []

def delete_duplicate(input_list):
	deleted_list = list(set(input_list))
	return deleted_list

def resolve(host):
	# print(host)
	answers = dns.resolver.resolve(host, 'TXT')
	record = answers[0].strings[0].decode('utf-8')
	return record

def answer_parse(record):
	#include
	global includes
	purse_includes = re.findall(r'include:(\S+)\s', record)
	includes = includes + purse_includes
	includes = delete_duplicate(includes)
	#ip4
	global ip4s
	purse_ip4s = re.findall(r'ip4:(\S+)\s', record)
	ip4s = ip4s + purse_ip4s
	ip4s = delete_duplicate(ip4s)

def main():
	# initial resolve
	global gcp_host
	record = resolve(gcp_host)
	answer_parse(record)
	
	# find iprange
	global includes
	while(includes != []):
		host = includes.pop()
		record = resolve(host)
		answer_parse(record)
		
	# Show Results
	global ip4s
	ip4s = delete_duplicate(ip4s)
	ip4s.sort()
	with open("gcp_ipranges.csv", 'wt') as f:
		for ip_range in ip4s:
			f.write(ip_range+'\n')

if __name__ == '__main__':
	main()

