from scapy.all import *
from header import colPr

# Common ports that are generally safe or expected to be open
SAFE_PORTS = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP",
    25: "SMTP",
    53: "DNS",
    110: "POP3",
    143: "IMAP",
    3389: "RDP",
    3306: "MySQL",
    8080: "HTTP-Proxy"
}

class PortScanner:
    def __init__(self, ip):
        self.ip = ip

    def portScan(self, startPort=1, endPort=65535):
        """
        Scans ports on the target IP and categorizes them as safe or suspicious.
        :param startPort: Starting port range.
        :param endPort: Ending port range.
        """
        colPr(col="yellow", text=f"Starting port scan on {self.ip} from {startPort} to {endPort}...")

        for port in range(startPort, endPort + 1):
            # Create a SYN packet for each port
            synPacket = IP(dst=self.ip) / TCP(dport=port, flags="S")
            response = sr1(synPacket, timeout=0.5, verbose=0)

            # Analyze the response
            if response and response.haslayer(TCP) and response[TCP].flags == "SA":
                if port in SAFE_PORTS:
                    colPr(col="green", text=f"Port {port} ({SAFE_PORTS[port]}) is open and common.")
                else:
                    colPr(col="red", text=f"Port {port} is open and uncommon. Investigate!")
            elif response and response.haslayer(ICMP):
                colPr(col="cyan", text=f"Port {port} is filtered by a firewall (ICMP type {response[ICMP].type}).")

        colPr(col="yellow", text="Port scan completed.")

    def scanResults(self):
        """
        Public method to start the port scan.
        """
        self.portScan()
