import string
import random

password_characters = string.ascii_letters + string.digits + string.punctuation
secret_key = ''.join(random.choice(password_characters) for i in range(16))
print secret_key
