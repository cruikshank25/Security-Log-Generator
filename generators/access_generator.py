import random 
import ipaddress
from events import access_event
from fields import access_fields
from faker import Faker


# generates a random valid ip address
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


# generate a random username
def get_user():
     faker = Faker()
     fname=faker.first_name()
     user = fname.lower()

     return user


# generate a pretend URL with faker made up of a domain name, uri path, uri extension and a query string
def get_url():
    # initialise the Faker object
    faker = Faker()

    # create a fake domain name
    domain_name = faker.domain_name()
    
    # create a fake resource path
    url_path = faker.uri_path()

    # create a fake file extension
    file_extension = faker.uri_extension()

    # create a possible query string that may or may not be added to the URL on a 20% chance
    query_string = None
    if random.randrange(5) == 1:
        param1 = faker.name()
        param2 = faker.random_number()
        param3 = faker.date_time_this_decade()
        query_string = f'userparam={param1}&id2={param2}&datetime={param3}'
    else:
        pass
    
    if query_string != None:
        url = f"http://{domain_name}{url_path}{file_extension}?{query_string}"
    else:
        url = f"http://{domain_name}{url_path}{file_extension}"

    return url_path, url


# gather and generate values for fields and construct into access event class object
def make_event():
    # get a random valid ip from the 'get_ip' function
    event_client_ip = get_ip()

    # get a randomly generated username
    event_user = get_user()

    # get a randomly generated url from the 'get_url' function
    event_resource, event_url = get_url()
    
    # get semi-random field values from 'fields.py' based on weights
    event_method = random.choices(access_fields.METHOD, access_fields.METHOD_WEIGHTS)[0]
    event_protocol = random.choices(access_fields.PROTOCOL, access_fields.PROTOCOL_WEIGHTS)[0]
    event_status = random.choices(access_fields.STATUS, access_fields.STATUS_WEIGHTS)[0]
    event_user_agent = random.choices(access_fields.USER_AGENT, access_fields.USER_AGENT_WEIGHTS)[0]

    # get a random value for bytes up to the max allowed by a HTTP request
    event_bytes = random.randint(1, 100000)    
    
    # construct the access_event class object from the gathered fields and return it
    event = access_event(event_client_ip, event_user, event_method, event_resource, event_protocol, event_status, event_bytes, event_url, event_user_agent)

    return event