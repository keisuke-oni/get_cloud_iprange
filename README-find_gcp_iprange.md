# find_gcp_iprange.py
## Introduction
Google Cloud Platform (GCP) 's IP address ranges are not provided as Official.<br />
Inorder to getting it, we need to resolv dns SPF record described by TXT record of '_cloud-netblocks.googleusercontent.com'.<br />
And, it is necessary to manually resolve DNS recursively to the results [1].


By running this program, We can get GCP IP Address Range automatically.

## How to
### Environment
#### Language
- python3
#### Require Plugins
- re
- dnspython

### Command
```sh
$ python3 find_gcp_ipgrange.py
```

## Result
```
104.154.0.0/15
104.196.0.0/14
107.167.160.0/19
107.178.192.0/18
108.170.192.0/20
108.170.208.0/21
108.170.216.0/22
108.170.220.0/23
108.170.222.0/24
108.59.80.0/20
130.211.128.0/17
130.211.16.0/20
130.211.32.0/19
130.211.4.0/22
130.211.64.0/18
130.211.8.0/21
146.148.16.0/20
146.148.2.0/23
146.148.32.0/19
146.148.4.0/22
146.148.64.0/18
146.148.8.0/21
162.216.148.0/22
162.222.176.0/21
173.255.112.0/20
192.158.28.0/22
199.192.112.0/22
199.223.232.0/22
199.223.236.0/23
208.68.108.0/23
23.236.48.0/20
23.251.128.0/19
34.100.0.0/16
34.102.0.0/15
34.104.0.0/22
34.64.0.0/11
34.96.0.0/14
35.184.0.0/14
35.188.0.0/15
35.190.0.0/17
35.190.128.0/18
35.190.192.0/19
35.190.224.0/20
35.190.240.0/22
35.190.242.0/23
35.192.0.0/14
35.196.0.0/15
35.198.0.0/16
35.199.0.0/17
35.199.128.0/18
35.200.0.0/14
35.203.232.0/21
35.204.0.0/14
35.206.0.0/15
35.208.0.0/13
35.216.0.0/15
35.220.0.0/14
35.224.0.0/13
35.232.0.0/15
35.234.0.0/16
35.235.0.0/17
35.235.192.0/20
35.235.216.0/21
35.235.224.0/20
35.236.0.0/14
35.240.0.0/15
35.242.0.0/15
35.244.0.0/14
8.34.208.0/20
8.35.192.0/21
8.35.200.0/23
```
## Reference
1. https://cloud.google.com/appengine/kb/#static-ip<br />
1. https://qiita.com/fiemon/items/139fb7117bcd227d1829
