import socket

# IP Pool
IP_POOL = [
    "192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5",
    "192.168.1.6", "192.168.1.7", "192.168.1.8", "192.168.1.9", "192.168.1.10",
    "192.168.1.11", "192.168.1.12", "192.168.1.13", "192.168.1.14", "192.168.1.15"
]

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9999

def resolve_ip(custom_header):
    """Resolve IP based on timestamp and ID"""
    hour = int(custom_header[:2])
    seq_id = int(custom_header[-2:])

    # Determine time slot
    if 4 <= hour <= 11:  # Morning
        pool_start = 0
    elif 12 <= hour <= 19:  # Afternoon
        pool_start = 5
    else:  # Night
        pool_start = 10

    ip_index = pool_start + (seq_id % 5)
    return IP_POOL[ip_index]

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_HOST, SERVER_PORT))
    print(f"[SERVER] Listening on {SERVER_HOST}:{SERVER_PORT}...")

    while True:
        data, addr = sock.recvfrom(4096)
        message = data.decode()
        try:
            custom_header, domain = message.split("|")
            resolved_ip = resolve_ip(custom_header)

            response = f"{custom_header}|{domain}|{resolved_ip}"
            sock.sendto(response.encode(), addr)

            print(f"[SERVER] {domain} -> {resolved_ip} (Header={custom_header})")
        except Exception as e:
            print("[SERVER] Error:", e)

if __name__ == "__main__":
    server()
