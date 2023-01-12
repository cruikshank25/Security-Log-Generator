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

'''
1. checks and defines number of events to generate based on config.py
2. checks for log type defined in config.py
3. defines logger for log type
4. for each event to generate, request a new event from the event generator
5. sleep for X milliseconds where X is the write_time in config.py
'''
def main():
    no_events = config.no_events

    if config.log_type == 'ids':
        logger = logger_definition.ids_logger()
        for i in range(no_events):
            event = make_ids_event()
            logger.info(f'{event.severity} - {event.protocol} - {event.src_ip}:{event.src_port} --> {event.dest_ip}:{event.dest_port} - {event.flags} - {event.alert_desc}')
            time.sleep(config.write_time)

    elif config.log_type == 'access':
        logger = logger_definition.access_logger()
        for i in range(no_events):
            event = make_access_event()
            logger.info(f'{event.client_ip} - {event.user} \"{event.method} {event.resource} {event.protocol} {event.status} {event.bytes} {event.referrer}\" \"{event.user_agent}\"')
            time.sleep(config.write_time)

    

if __name__ == '__main__':
    main()