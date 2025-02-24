# Ask for desired length (12 - 128)
# Ask if you want symbols
# Ask if want capital letters
# Ask if want numbers
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


password = ''.join(random.choices(string.ascii_lowercase, k=length))     

print(f"Generated Password: {password}")
