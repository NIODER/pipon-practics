import random
import string


def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    lower_delete = ["l", "o"]
    upper_delete = ["I", "O"]
    digits_delete = ["1", "0"]
    for char in lower_delete:
        index = lowercase.index(char)
        lowercase = lowercase[:index] + lowercase[index + 1:]
    for char in upper_delete:
        index = uppercase.index(char)
        uppercase = uppercase[:index] + uppercase[index + 1:]
    for char in digits_delete:
        index = digits.index(char)
        digits = digits[:index] + digits[index + 1:]
    password1 = lowercase[random.randint(0, len(lowercase) - 1)]
    password2 = uppercase[random.randint(0, len(uppercase) - 1)]
    password3 = digits[random.randint(0, len(digits) - 1)]
    all_chars = lowercase + uppercase + digits
    while len(password1 + password2 + password3) < int(length):
        rnd = random.randint(0, 2)
        if rnd == 0:
            password1 += all_chars[random.randint(0, len(all_chars) - 1)]
        elif rnd == 1:
            password2 += all_chars[random.randint(0, len(all_chars) - 1)]
        else:
            password3 += all_chars[random.randint(0, len(all_chars) - 1)]
    list_password = [password1, password2, password3]
    random.shuffle(list_password)
    return "".join(list_password)


def main(count, length):
    passwords = []
    for i in range(int(count)):
        passwords.append(generate_password(length))
    return passwords


print(*main(100, 10), sep="\n")
