from string import ascii_lowercase
import random


def generate_slug(title: str):

    slug = str("-".join(title.split()).lower()) + "-"

    for _ in range(30):
        slug += "".join(random.choice([str(i) for i in ascii_lowercase]))

    return slug


def is_video(file: str):
    return file.split(".")[-1].lower() in ['mp4', 'avi']


def is_audio(file: str):
    return file.split(".")[-1].lower() in ['mp3', 'wav', 'out', 'wma']


def is_photo(file: str):
    return file.split(".")[-1].lower() in ['jpeg', 'jpg', 'png', 'gif']

