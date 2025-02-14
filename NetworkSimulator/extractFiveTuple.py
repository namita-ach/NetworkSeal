import dpkt
import socket

def extract_five_tuple(pcap_file): # we've a pcap
    # no get the source IP, destination IP, source port, dest port, and protocol
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for _, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data

            if isinstance(ip, dpkt.ip.IP):
                src_ip = socket.inet_ntoa(ip.src)
                dst_ip = socket.inet_ntoa(ip.dst)
                protocol = ip.p
                
                if isinstance(ip.data, dpkt.tcp.TCP):
                    src_port, dst_port = ip.data.sport, ip.data.dport
                    print(f"TCP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

                elif isinstance(ip.data, dpkt.udp.UDP):
                    src_port, dst_port = ip.data.sport, ip.data.dport
                    print(f"UDP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

                elif isinstance(ip.data, dpkt.icmp.ICMP):
                    print(f"ICMP: {src_ip} -> {dst_ip}")

if __name__ == "__main__":
    extract_five_tuple("captured_traffic.pcap")
