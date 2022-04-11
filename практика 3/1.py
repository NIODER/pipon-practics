def ask_password():
    password = "password"
    for i in range(3):
        input_password = input()
        if input_password == password:
            print("Пароль принят")
            return
    print("В доступе отказано")


ask_password()
