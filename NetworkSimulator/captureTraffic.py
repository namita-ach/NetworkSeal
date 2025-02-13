from scapy.all import sniff, wrpcap

def capture_traffic(filename="captured_traffic.pcap", packet_count=100):
    """Captures live network packets and saves them to a .pcap file."""
    print(f"Capturing {packet_count} packets...")
    packets = sniff(count=packet_count)
    wrpcap(filename, packets)
    print(f"Saved traffic to {filename}")

if __name__ == "__main__":
    capture_traffic()
