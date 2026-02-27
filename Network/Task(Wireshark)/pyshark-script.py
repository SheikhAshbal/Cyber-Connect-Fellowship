import pyshark

def analyze_dns(pcap_file):
    # Open the pcap file and apply DNS filter
    capture = pyshark.FileCapture(pcap_file, display_filter="dns")

    print("DNS Traffic Analysis\n")
    print("-" * 40)

    for packet in capture:
        try:
            # Extract source IP
            src_ip = packet.ip.src

            # Extract queried domain name
            query_name = packet.dns.qry_name

            print(f"Source IP: {src_ip}")
            print(f"Queried Domain: {query_name}")
            print("-" * 40)

        except AttributeError:
            # Skip packets that do not have expected fields
            continue

    capture.close()


if __name__ == "__main__":
    pcap_path = "first.pcap"  # Replace with your pcap file name
    analyze_dns(pcap_path)
