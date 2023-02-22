from random import randint
PAROL = "123456"
parol = input("Введите пароль: ")
if parol == PAROL:
    code = str(randint(1000,9999))
    print("Ваш код: " + code)
    my_code = input("Введите код из СМС")
    if my_code == code:
        pass
else:
    print("Неверный пароль")