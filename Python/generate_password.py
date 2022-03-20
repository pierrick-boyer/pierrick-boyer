import random
import string


def generate_password():
    ask_length = input("Enter the length of the password to generate: ")
    length = int(ask_length)
    password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return ''.join(random.choice(password) for i in range(length))