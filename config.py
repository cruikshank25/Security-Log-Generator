config = {
    "logging_level":"INFO",
    "no_events":500,
    "write_time":0.25,
    "log_class":"ids_event",
    "class_fields":"ids_fields",
}

logging_level = config["logging_level"]
no_events = int(config["no_events"])
write_time = float(config["write_time"])
log_class = config["log_class"]
class_fields = config["class_fields"]