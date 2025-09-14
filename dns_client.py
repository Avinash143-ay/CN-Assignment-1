import socket
from scapy.all import PcapReader, DNS, DNSQR
from datetime import datetime

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9999

def parse_pcap(pcap_file, limit=None):
    """Extract only DNS queries from PCAP file with custom headers"""
    dns_queries = []
    seq = 0
    with PcapReader(pcap_file) as pcap:
        for pkt in pcap:
            if pkt.haslayer(DNS) and pkt[DNS].qr == 0:
                if pkt.haslayer("UDP") and pkt["UDP"].dport == 53:
                    domain = pkt[DNSQR].qname.decode().strip(".")
                elif pkt.haslayer("TCP") and pkt["TCP"].dport == 53:
                    domain = pkt[DNSQR].qname.decode().strip(".")
                else:
                    continue  

                
                pkt_time = datetime.fromtimestamp(float(pkt.time))
                custom_header = pkt_time.strftime("%H%M%S") + f"{seq:02d}"

                seq += 1
                dns_queries.append((custom_header, domain))

                if limit and seq >= limit:
                    break
    return dns_queries



def client(pcap_file):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    queries = parse_pcap(pcap_file)

    results = []
    for header, domain in queries:
        message = f"{header}|{domain}"
        sock.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
        data, _ = sock.recvfrom(4096)
        resp_header, resp_domain, ip = data.decode().split("|")
        print(f"[CLIENT] {resp_domain} -> {ip} (Header={resp_header})")
        results.append((resp_header, resp_domain, ip))

    # Write report
    with open("dns_report.txt", "w") as f:
        f.write("CustomHeader\tDomain\tResolvedIP\n")
        for h, d, ip in results:
            f.write(f"{h}\t{d}\t{ip}\n")

if __name__ == "__main__":
    # ⚠️ Update path with your chosen PCAP file
    pcap_file = r"C:\Users\GUDA AVINASH REDDY\OneDrive - iitgn.ac.in\Desktop\CN ass1\1.pcap"
    client(pcap_file)
