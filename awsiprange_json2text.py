#!/usr/bin/env python

import requests
import json

def delete_duplicate(input_list):
	deleted_list = list(set(input_list))
	return deleted_list

def main():
	json_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
	json_data = requests.get(json_url).text
	json_dict = json.loads(json_data)
	
	dict_len = len(json_dict['prefixes'])

	ip_ranges = []
	for i in range(dict_len):
		ip_ranges.append(json_dict['prefixes'][i]['ip_prefix'])
	
	ip_ranges = delete_duplicate(ip_ranges)
	ip_ranges.sort()
	with open("aws_ipranges.csv", 'wt') as f:
		for ip_range in ip_ranges:
			f.write(ip_range+'\n')

if __name__ == '__main__':
	main()