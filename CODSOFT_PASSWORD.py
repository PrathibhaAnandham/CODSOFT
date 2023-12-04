import random
import string

def generate_password(len_password):
    ch = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(ch) for _ in range(len_password))
    return password

len_password = int(input("Enter the desired length of the password: "))
password = generate_password(len_password)
f"Generated password:{password}"