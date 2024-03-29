#Author: Sean Cruikshank
#TODO: make IDS alerts relevant to protocol/port
#TODO: payload values (user agents, binary data, URLS, file names etc) for IDS events
#TODO: add optional output filepath
#TODO: update README into simple / advanced sections
#TODO: add a custom log generator (for user specified log format)
#TODO: add windows event log event type
#TODO: add linux log event type
#TODO: add perimiter log event type
#TODO: ability to customise weightings
#TODO: add threat actor group fields to logs
#TODO: A seperate README file for log format explanations
#TODO: A seperate README file for wave distribution configurations
#TODO: debug log
#TODO: stdout information
#TODO: create an API version of project (so you can call synthetic events via an api)

import time
import logger
import yaml
import numpy as np
from generators.ids_generator import make_event as make_ids_event
from generators.access_generator import make_event as make_access_event
from generators.endpoint_generator import make_event as make_endpoint_event
import sine_wave_generator as swg


'''
1. checks and defines number of events to generate based on config.yaml (not used if 'event_distribution'='wave')
2. checks for log type defined in config.yaml
3. defines logger for log type
4. checks if event_distribution is 'linear' or 'wave'
5. if linear, for each event to generate, request a new event from the event generator
6. sleep for X milliseconds where X is the write_time in config.yaml
7. if wave, create sine waveform based on the amplitude, frequency, sample_rate and duration values
8. use waveform to generate Y events per T time slice
'''

def main():

    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    logging_level = config['config']['logging_level']
    print(f'logging_level: {logging_level}')

    log_type = config['config']['log_type']
    print(f'log type: {log_type}')

    event_distribution = config['config']['event_distribution']
    print(f'event distribution: {event_distribution}')
   
    if event_distribution == 'linear':

        no_events = config['config']['no_events']
        print(f'no. of events: {no_events}')

        write_time = config['config']['write_time']
        print(f'write time: {write_time}')
    
    elif event_distribution == 'wave':

        frequency = config['config']['frequency']
        print(f'frequency: {frequency}')

        amplitude = config['config']['amplitude']
        print(f'amplitude: {amplitude}')

        sample_rate = config['config']['sample_rate']
        print(f'sample_rate: {sample_rate}')

        duration = config['config']['duration']
        print(f'duration:  {duration}')

        stretch = config['config']['stretch']
        print(f'stretch: {stretch}')



    if log_type == 'ids':
        ids_logger = logger.ids_logger(logging_level)

        if event_distribution == 'linear':
            for i in range(no_events):
                event = make_ids_event()
                ids_logger.info(f'{event.severity} - {event.protocol} - {event.src_ip}:{event.src_port} --> {event.dest_ip}:{event.dest_port} - {event.flags} - {event.alert_desc}')
                time.sleep(write_time)

        elif event_distribution == 'wave':
            t, y = swg.sine_wave(frequency, amplitude, sample_rate, duration)
            t = np.diff(t)
            t = t[0]*stretch
            for amp in np.rint(y).astype(int):
                time.sleep(t)
                for val in range(amp):
                    event = make_ids_event()
                    ids_logger.info(f'{event.severity} - {event.protocol} - {event.src_ip}:{event.src_port} --> {event.dest_ip}:{event.dest_port} - {event.flags} - {event.alert_desc}')

    elif log_type == 'access':
        access_logger = logger.access_logger(logging_level)

        if event_distribution == 'linear':
            for i in range(no_events):
                event = make_access_event()
                access_logger.info(f'{event.client_ip} - {event.user} \"{event.method} {event.resource} {event.protocol} {event.status} {event.bytes} {event.referrer}\" \"{event.user_agent}\"')
                time.sleep(write_time)

        elif event_distribution == 'wave':
            t, y = swg.sine_wave(frequency, amplitude, sample_rate, duration)
            t = np.diff(t)
            t = t[0]*stretch
            for amp in np.rint(y).astype(int):
                time.sleep(t)
                for val in range(amp):
                    event = make_access_event()
                    access_logger.info(f'{event.client_ip} - {event.user} \"{event.method} {event.resource} {event.protocol} {event.status} {event.bytes} {event.referrer}\" \"{event.user_agent}\"')

    elif log_type == 'endpoint':
        endpoint_logger = logger.endpoint_logger(logging_level)

        if event_distribution == 'linear':
            no_events = no_events
            for i in range(no_events):
                event = make_endpoint_event()
                if event.event_type == 'Malware Detected':
                    endpoint_logger.info(f'\nEvent Type: {event.event_type}\nFile Name: {event.file_name}\nFile Path: {event.file_path}\nFile Hash: {event.file_hash}\nThreat Name: {event.threat_name}\nAction Taken: {event.action_taken}\nUser: {event.user}\nComputer: {event.computer}' )
                    time.sleep(write_time)
                elif event.event_type == 'Scan Started':
                    endpoint_logger.info(f'\nEvent Type: {event.event_type}\nScan Type: {event.scan_type}\nUser: {event.user}\nComputer: {event.computer}')
                    time.sleep(write_time)
                elif event.event_type == 'Scan Completed':
                    endpoint_logger.info(f'\nEvent Type: {event.event_type}\nScan Type: {event.scan_type}\nMalware Found: {event.malware_found}\nUser: {event.user}\nComputer: {event.computer}')
                    time.sleep(write_time)
                elif event.event_type == 'Update Applied':
                    endpoint_logger.info(f'\nEvent Type: {event.event_type}\nUpdate Type: {event.update_type}\nUpdate Version: {event.update_version}\nUser: {event.user}\nComputer: {event.computer}')
                    time.sleep(write_time)
                elif event.event_type == 'Exception':
                    endpoint_logger.info(f'\nEvent Type: {event.event_type}\nFile/Process: {event.process}\nReason: {event.reason}\nUser: {event.user}\nComputer: {event.computer}')
                    time.sleep(write_time)
                elif event.event_type == 'Real-time Protection Enabled':
                    endpoint_logger.info(f'\nEvent Type: {event.event_type}\nUser: {event.user}\nComputer: {event.computer}')
                    time.sleep(write_time)
                elif event.event_type == 'Real-time Protection Disabled':
                    endpoint_logger.info(f'\nEvent Type: {event.event_type}\nReason: {event.reason}\nUser: {event.user}\nComputer: {event.computer}')
                    time.sleep(write_time)

        elif event_distribution == 'wave':
            t, y = swg.sine_wave(frequency, amplitude, sample_rate, duration)
            t = np.diff(t)
            t = t[0]*stretch
            for amp in np.rint(y).astype(int):
                time.sleep(t)
                for val in range(amp):
                    event = make_endpoint_event()
                    if event.event_type == 'Malware Detected':
                        endpoint_logger.info(f'\nEvent Type: {event.event_type}\nFile Name: {event.file_name}\nFile Path: {event.file_path}\nFile Hash: {event.file_hash}\nThreat Name: {event.threat_name}\nAction Taken: {event.action_taken}\nUser: {event.user}\nComputer: {event.computer}' )
                        time.sleep(write_time)
                    elif event.event_type == 'Scan Started':
                        endpoint_logger.info(f'\nEvent Type: {event.event_type}\nScan Type: {event.scan_type}\nUser: {event.user}\nComputer: {event.computer}')
                        time.sleep(write_time)
                    elif event.event_type == 'Scan Completed':
                        endpoint_logger.info(f'\nEvent Type: {event.event_type}\nScan Type: {event.scan_type}\nMalware Found: {event.malware_found}\nUser: {event.user}\nComputer: {event.computer}')
                        time.sleep(write_time)
                    elif event.event_type == 'Update Applied':
                        endpoint_logger.info(f'\nEvent Type: {event.event_type}\nUpdate Type: {event.update_type}\nUpdate Version: {event.update_version}\nUser: {event.user}\nComputer: {event.computer}')
                        time.sleep(write_time)
                    elif event.event_type == 'Exception':
                        endpoint_logger.info(f'\nEvent Type: {event.event_type}\nFile/Process: {event.process}\nReason: {event.reason}\nUser: {event.user}\nComputer: {event.computer}')
                        time.sleep(write_time)
                    elif event.event_type == 'Real-time Protection Enabled':
                        endpoint_logger.info(f'\nEvent Type: {event.event_type}\nUser: {event.user}\nComputer: {event.computer}')
                        time.sleep(write_time)
                    elif event.event_type == 'Real-time Protection Disabled':
                        endpoint_logger.info(f'\nEvent Type: {event.event_type}\nReason: {event.reason}\nUser: {event.user}\nComputer: {event.computer}')
                        time.sleep(write_time)
        

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)