# CN-Assignment-1-DNS Resolution Using Client-Server Setup

This assignment demonstrates how DNS resolution works using a client-server architecture.

1. Download the packet capture file:
Use the sample file 1.pcap for this assignment.

2. Run the server:
Open the server script server_side.py in VS Code and run it. The server will start listening for client requests.

3.Run the client:
Open a terminal and run the client script using:
     bash
     python dns_client.py
     
The client will send DNS resolution requests to the server.
4.Expected output:
After running both scripts, you should see DNS resolutions like the following (Custom Header, Domain, Resolved IP):

| Custom Header | Domain      | Resolved IP  |
| ------------- | ----------- | ------------ |
| 18041600      |facebook.com   | 192.168.1.6  |
| 18041601      | stackoverflow.com | 192.168.1.7  |
| 18041602      | example.com  | 192.168.1.8  |
| 18041603      | linkedin.com   | 192.168.1.9  |
| 18041604      | apple.com  | 192.168.1.10 |
| 18041605      | google.com  | 192.168.1.6  |
