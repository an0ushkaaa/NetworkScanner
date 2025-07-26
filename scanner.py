import scapy.all as scapy
import socket

COMMON_PORTS = [21, 22, 23, 80, 443, 445, 3389]

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    results = []

    for element in answered_list:
        ip = element[1].psrc
        mac = element[1].hwsrc

        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"

        open_ports = []
        for port in COMMON_PORTS:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(str(port))
            sock.close()

        results.append({
            "ip": ip,
            "mac": mac,
            "hostname": hostname,
            "ports": open_ports
        })

    return results
