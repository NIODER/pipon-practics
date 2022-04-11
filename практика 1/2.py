login = input()
second_address = input()

if "@" in login:
    print("Некорректный логин")
elif "@" not in second_address:
    print("Некорректный адрес")
else:
    print("OK")