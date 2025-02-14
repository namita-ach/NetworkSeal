from scapy.all import sniff, wrpcap

def capture_traffic(filename="captured_traffic.pcap", packet_count=100): # captute the packets into a pcap
    print(f"Capturing {packet_count} packets...")
    packets = sniff(count=packet_count)
    wrpcap(filename, packets)
    print(f"Saved traffic to {filename}")

if __name__ == "__main__":
    capture_traffic()
