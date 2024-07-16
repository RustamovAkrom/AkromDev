from string import ascii_lowercase
import random

def generate_slug(title: str):

    slug = str("-".join(title.split()).lower()) + "-"
    
    for _ in range(30):
        slug += "".join(random.choice([str(i) for i in ascii_lowercase]))

    return slug

