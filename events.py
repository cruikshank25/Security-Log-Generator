'''
IDS CLASSES
'''
# IDS event class representing the contents of a typical IDS security log event
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


'''
ACCESS CLASSES
'''
# Access log event type class representing the contents of a typical access log event
class access_event:
    def __init__(self, client_ip, user, method, resource, protocol, status, bytes, referrer, user_agent):
        self.client_ip = client_ip
        self.user = user
        self.method = method
        self.resource = resource
        self.protocol = protocol
        self.status = status
        self.bytes = bytes
        self.referrer = referrer
        self.user_agent = user_agent


'''
ENDPOINT CLASSES
'''
# Endpoint Anti-Virus log event type class representing the contents of a typical endpoint anti-virus log event
class endpoint_malware_detected_event:
    def __init__(self, event_type, file_name, file_path, file_hash, threat_name, action_taken, user, computer):
        self.event_type = event_type
        self.file_name = file_name
        self.file_path = file_path
        self.file_hash = file_hash
        self.threat_name = threat_name
        self.action_taken = action_taken
        self.user = user
        self.computer = computer


class endpoint_scan_started_event:
    def __init__(self, event_type, scan_type, user, computer):
        self.event_type = event_type
        self.scan_type = scan_type
        self.user = user
        self.computer = computer


class endpoint_scan_completed_event: 
    def __init__(self, event_type, scan_type, malware_found, user, computer):
        self.event_type = event_type
        self.scan_type = scan_type
        self.malware_found = malware_found
        self.user = user
        self.computer = computer


class endpoint_update_applied_event:
    def __init__(self, event_type, update_type, update_version, user, computer):
        self.event_type = event_type
        self.update_type = update_type
        self.update_version = update_version
        self.user = user
        self.computer = computer


class endpoint_exception_event:
    def __init__(self, event_type, process, reason, user, computer):
        self.event_type = event_type
        self.process = process
        self.reason = reason 
        self.user = user
        self.computer = computer 


class endpoint_real_time_protection_enabled_event:
    def __init__(self, event_type, user, computer):
        self.event_type = event_type
        self.user = user
        self.computer = computer


class endpoint_real_time_protection_disabled_event:
    def __init__(self, event_type, reason, user, computer):
        self.event_type = event_type
        self.reason = reason
        self.user = user
        self.computer = computer

