## How it works:
1. Capturing Network Traffic 
   - I used the scapy library to sniff live network packets.  
   - The capture_traffic  function collects a specified number of packets (default: 100) and saves them to a .pcap file using wrpcap
   - This allows for later analysis of network traffic patterns.  

2. Extracting Five-Tuple Information
   - I used the dpkt library to read the captured .pcap file and extract key network metadata.  
   - The extracted five-tuple includes:  
     - Source IP  
     - Destination IP  
     - Source Port  
     - Destination Port  
     - Protocol (TCP, UDP, ICMP)  
   - This helps analyze communication patterns between network hosts.  

3. Live Network Monitoring
   - I implemented a real-time network monitoring function using scapy to analyze packets as they arrive.  
   - The script listens on a specified network interface and prints the source and destination IPs along with the protocol used.
     
4. Traffic Simulation and Integration
   - I integrated the traffic capturing and analysis scripts with a main control script.  
   - The main() function ensures that traffic simulation, packet capturing, and live monitoring run in sequence.  
   - Additionally, a random IP generator using the Faker library is included to help simulate network activity.  

## What it does:
- The system starts by simulating network traffic, ensuring there is data to capture and analyze.  
- The capture script then records network packets and stores them in a .pcap file.  
- The five-tuple extraction script processes the captured packets to extract meaningful metadata.  
- The live capture module provides real-time network traffic analysis, which can be used for intrusion detection or performance monitoring.  
