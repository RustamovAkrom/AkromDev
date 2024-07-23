import random
from string import ascii_lowercase, digits


def generate_token(max_length: int = 50):
    token = ""
    for _ in range(1, max_length):
        token += "".join(random.choices([str(i) for i in ascii_lowercase + digits]))
    return token
