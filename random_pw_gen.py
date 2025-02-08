import random
import string
import sys

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range (length))
    return password

def main():
    password_length = int(sys.argv[1])
    created_password = generate_password(password_length)
    print(created_password)

if __name__=="__main__":
    main()