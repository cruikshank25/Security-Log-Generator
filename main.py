#Author: Sean Cruikshank
#TODO: make alerts relevant to protocol/port
#TODO: payload values (user agents, binary data, URLS, file names etc)
#TODO: timeseries randomness? 
#TODO: add optional output filepath
#TODO: configuration into a JSON file?
#TODO: add 'how to extend' section in README
#TODO: add a 'future features' section in README

import time
import logger_definition
import config
from generators.ids_generator import make_event as make_ids_event
from generators.access_generator import make_event as make_access_event


def main():
    # define number of events to be written (taken from config.py)
    no_events = config.no_events

    # check for log type to write
    if config.log_type == 'ids':
        # define the logger for the log type
        logger = logger_definition.ids_logger()
        # for each event in number of events, create an event and sleep for X time where X is 'write_time' from config.py
        for i in range(no_events):
            event = make_ids_event()
            logger.info(f'{event.severity} - {event.protocol} - {event.src_ip}:{event.src_port} --> {event.dest_ip}:{event.dest_port} - {event.flags} - {event.alert_desc}')
            time.sleep(config.write_time)

    elif config.log_type == 'access':
        logger = logger_definition.access_logger()
        for i in range(no_events):
            event = make_access_event()
            logger.info(f'{event.client_ip} {event.method} {event.resource} {event.protocol} {event.status} {event.bytes} {event.referrer} {event.user_agent}')
            time.sleep(config.write_time)

    

if __name__ == '__main__':
    main()