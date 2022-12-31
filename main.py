#Author: Sean Cruikshank
#TODO: make alerts relevant to protocol/port
#TODO: add comments
#TODO: more realistic ip addresses from ipaddress lib
#TODO: payload values (user agents, binary data, URLS, file names etc)

import log
import config
import time
import random

SOURCE_IP = '192.168.1.'
DESTINATION_IP = '192.168.1.'

PROTOCOL = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP', 'FTP', 'SMTP', 'DNS', 'DHCP', 'TFTP', 'SNMP']
PROTOCOL_WEIGHTS = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

FLAG = ['SYN', 'ACK', 'FIN', 'RST', 'PSH', 'URG']

ALERT_DESCRIPTION = ['Port scanning', 'Denial of service (DoS)', 'Malicious traffic',  'Phishing', 'Malware', 'SQL Injection', 'Cross-site scripting (XSS)']
ALERT_WEIGHTS = [7, 6, 5, 4, 3, 2, 1]

SEVERITY = ['low_severity', 'medium_severity', 'high_severity', 'critical_severity']
SEVERITY_WEIGHTS = [4, 3, 2, 1]

class Event:
    def __init__(self, severity, protocol, src_ip, dest_ip, src_port, dest_port, flags, alert_desc):
        self.severity = severity
        self.protocol = protocol
        self.src_ip = src_ip
        self.dest_ip = dest_ip
        self.src_port = src_port
        self.dest_port = dest_port
        self.flags = flags
        self.alert_desc = alert_desc


def get_port(protocol):
    protocol_to_port = {
        'TCP': random.randint(1, 65535),
        'UDP': random.randint(1, 65535),
        'ICMP': 1,
        'HTTP': 80,
        'HTTPS': 443,
        'FTP': 21,
        'SMTP': 25,
        'DNS': 53,
        'DHCP': 67,
        'TFTP': 69,
        'SNMP': 161
    }

    return protocol_to_port.get(protocol, random.randint(1, 65535))


def make_event():
    event_severity = random.choices(SEVERITY, SEVERITY_WEIGHTS)[0]
    event_protocol = random.choices(PROTOCOL, PROTOCOL_WEIGHTS)[0]
    event_src_ip = SOURCE_IP + str(random.randint(1, 255))
    event_dest_ip = DESTINATION_IP + str(random.randint(1, 255))
    event_src_port = random.randint(1, 65535)
    event_dest_port = event_dest_port = get_port(event_protocol)
    event_flag = random.choice(FLAG)
    event_alert_desc = random.choices(ALERT_DESCRIPTION, ALERT_WEIGHTS)[0]
    event = Event(event_severity, event_protocol, event_src_ip, event_dest_ip, event_src_port, event_dest_port, event_flag, event_alert_desc)

    return event


def main():
    # define a logger and number of events to be written (taken from config.py)
    logger = log.custom_logger()
    no_events = config.no_events

    # for each event in number of events, create an event and sleep for X time where X is 'write_time' from config.py
    for i in range(no_events):
        event = make_event()
        logger.info(f"{event.severity} - {event.protocol} - {event.src_ip} - {event.dest_ip} - {event.src_port} - {event.dest_port} - {event.flags} - {event.alert_desc}")
        time.sleep(config.write_time)


if __name__ == '__main__':
    main()