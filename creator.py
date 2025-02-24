import random
import string

while True:
    try:
        length=int(input("What lenth for your password? (Between 12-128): "))
        if 12 <= length <= 128:
            break
        else:
            print("Please enter a number between 12 and 128.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    include_special_chars = input("Include Special Characters? (yes/no): ").lower()   
    if include_special_chars in ['yes', 'no']:
        break
    else:
        print("Please enter 'yes' or 'no'")


while True:
    include_uppercase = input("Include Uppercase Letters? (yes/no): ").lower()
    if include_uppercase in ['yes', 'no']:
        break
    else:
        print("Please enter 'yes' or 'no'")

while True:
    include_numbers = input("Include Numbers? (yes/no): ").lower()
    if include_numbers in ['yes', 'no']:
        break
    else:
        print("Please enter 'yes' or 'no'")

characters = string.ascii_lowercase 

if include_special_chars == 'yes':
    safe_special_chars = "!#$%&'()*+,-./:;<=>?@[\\]^_"
    characters += safe_special_chars

if include_uppercase == 'yes':
    characters += string.ascii_uppercase

if include_numbers == 'yes':
    characters += string.digits

password = ''.join(random.choices(characters, k=length))     

print(f"Generated Password: {password}")
