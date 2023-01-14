import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation + '@'
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

password = generate_password(16)
print(password)
