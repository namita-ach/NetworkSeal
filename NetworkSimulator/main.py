from simulateTraffic import generate_traffic
from captureTraffic import capture_packets
from extractFiveTuple import extract_five_tuple
from liveCapture import monitor_live_traffic

def main():
    print("Simulating network traffic...")
    generate_traffic()

    print("Capturing network packets...")
    capture_packets()

    print("Extracting 5-tuple information...")
    extract_five_tuple()

    print("Monitoring live network traffic...")
    monitor_live_traffic()

    print("Network simulation complete")

if __name__ == "__main__":
    main()
