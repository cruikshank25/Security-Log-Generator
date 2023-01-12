# IDS log fields class for possible fields and possible values for field
class ids_fields:
    def __init__(self):
         # define possible field values and weights for field values (the liklihood of a particular field value being selected over another)
        self.PROTOCOL = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP', 'FTP', 'SMTP', 'DNS', 'DHCP', 'TFTP', 'SNMP']
        self.PROTOCOL_WEIGHTS = [10, 4, 4, 4, 3, 1, 1, 1, 1, 1, 1]
        
        self.FLAG = ['SYN', 'ACK', 'FIN', 'RST', 'PSH', 'URG']
        self.FLAG_WEIGHTS = [10, 6, 4, 2, 2, 1]
        
        self.ALERT_DESCRIPTION = ['Port scanning', 'Denial of service (DoS)', 'PING NMAP', 'Malicious traffic',
            'Phishing', 'Malware', 'SQL Injection', 'Cross-site scripting (XSS)', 'Worm Propagation Attempt']
        self.ALERT_WEIGHTS = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        
        self.SEVERITY = ['low_severity', 'medium_severity', 'high_severity', 'critical_severity']
        self.SEVERITY_WEIGHTS = [20, 4, 2, 1]

ids_fields = ids_fields()


# access log fields class for possible fields and possible values for field
class access_fields:
    def __init__(self):
        self.METHOD = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
        self.METHOD_WEIGHTS = [20, 6, 4, 2, 1, 1, 1, 1, 1]

        self.PROTOCOL = ['HTTP/1.1', 'HTTPS/1.1', 'HTTPS/2.0']
        self.PROTOCOL_WEIGHTS = [20, 10, 5]

        self.STATUS = ['200', '201', '202', '203', '204', '205', '206',
                        '300', '301', '302', '303', '304', '305', '307',
                        '400', '401', '402', '403', '404', '405', '406',
                        '407', '408', '409', '410', '411', '412', '413',
                        '414', '415', '416', '417',
                        '500', '501', '502', '503', '504', '505']
        self.STATUS_WEIGHTS = [40, 5, 5, 5, 5, 5, 5,
                               10, 2, 2, 2, 2, 2, 2,
                               20, 2, 2, 2, 2, 2, 2,
                               2, 2, 2, 2, 2, 2, 2,
                               2, 2, 2, 2,
                               10, 1, 1, 1, 1, 1]

        self.USER_AGENT = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
                           'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
                           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                           '"Googlebot/2.1 (+http://www.googlebot.com/bot.html)"']
        self.USER_AGENT_WEIGHTS = [5, 5, 5, 1, 1]


access_fields = access_fields()