from fields import endpoint_fields
from events import endpoint_malware_detected_event, endpoint_scan_started_event, endpoint_scan_completed_event, endpoint_update_applied_event, endpoint_exception_event, endpoint_real_time_protection_disabled_event, endpoint_real_time_protection_enabled_event
from faker import Faker
import random
import string
import uuid
import os


# generate a random username
def get_user():
     faker = Faker()
     fname=faker.first_name()
     user = fname.lower()

     return user


# generate a random hash
def get_hash():
     hash = uuid.uuid4()

     return hash


# generate a malicious file name
def get_file():
     types = ['random_chars', 'doppleganger', 'double_extension', 'obvious']
     choice = random.choice(types)

     if choice == 'random_chars':
          file_name = ''
          for i in range(10):
               rand_asclo = random.choice(string.ascii_lowercase) 
               file_name = file_name + rand_asclo
          file = str(file_name) + str('.exe')
     elif choice == 'doppleganger':
          file = random.choice(endpoint_fields.LEGIT_PROCESSES)
     elif choice == 'double_extension':
          faker = Faker()
          f1 = faker.file_name()
          file = str(f1) + str('.exe')
     elif choice == 'obvious':
          file = (random.choice(endpoint_fields.OBVIOUS_MALICIOUS))

     return file


# generate a fake file path
def get_file_path():
     faker = Faker()
     file_path = faker.file_path(depth=3)
     file_path, file_name = os.path.splitext(file_path)
     root_path = "C:\\Users\\"
     user_path = get_user()
     file_path = str(root_path) + str(user_path) + str(file_path) + "/"
     file_path = file_path.replace('/', '\\')

     return file_path


# generate a legitimate windows process
def get_legit_file():
     legit_file = random.choice(endpoint_fields.LEGIT_PROCESSES)

     return legit_file


# get computer name of 8 uppercase ascii characters
def get_computer_name():
     computer_name = ''
     for i in range(8):
          rand_ascup = random.choice(string.ascii_uppercase)
          computer_name = computer_name + rand_ascup

     for i in range(2):
          rand_int = random.randint(1,9)
          str_rand_int = str(rand_int)
          computer_name = computer_name + str_rand_int
     
     return computer_name


# generate a random number with a 10% chance of '0' value
def random_number_likely_zero():
     num = random.randint(0, 100)
     if num <= 90:
          return 0
     return random.randint(1,9)


# generate random version number
def random_version_number():
     num1 = random.randint(0,9)
     num2 = random.randint(0,9)
     num3 = random.randint(0,9)
     random_version_num = f'{num1}.{num2}.{num3}'
     return random_version_num
     


# generate the endpoint antivirus event
def make_event():
     event_type = random.choices(endpoint_fields.EVENT_TYPE, endpoint_fields.EVENT_TYPE_WEIGHTS)[0]

     if event_type == 'Malware Detected':
          event_file_name = get_file()
          event_file_path = get_file_path() + str(event_file_name)
          event_file_hash = get_hash()
          event_threat_name = random.choices(endpoint_fields.THREAT_NAME)
          event_action_taken = random.choices(endpoint_fields.ACTION, endpoint_fields.ACTION_WEIGHTS)[0]
          event_user = get_user()
          event_computer_name = get_computer_name()
          event = endpoint_malware_detected_event(event_type, event_file_name, event_file_path, event_file_hash, event_threat_name, event_action_taken, event_user, event_computer_name)
          return event

     elif event_type == 'Scan Started':
          event_scan_type = random.choices(endpoint_fields.SCAN_TYPE, endpoint_fields.SCAN_TYPE_WEIGHTS)[0]
          event_user = get_user()
          event_computer_name = get_computer_name()
          event = endpoint_scan_started_event(event_type, event_scan_type, event_user, event_computer_name)
          return event

     elif event_type == 'Scan Completed':
          event_scan_type = random.choices(endpoint_fields.SCAN_TYPE, endpoint_fields.SCAN_TYPE_WEIGHTS)[0]
          event_malware_found = random_number_likely_zero()
          event_user = get_user()
          event_computer_name = get_computer_name()
          event = endpoint_scan_completed_event(event_type, event_scan_type, event_malware_found, event_user, event_computer_name)
          return event
     
     elif event_type == 'Update Applied':
          event_update_type = random.choices(endpoint_fields.UPDATE_TYPE, endpoint_fields.UPDATE_TYPE_WEIGHTS)[0]
          event_update_version = random_version_number()
          event_user = 'System'
          event_computer = get_computer_name()
          event = endpoint_update_applied_event(event_type, event_update_type, event_update_version, event_user, event_computer)
          return event

     elif event_type == 'Exception':
          event_process = get_legit_file()
          event_reason = random.choices(endpoint_fields.EXCEPTION_REASON, endpoint_fields.EXCEPTION_REASON_WEIGHTS)[0]
          event_user = get_user()
          event_computer = get_computer_name()
          event = endpoint_exception_event(event_type, event_process, event_reason, event_user, event_computer)
          return event

     elif event_type == 'Real-time Protection Enabled':
          event_user = get_user()
          event_computer = get_computer_name()
          event = endpoint_real_time_protection_enabled_event(event_type, event_user, event_computer)
          return event
     
     elif event_type == 'Real-time Protection Disabled':
          event_reason = random.choices(endpoint_fields.REALTIME_PROTECTION_REASON, endpoint_fields.REALTIME_PROTECTION_REASON_WEIGHTS)[0]
          event_user = get_user()
          event_computer = get_computer_name()
          event = endpoint_real_time_protection_disabled_event(event_type, event_reason, event_user, event_computer)
          return event




     


