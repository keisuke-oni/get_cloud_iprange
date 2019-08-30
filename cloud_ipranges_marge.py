#!/usr/bin/env python

def readCsv(vender, filepath):
	contents = ""
	with open(filepath, 'r') as f:
		for s_line in f:
			#print(s_line)
			content = s_line.rstrip('\n') + ',' + vender + '\n'
			contents += content
	return contents


def main():
	venders = {
		'aws': 'aws_ipranges.csv',
		'azure': 'azure_ipranges.csv',
		'gcp': 'gcp_ipranges.csv',
	};

	with open("cloud_ipranges.csv", 'wt') as f:
		f.write('ip_range,vender'+'\n')
		for k, v in venders.items():
			f.write(readCsv(k, v))

if __name__ == '__main__':
	main()