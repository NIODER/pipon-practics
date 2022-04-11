import random
import string


def generate_password(length):
    password = ""
    all_letters = string.ascii_letters + string.digits
    delete = ["l", "I", "1", "o", "O", "0"]
    for char in delete:
        index = all_letters.index(char)
        all_letters = all_letters[:index] + all_letters[index + 1:]
    for i in range(length):
        letter_index = random.randint(0, len(all_letters) - 1)
        password = password + all_letters[letter_index]
        all_letters = all_letters[:letter_index] + all_letters[letter_index + 1:]
    return password


def main(count, length):
    passwords = []
    for i in range(count):
        passwords.append(generate_password(length))
    return passwords


print(*main(5, 15))
