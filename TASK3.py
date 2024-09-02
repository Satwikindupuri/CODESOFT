import random
import string

try:
    num_letters = int(input("Enter the number of letters you want in the password: "))
    num_digits = int(input("Enter the number of digits you want in the password: "))
    num_specials = int(input("Enter the number of special characters you want in the password: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()


total_length = num_letters + num_digits + num_specials
if total_length == 0:
    print("The total length of the password must be greater than zero.")
    exit()


password = ''.join(
    random.choices(string.ascii_letters, k=num_letters) +
    random.choices(string.digits, k=num_digits) +
    random.choices(string.punctuation, k=num_specials)
)

# Display the generated password
print(f"Your generated password is: {''.join(random.sample(password, len(password)))}")
