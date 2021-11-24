MIN_LENGTH = 5

password = input(f"Enter your password (at least {MIN_LENGTH} characters): ")

while len(password) < MIN_LENGTH:
    print("Invalid password!")
    password = input(f"Enter your password (at least {MIN_LENGTH} characters): ")

print("*" * len(password))