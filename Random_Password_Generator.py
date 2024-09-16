import random
import string

def generate_password(length):
    chars=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(chars) for _ in range(length))
    return password

while True:
    length=int(input("Enter desired password length (between 8 and 32): "))
    if 8<=length<=32:
        break
    print("Invalid input. Please enter a value between 8 and 32.")
password=generate_password(length)
print("Generated Password:",password)