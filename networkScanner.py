
import scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    options, arguments = parser.parse_args()
    return options


def scan(ip):                                               #1. who has target ip
    arp_request = scapy.ARP(pdst=ip)                        # use scapy.ls(scapy.ARP) to find all the argument can set for scapy.ARP , print(arp_request.show())--> to see all the packet feild  , summary():implemeted by scapy to print content of packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")        #2.set dest mac to broadcast MAC, to create ethernet object and store in broadcast with dest broadcast feild as ff:...:ff
    arp_request_broadcast = broadcast/arp_request           #in scapy broadcast is append with arp request new packet with combination of both, print(arp_request_broadcast.summary(),arp_request_broadcast.show() )
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]   #will send the packet and return value (couple of two values answered,unanswered) print(answered.summary())
    #as it give 2 values we are telling it to give only element 0 by [0]
    clients_list = []
    for element in answered_list:                            #parse response
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}    #print(element1.show())
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)



