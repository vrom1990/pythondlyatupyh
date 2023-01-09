import time

t = int(input("Введите температуру: "))

while t <= 50:
    print("Делаем дела")
    time.sleep(1)
    t = int(input("Введите температуру: "))

print("ТРЕВОГА!")
    
