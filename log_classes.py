# IDS event class representing the contents of an IDS security log event
class ids_event:
    def __init__(self, severity, protocol, src_ip, dest_ip, src_port, dest_port, flags, alert_desc):
        self.severity = severity
        self.protocol = protocol
        self.src_ip = src_ip
        self.dest_ip = dest_ip
        self.src_port = src_port
        self.dest_port = dest_port
        self.flags = flags
        self.alert_desc = alert_desc
