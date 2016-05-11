
#!/usr/bin/python

import urllib
from json import load
from urllib2 import urlopen

ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
tor = urllib.urlopen('https://check.torproject.org/exit-addresses')

for ip_tor in tor.readlines():
       ip_tor = ip_tor.replace("\n","")
       if "ExitAddress" in ip_tor:
           ip_tor = ip_tor.split(" ")[1]
           if ip == ip_tor:
               success = 1
               break
           else:
               success = 0

if success == 1:

        print "[+] Your public Ip: " + ip + "  ==> It's a TOR exit node"

else:

        print "[-] Your public Ip: " + ip + " ==> It's NOT a TOR exit node"
