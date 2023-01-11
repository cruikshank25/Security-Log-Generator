import random 
import ipaddress
from events import access_event
from fields import access_fields
from faker import Faker

def get_ip():
    # generate a random octet (a number between 0 and 255)
    octet1 = random.randint(0, 255)
    octet2 = random.randint(0, 255)
    octet3 = random.randint(0, 255)
    octet4 = random.randint(0, 255)

    # create a string representation of the ip address
    ip_str = f"{octet1}.{octet2}.{octet3}.{octet4}"

    # create an ip address object using the ip_address function
    ip_addr = ipaddress.ip_address(ip_str)

    return ip_addr


def get_url():

    faker = Faker()
    domain_name = faker.domain_name()
    url_path = faker.uri_path()
    file_extension = faker.uri_extension()
    param1 = faker.name()
    param2 = faker.random_number()
    param3 = faker.date_time_this_decade()
    query_string = f'param1={param1}&param2={param2}&param3={param3}'
    url = f"http://{domain_name}{url_path}{file_extension}?{query_string}"

    return url_path, url


def make_event():

    event_client_ip = get_ip()
    event_resource, event_url = get_url()
    event_method = random.choices(access_fields.METHOD, access_fields.METHOD_WEIGHTS)[0]
    event_protocol = random.choices(access_fields.PROTOCOL, access_fields.PROTOCOL_WEIGHTS)[0]
    event_status = random.choices(access_fields.STATUS, access_fields.STATUS_WEIGHTS)[0]
    event_bytes = random.randint(1, 100000)
    event_user_agent = random.choices(access_fields.USER_AGENT, access_fields.USER_AGENT_WEIGHTS)[0]

    event = access_event(event_client_ip, event_method, event_resource, event_protocol, event_status, event_bytes, event_url, event_user_agent)

    return event