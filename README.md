# Network Diagnostics Commands Guide

This guide covers basic network diagnostic and troubleshooting commands for Windows PowerShell and Command Prompt, based on the provided screenshots.

## 1. `route`
**Command:** `route print` (or `route print 192` to filter)
**How to perform:**
Open your terminal (PowerShell or Command Prompt) and type the command, then press Enter.
**Description:**
Displays the network routing tables. It lists the active IPv4 and IPv6 routes, showing how network traffic is directed through different network interfaces.

## 2. `ipconfig`
**Command:** `ipconfig`
**How to perform:**
Type `ipconfig` in your terminal and press Enter.
**Description:**
Displays the standard TCP/IP network configuration for your system. It quickly shows your IPv4 Address, Subnet Mask, and Default Gateway for the active network adapters (like Wi-Fi or Ethernet).

## 3. `ipconfig /all`
**Command:** `ipconfig /all`
**How to perform:**
Type `ipconfig /all` in your terminal and press Enter.
**Description:**
Provides a comprehensive and detailed view of your network configuration. In addition to basic IP details, it shows physical MAC addresses, DHCP status, DNS server addresses, and IP lease dates.

## 4. `nslookup`
**Command:** `nslookup <domain-name>` (e.g., `nslookup youtube.com`)
**How to perform:**
Type `nslookup` followed by a website domain (like `youtube.com`) in your terminal and press Enter.
**Description:**
Queries the Domain Name System (DNS) to find the IP address mapping for a specific domain name. It tells you which DNS server was used and the IPs associated with the target domain.

## 5. `ping`
**Command:** `ping <domain-or-ip>` (e.g., `ping google.com`)
**How to perform:**
Type `ping` followed by a valid website domain or IP address in your terminal and press Enter.
**Description:**
Tests the network connectivity and reachability of a specific host. It sends test packets and measures the round-trip time, reporting on packet loss and latency. (Note: in the screenshot, it was written as `goolge.com`, but the concept remains the same).

## 6. `netstat`
**Command:** `netstat`
**How to perform:**
Type `netstat` in your terminal and press Enter.
**Description:**
Displays active TCP connections on your machine. It outlines local and remote IP addresses, port numbers, and the current state of each connection (e.g., ESTABLISHED, TIME_WAIT, CLOSE_WAIT).
