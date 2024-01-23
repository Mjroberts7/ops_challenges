# this file is to be testing breakdowns of certain code snippets 
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

# Variables

# Lists


# functions
def ICMPscan(netadd):
    
    try:
        ip_list = ipaddress.IPv4Network(netadd).hosts()
    except ValueError:
        print("not correct address format")
        return
        
    hosts_count = 0
    
    broadcastaddress = "192.168.2.1"
    loopback = "127.0.0.1"
    if network[-1:-2] == 24:
        ip_list = ip_list - loopback
        ip_list = ip_list - broadcastaddress

    for host in ip_list:
        try:
            print(f'Pinging {str(host)}')
            response = sr1(
                IP(dst=str(host))/ICMP(),
                timeout=2,
                verbose=0
            )
            print(response)
        except scapy.all.sr1.error as e1:
            print(f'sr1 Error: {host}: {e1}')
        except Exception as e:
            print(f'Error: ping did not work {e}')


if __name__ == "__main__":
    network = str(input("Network address + CIDR block?\n"))
    ICMPscan(network)