import random

print('A simple program for creating passwords.')
try:
    number = int(input('How many letters must be the password? '))
    password = ''
    for i in range(number):
        password = password + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnm!@#$%&*()-+'))
    print(f'Your password is {password}')
except ValueError:
    print('We need numbers')
