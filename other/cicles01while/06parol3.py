login = input("Введите логин> ")
parol = input("Введите пароль> ")
while login != "admin" or parol != "123456":
    if login != "admin":
        if parol != "123456":
            print("Логин и пароль не верны")
        else:
            print("Логин не верен")
    else:
        print("Пароль не верен")
    login = input("Введите логин> ")
    parol = input("Введите пароль> ")
    
print("Успешный вход")