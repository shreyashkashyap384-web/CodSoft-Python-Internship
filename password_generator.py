# Password Generator Program
# This program generates a random and strong password

import random
import string

print("Password Generator")

# Password length input from the user
length = int(input("Enter password length: "))

# Combining letters, digits, and special characters
characters = string.ascii_letters + string.digits + string.punctuation

# Initializing empty password variable
password = ""

# Generating random characters for the password
for i in range(length):
    password += random.choice(characters)

# Displaying generated password
print("Generated Password:", password)