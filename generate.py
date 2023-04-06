import string
import random
import pyperclip

def generate():
    len=20
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    all_chars = upper + lower + numbers + symbols
    password = ''.join(random.sample(all_chars, len))
    return password

def copy(x):
    pyperclip.copy(x)