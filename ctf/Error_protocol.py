import dpkt

# Open the PCAP file in binary read mode
input = open("error_reporting.pcap", "rb")

# Open the output file in binary write mode
output = open("output.jpg", "wb")

# Create a pcap reader
pcap = dpkt.pcap.Reader(input)

# Loop through the packets
for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    if eth.type != dpkt.ethernet.ETH_TYPE_IP:  # 2048 is ETH_TYPE_IP
        continue

    ip = eth.data
    if ip.p == dpkt.ip.IP_PROTO_ICMP:
        icmp = ip.data
        if hasattr(icmp, 'data') and hasattr(icmp.data, 'data') and len(icmp.data.data) > 0:
            try:
                print(icmp.data.data)
                output.write(icmp.data.data)
            except Exception as e:
                print('Error extracting ICMP payload data from this packet:', e)

# Close the files
input.close()
output.close()
