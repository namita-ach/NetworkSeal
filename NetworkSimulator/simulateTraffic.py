from scapy.all import send, IP, TCP, UDP, ICMP
from utils import get_random_ip
import random
import time

common_ports = {
    "HTTP": 80, "HTTPS": 443, "DNS": 53, "FTP": 21, "SSH": 22, "SMTP": 25
}

def generate_traffic():
    """Simulates network traffic with random IPs and protocols."""
    while True:
        src_ip = get_random_ip()
        dst_ip = get_random_ip()
        if src_ip == dst_ip:
            continue
        
        protocol = random.choice(["TCP", "UDP", "ICMP"])
        
        if protocol == "TCP":
            pkt = IP(src=src_ip, dst=dst_ip) / TCP(sport=random.randint(1024, 65535), dport=random.choice(list(common_ports.values())))
        elif protocol == "UDP":
            pkt = IP(src=src_ip, dst=dst_ip) / UDP(sport=random.randint(1024, 65535), dport=random.choice(list(common_ports.values())))
        else:
            pkt = IP(src=src_ip, dst=dst_ip) / ICMP()
        
        send(pkt, verbose=False)
        print(f"Sent {protocol} packet: {src_ip} -> {dst_ip}")
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    generate_traffic()
S