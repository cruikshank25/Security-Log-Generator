#TODO: make alerts relevant to protocol and port
#TODO: weights for chance of particular protocol and alerts

import log
import config
import time
import random

PROTOCOL = ['TCP', 'UDP', 'ICMP', 'HTTP', 'HTTPS', 'FTP', 'SMTP', 'DNS', 'DHCP', 'TFTP', 'SNMP']
SOURCE_IP = '192.168.1.'
DESTINATION_IP = '192.168.1.'
FLAGS = ['SYN', 'ACK', 'FIN', 'RST', 'PSH', 'URG']
ALERT_DESCRIPTION = ['Malware', 'Phishing', 'SQL Injection', 'Cross-site scripting (XSS)', 'Denial of service (DoS)', 'Port scanning', 'Malicious traffic']


def make_event():
    event_protocol = random.choice(PROTOCOL)
    event_src_ip = SOURCE_IP + str(random.randint(1, 255))
    event_dest_ip = DESTINATION_IP + str(random.randint(1, 255))
    event_src_port = random.randint(1, 65535)
    
    if event_protocol == 'TCP':
        event_dest_port = random.randint(1, 65535)
    elif event_protocol == 'UDP':
        event_dest_port = random.randint(1, 65535)
    elif event_protocol == 'ICMP':
        event_dest_port = '1'
    elif event_protocol == 'HTTP':
        event_dest_port = '80'
    elif event_protocol == 'HTTPS':
        event_dest_port = '443'
    elif event_protocol == 'FTP':
        event_dest_port = '21'
    elif event_protocol == 'SMTP':
        event_dest_port = '25'
    elif event_protocol == 'DNS':
        event_dest_port = '53'
    elif event_protocol == 'DHCP':
        event_dest_port = '67'
    elif event_protocol == 'TFTP':
        event_dest_port = '69'
    elif event_protocol == 'SNMP':
        event_dest_port = '161'
    else:
        event_dest_port = random.randint(1, 65535)


    event_flags = random.choice(FLAGS)
    event_alert_desc = random.choice(ALERT_DESCRIPTION)
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