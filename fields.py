# IDS log fields class for possible fields and possible values for fields
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



# access log fields class for possible fields and possible values for fields
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


# endpoint log fields class for possible fields and possible values for fields
class endpoint_fields:
    def __init__(self):
        self.EVENT_TYPE = ['Malware Detected', 'Scan Started', 'Scan Completed', 'Update Applied', 'Exception',
                            'Real-time Protection Disabled', 'Real-time Protection Enabled', ]
        self.EVENT_TYPE_WEIGHTS = [4, 8, 8, 8, 1,
                                    1, 1]

        self.ACTION = ['Quarantine', 'Restored', 'Deleted', 'Allow', 'Clean', 'Report', 'Block']
        self.ACTION_WEIGHTS = [10, 2, 4, 2, 4, 1, 1]

        # equal chance
        self.THREAT_NAME = ['Virus.Win32.Example', 'Trojan.JS.Example', 'Worm.Win32.Example', 'Adware.Win32.Example',
                            'Ransomware.Win32.Example', 'Backdoor.Win32.Example', 'Rootkit.Win32.Example', 'Spyware.Win32.Example',
                            'PUP.Win32.Example', 'Exploit.Win32.Example']
        #self.THREAT_NAME_WEIGHTS = []

        self.SCAN_TYPE = ['Full Scan', 'Quick Scan', 'Custom Scan', 'On-Demand Scan', 'Real-time Scan', 'Boot-time Scan']
        self.SCAN_TYPE_WEIGHTS = [5, 5, 2, 2, 1, 1]

        self.UPDATE_TYPE = ['Definition Update', 'Threat Database Update', 'Software Update', 'Configuration Update', 'Engine Update']
        self.UPDATE_TYPE_WEIGHTS = [3, 2, 1, 1, 1]

        self.EXCEPTION_REASON = ['Trusted Application', 'Whitelisted', 'Trusted Publisher', 'Administrator Override']
        self.EXCEPTION_REASON_WEIGHTS = [4, 4, 4, 1]

        self.REALTIME_PROTECTION_REASON = ['Scheduled', 'Manual', 'Automatic']
        self.REALTIME_PROTECTION_REASON_WEIGHTS = [3, 1, 2]
        
        self.LEGIT_PROCESSES = ['crsss.exe', 'wininit.exe', 'services.exe', 'lsass.exe',
                                'svchost.exe', 'msiexec', 'taskmgr.exe', 'explorer.exe']

        self.OBVIOUS_MALICIOUS = ['password_stealer.exe', 'keylogger.exe', 'squirmy_wormy.exe', 'ransom.exe',
                                'kaiden_bot.exe', 'adrev4free.scr', 'trjn_hrse.exe', 'SQL_SLAMMER.exe',
                                'CODE_RED.scr', 'gonnacry.exe', 'leepicvirus.exe', 'doom.exe']




ids_fields = ids_fields()
access_fields = access_fields()
endpoint_fields = endpoint_fields()