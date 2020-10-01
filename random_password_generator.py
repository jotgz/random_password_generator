import string
import random


alphabet_string = string.ascii_lowercase
uppercase_alphabet_string = string.ascii_uppercase

uppercase_alphabet_list = list(uppercase_alphabet_string)
alphabet_list = list(alphabet_string)
special_characters_list = ['@', '$', '&', '!', '%']
full_alphabet = alphabet_list + uppercase_alphabet_list + special_characters_list

password = ''


def password_length():

    global prompt
    prompt = int(input('Pick a number from 8 - 20 '))
    
    if prompt not in range(8, 21):
        print('Value has to be between 8 and 20, please choose again')
        password_length()


def generate_password():
    global password
    password = ''.join(random.choice(full_alphabet) for x in range(prompt))
    print(f'Your password is {password}')
   

def run():

    password_length()

    generate_password()

run()