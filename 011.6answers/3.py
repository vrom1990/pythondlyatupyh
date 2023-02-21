from random import randint
PAROL = "123456"
parol = input("Введите пароль: ")
if parol == PAROL:
    code = randint(1000,9999)
else:
    print("Неверный пароль")