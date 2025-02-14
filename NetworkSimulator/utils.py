from faker import Faker

fake = Faker()

def get_random_ip(): # random ipv4 address
    return fake.ipv4()
