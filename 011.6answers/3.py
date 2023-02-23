from random import randint
PAROL = "123456"
parol = input("Введите пароль: ")
if parol == PAROL:
    code = str(randint(1000,9999))
    print("Ваш код: " + code)
    my_code = input("Введите код из СМС")
    if my_code == code:
        moj_palets = input("Успешное сканирование?: ")
        if moj_palets == "да":
            print("Успешный вход в систему!")
        else:
            print("Неверный отпечаток пальца!")
else:
    print("Неверный пароль")