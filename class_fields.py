# IDS log possible fields and possible values for field
class ids_fields:
    def __init__(self):
         # define possible field values and weights for field values (the liklihood of a particular field value being selected
        self.PROTOCOL = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP', 'FTP', 'SMTP', 'DNS', 'DHCP', 'TFTP', 'SNMP']
        self.PROTOCOL_WEIGHTS = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.FLAG = ['SYN', 'ACK', 'FIN', 'RST', 'PSH', 'URG']
        self.FLAG_WEIGHTS = [6, 5, 4, 3, 2, 1]
        self.ALERT_DESCRIPTION = ['Port scanning', 'Denial of service (DoS)', 'PING NMAP', 'Malicious traffic',
            'Phishing', 'Malware', 'SQL Injection', 'Cross-site scripting (XSS)', 'Worm Propagation Attempt']
        self.ALERT_WEIGHTS = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.SEVERITY = ['low_severity', 'medium_severity', 'high_severity', 'critical_severity']
        self.SEVERITY_WEIGHTS = [4, 3, 2, 1]


ids_fields = ids_fields()