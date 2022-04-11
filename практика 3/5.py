def encrypt_caesar(message, step):
    encrypt = []
    for letter in list(message):
        encrypt.append(chr((ord(letter) + int(step))))
    return "".join(encrypt)


def decrypt_caesar(message, step):
    decrypt = []
    for letter in list(message):
        decrypt.append(chr(ord(letter) - int(step)))
    return "".join(decrypt)


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
print(encrypted)
print(decrypt_caesar(encrypted, shift))
