config = {
    "logging_level":"INFO",
    # General Parameters (applies first)
    "log_type":"ids",
    "event_distribution": "linear",
    # Linear Distribution Parameters (only applies if linear distribution)
    "no_events":2500,
    "write_time":0.5,
    # Wave Distribution Parameters (only applies if wave distribution)
    "frequency": 'n/a',
    "amplitude": 'n/a',
    "sample_rate": 'n/a',
    "duration": 'n/a',
    "stretch": 'n/a'
}


logging_level = config["logging_level"]
log_type = config["log_type"]
event_distribution = config["event_distribution"]
no_events = int(config["no_events"])
write_time = float(config["write_time"])
frequency = config["frequency"]
amplitude = config["amplitude"]
sample_rate = config["sample_rate"]
duration = config["duration"]
stretch = config["stretch"]