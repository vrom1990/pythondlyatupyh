m1 = 10
m2 = 10
m3 = 10
m4 = 10
m5 = 10
m6 = 10
m7 = 10
m8 = 10
m9 = 10
m10 = 10

if m1+m2+m3 < m4+m5+m6:
    if m1 < m2:
        print("Первая фальшивая")
    elif m1 > m2:
        print("Вторая фальшивая")
    else:
        print("Третья фальшивая")
elif m1+m2+m3 > m4+m5+m6:
    if m4 < m5:
        print("Четвёртая фальшивая")
    elif m4 > m5:
        print("Пятая фальшивая")
    else:
        print("Шестая фальшивая")
else:
    if m7 < m8:
        print("Седьмая фальшивая")
    elif m7 > m8:
        print("Восьмая фальшивая")
    else:
        print("Девятая фальшивая")