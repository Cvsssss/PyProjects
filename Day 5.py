import random

print("Welcome to the random password generator")
total = int(input("How long do you want?: "))
usr_number = int(input("How many number do you want?: "))
usr_letters = int(input("How many symbols do you want?: "))
password = []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["@", "#", "$", "%", "&"]

for n in range(0,usr_number):
    random_int = random.randint(0,9)
    password.append(numbers[random_int])
for b in range(0,usr_letters):
    random_symbol = random.randint(0,4)
    password.append(symbols[random_symbol])
for c in range(0,total-usr_letters-usr_number):
    random_letter = random.randint(0,25)
    password.append(letters[random_letter])

random.shuffle(password)
final_pass = ''.join(str(c) for c in password)
print(f"Your password is: {final_pass}")