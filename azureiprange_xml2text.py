#!/usr/bin/env python

import requests
import xml.etree.ElementTree as et

def delete_duplicate(input_list):
	deleted_list = list(set(input_list))
	return deleted_list

def main():
	# Maybe this date will be updated in the future.  Please confirm.
	# https://www.microsoft.com/en-us/download/details.aspx?id=41653
	#
	xml_date = '20190715'
	#

	xml_url = 'https://download.microsoft.com/download/0/1/8/018E208D-54F8-44CD-AA26-CD7BC9524A8C/PublicIPs_' + xml_date + '.xml'
	xml_data = requests.get(xml_url).text
	xml_obj = et.fromstring(xml_data)
	ip_ranges_xml = xml_obj.findall(".//IpRange")

	ip_ranges = []
	for ip_range_xml in ip_ranges_xml:
		ip_ranges.append(ip_range_xml.attrib['Subnet'])

	ip_ranges = delete_duplicate(ip_ranges)
	ip_ranges.sort()
	with open("azure_ipranges.csv", 'wt') as f:
		for ip_range in ip_ranges:
			f.write(ip_range+'\n')
	
if __name__ == '__main__':
	main()