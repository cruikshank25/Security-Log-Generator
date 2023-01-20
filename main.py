#Author: Sean Cruikshank
#TODO: make alerts relevant to protocol/port
#TODO: payload values (user agents, binary data, URLS, file names etc)
#TODO: add optional output filepath
#TODO: configuration into a JSON file?
#TODO: add 'how to extend' section in README
#TODO: add a 'future features' section in README
#TODO: application error log
#TODO: improve log formats

import time
import logger
import config
import numpy as np
from generators.ids_generator import make_event as make_ids_event
from generators.access_generator import make_event as make_access_event
import sine_wave_generator as swg


'''
1. checks and defines number of events to generate based on config.py (not used if 'event_distribution'='wave')
2. checks for log type defined in config.py
3. defines logger for log type
4. checks if event_distribution is 'linear' or 'wave'
5. if linear, for each event to generate, request a new event from the event generator
6. sleep for X milliseconds where X is the write_time in config.py
7. if wave, create sine waveform based on the amplitude, frequency, sample_rate and duration values
8. use waveform to generate Y events per T time slice
'''
def main():
    

    if config.log_type == 'ids':
        ids_logger = logger.ids_logger()

        if config.event_distribution == 'linear':
            no_events = config.no_events
            for i in range(no_events):
                event = make_ids_event()
                ids_logger.info(f'{event.severity} - {event.protocol} - {event.src_ip}:{event.src_port} --> {event.dest_ip}:{event.dest_port} - {event.flags} - {event.alert_desc}')
                time.sleep(config.write_time)

        elif config.event_distribution == 'wave':
            t, y = swg.sine_wave(config.frequency, config.amplitude, config.sample_rate, config.duration)
            t = np.diff(t)
            t = t[0]*config.stretch
            for amp in np.rint(y).astype(int):
                time.sleep(t)
                for val in range(amp):
                    event = make_ids_event()
                    ids_logger.info(f'{event.severity} - {event.protocol} - {event.src_ip}:{event.src_port} --> {event.dest_ip}:{event.dest_port} - {event.flags} - {event.alert_desc}')

    elif config.log_type == 'access':
        access_logger = logger.access_logger()

        if config.event_distribution == 'linear':
            no_events = config.no_events
            for i in range(no_events):
                event = make_access_event()
                access_logger.info(f'{event.client_ip} - {event.user} \"{event.method} {event.resource} {event.protocol} {event.status} {event.bytes} {event.referrer}\" \"{event.user_agent}\"')
                time.sleep(config.write_time)

        elif config.event_distribution == 'wave':
            t, y = swg.sine_wave(config.frequency, config.amplitude, config.sample_rate, config.duration)
            t = np.diff(t)
            t = t[0]*config.stretch
            for amp in np.rint(y).astype(int):
                time.sleep(t)
                for val in range(amp):
                    event = make_access_event()
                    access_logger.info(f'{event.client_ip} - {event.user} \"{event.method} {event.resource} {event.protocol} {event.status} {event.bytes} {event.referrer}\" \"{event.user_agent}\"')


if __name__ == '__main__':
    main()