

# CN-Assignment-1: DNS Resolution Using Client-Server Setup

This assignment demonstrates DNS resolution using a client-server architecture. The goal is to understand how a client queries a server for domain name resolutions and how the server responds with corresponding IP addresses.

---

## Steps to Run

### 1. Download the Packet Capture File

Use the provided sample file **1.pcap**(https://drive.google.com/file/d/1OjLtrl9QglB52Po-gvwyYWjj0f8ewl7S/view?usp=drive_link) for this assignment.

### 2. Run the Server

Open the server script `server_side.py` in VS Code (or any Python environment) and run it.
The server will start listening for incoming client requests.

```bash
python server_side.py
```

### 3. Run the Client

Open a terminal and run the client script:

```bash
python dns_client.py
```

The client sends DNS resolution requests to the server.

---

## Expected Output

After running both scripts, you should see DNS resolutions like the following:

| Custom Header | Domain             | Resolved IP  |
| ------------- | ------------------ | ------------ |
| 18041600      | facebook.com       | 192.168.1.6  |
| 18041601      | stackoverflow\.com | 192.168.1.7  |
| 18041602      | example.com        | 192.168.1.8  |
| 18041603      | linkedin.com       | 192.168.1.9  |
| 18041604      | apple.com          | 192.168.1.10 |
| 18041605      | google.com         | 192.168.1.6  |

---


