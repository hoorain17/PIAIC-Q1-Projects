import random

print('Welcome to your password generator')

# Correct the character set by removing commas
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*().,/?1234567890'

# Get the number of passwords to generate and the password length
number = int(input('Amount of passwords to generate: '))
length = int(input('Input your password length: '))

print('\nHere are your passwords:\n')

# Generate passwords
for _ in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)












       