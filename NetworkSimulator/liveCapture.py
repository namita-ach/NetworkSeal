from scapy.all import sniff
import argparse

def live_capture(interface="eth0"):
    """Monitors real-time network traffic."""
    print(f"Capturing live traffic on interface: {interface}")
    
    def process_packet(packet):
        if packet.haslayer("IP"):
            print(f"Packet: {packet['IP'].src} -> {packet['IP'].dst}, Protocol: {packet.proto}")

    sniff(iface=interface, prn=process_packet, store=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Live capture network packets")
    parser.add_argument("--iface", type=str, default="eth0", help="Network interface to sniff on")
    args = parser.parse_args()

    live_capture(args.iface)
