from faker import Faker

fake = Faker()

def get_random_ip():
    """Generates a random IPv4 address."""
    return fake.ipv4()
