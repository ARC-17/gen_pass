import random
import string

def generate_password(size=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(size))
    return password

password_length = int(input("Enter the desired password length"))
generated_password = generate_password(password_length)
print(f'Your password: {generated_password}')
