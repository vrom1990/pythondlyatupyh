login = input("Введите логин> ")
parol = input("Введите пароль> ")
while login != "admin" or parol != "123456":
    print("Логин или пароль неверны!")
    login = input("Введите логин> ")
    parol = input("Введите пароль> ")
    
print("Успешный вход")