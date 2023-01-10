# Security Log Generator

## Description 

- Generates simulated security log events of similar format to IDS systems like Snort.

- View the 'security_log_sample.log' for example log events that are produced. 

## How To Use

- To run, simply run 'python main.py' in the terminal.

- To change the number of log events to be generated, use the 'no_events' setting in the config.py file.

- To change the time taken to write an event, modify the 'write_time' setting in the config.py file.
The lower the write time, the faster your event's will be generated (default is 0.25 (250 ms)).

- Tested with Python version 3.10.6 (should be compatible with any version above 3.6+).
