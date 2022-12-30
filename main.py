#TODO: make alerts relevant to protocol/port
#TODO: weights for chance of particular protocol and alerts

import log
import config
import time
import random

SOURCE_IP = '192.168.1.'
DESTINATION_IP = '192.168.1.'

PROTOCOL = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP', 'FTP', 'SMTP', 'DNS', 'DHCP', 'TFTP', 'SNMP']
PROTOCOL_WEIGHTS = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
PROTOCOL_TO_PORT = {
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

FLAGS = ['SYN', 'ACK', 'FIN', 'RST', 'PSH', 'URG']
ALERT_DESCRIPTION = ['Port scanning', 'Denial of service (DoS)', 'Malicious traffic',  'Phishing', 'Malware', 'SQL Injection', 'Cross-site scripting (XSS)']
ALERT_WEIGHTS = [7, 6, 5, 4, 3, 2, 1]


def make_event():
    event_protocol = random.choices(PROTOCOL, PROTOCOL_WEIGHTS)[0]
    event_src_ip = SOURCE_IP + str(random.randint(1, 255))
    event_dest_ip = DESTINATION_IP + str(random.randint(1, 255))
    event_src_port = random.randint(1, 65535)
    event_dest_port = PROTOCOL_TO_PORT.get(event_protocol, random.randint(1, 65535))
    event_flags = random.choice(FLAGS)
    event_alert_desc = random.choices(ALERT_DESCRIPTION, ALERT_WEIGHTS)[0]
    event = f"{event_protocol} {event_src_ip} {event_dest_ip} {event_src_port} {event_dest_port} {event_flags} {event_alert_desc}"

    return event


def main():
    logger = log.custom_logger()
    no_events = config.no_events

    for i in range(no_events):
        event = make_event()
        logger.info(event)
        time.sleep(0.25)


if __name__ == '__main__':
    main()