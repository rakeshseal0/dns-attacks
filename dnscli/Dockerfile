FROM ubuntu:latest

# Update package lists, install dnsutils (which includes nslookup)
RUN apt-get update && \
    apt-get install -y dnsutils netcat python3 python3-pip tcpdump
RUN pip3 install scapy
RUN mkdir /scripts
# Keep the container running
CMD tail -f /dev/null

