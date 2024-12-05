from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

if __name__ == "__main__":
    print("Starting packet sniffer...")
    print("Press Ctrl+C to stop.")
    sniff(prn=packet_callback, count=10)

