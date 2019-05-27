import string
import random
import argparse

parser = argparse.ArgumentParser(description='generate a password with x amount of randomised ascii characters')
parser.add_argument('x', metavar='N', type=int, help='length of desired password string')
args = parser.parse_args()

x = args.x

password_characters = string.ascii_letters + string.digits + string.punctuation
secret_key = ''.join(random.choice(password_characters) for i in range(x))
print secret_key
