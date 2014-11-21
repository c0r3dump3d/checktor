def checkTor(ip):
        ip_exit_tor_relay=[]
        tor = urllib.urlopen('http://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv')
        for ip_tor in tor.readlines():
                ip_tor = ip_tor.replace("\n","")
                ip_exit_tor_relay.append(ip_tor)
        if ip in ip_exit_tor_relay:
                print " it's a TOR exit node."
        else:
                print " it's NOT a TOR exit node."
