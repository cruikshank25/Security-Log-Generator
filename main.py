#Author: Sean Cruikshank
#TODO: make alerts relevant to protocol/port
#TODO: payload values (user agents, binary data, URLS, file names etc)
#TODO: investigate weighting and bias to produce less high_severity and critical_severity events
#TODO: timeseries randomness? 

import log
import config
import time
import random
import ipaddress


# define possible field values and weights for field values (the liklihood of a particular field value being selected)
PROTOCOL = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP', 'FTP', 'SMTP', 'DNS', 'DHCP', 'TFTP', 'SNMP']
PROTOCOL_WEIGHTS = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

FLAG = ['SYN', 'ACK', 'FIN', 'RST', 'PSH', 'URG']
FLAG_WEIGHTS = [6, 5, 4, 3, 2, 1]

ALERT_DESCRIPTION = ['Port scanning', 'Denial of service (DoS)', 'PING NMAP', 'Malicious traffic',
    'Phishing', 'Malware', 'SQL Injection', 'Cross-site scripting (XSS)', 'Worm Propagation Attempt']
ALERT_WEIGHTS = [9, 8, 7, 6, 5, 4, 3, 2, 1]

SEVERITY = ['low_severity', 'medium_severity', 'high_severity', 'critical_severity']
SEVERITY_WEIGHTS = [4, 3, 2, 1]


# a class of 'Event' representing the contents of a security log event
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

    # create a dictionary of common port values for protocols
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

    # return the port for the protocol, if not protocol from above, generate random port number
    return protocol_to_port.get(protocol, random.randint(1, 65535))


def get_ip():

    # generate a random octet (a number between 0 and 255)
    octet1 = random.randint(0, 255)
    octet2 = random.randint(0, 255)
    octet3 = random.randint(0, 255)
    octet4 = random.randint(0, 255)

    # create a string representation of the ip address
    ip_str = f"{octet1}.{octet2}.{octet3}.{octet4}"

    # create an ip address object using the ip_address function
    ip_addr = ipaddress.ip_address(ip_str)

    return ip_addr


def make_event():
    
    # create the severity, protocol, flag and alert description from the possible choices based on the weights
    event_severity = random.choices(SEVERITY, SEVERITY_WEIGHTS)[0]
    event_protocol = random.choices(PROTOCOL, PROTOCOL_WEIGHTS)[0]
    event_flag = random.choices(FLAG, FLAG_WEIGHTS)[0]
    event_alert_desc = random.choices(ALERT_DESCRIPTION, ALERT_WEIGHTS)[0]

    # use the get_ip method to generate random valid ip addresses for source and destination
    event_src_ip = get_ip()
    event_dest_ip = get_ip()

    # create a random valid source port
    event_src_port = random.randint(1, 65535)
    
    # create the dest port based on the protocol, if not then generate a random valid port
    event_dest_port = event_dest_port = get_port(event_protocol)

    # create the event using the 'Event' class and return the 'Event' object
    event = Event(event_severity, event_protocol, event_src_ip, event_dest_ip, event_src_port, event_dest_port, event_flag, event_alert_desc)

    return event


def main():
    # define a logger and number of events to be written (taken from config.py)
    logger = log.custom_logger()
    no_events = config.no_events

    # for each event in number of events, create an event and sleep for X time where X is 'write_time' from config.py
    for i in range(no_events):
        event = make_event()
        logger.info(f"{event.severity} - {event.protocol} - {event.src_ip}:{event.src_port} --> {event.dest_ip}:{event.dest_port} - {event.flags} - {event.alert_desc}")
        time.sleep(config.write_time)


if __name__ == '__main__':
    main()