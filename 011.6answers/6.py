ochki = 0
print("Добро пожаловать в симулятор свиданий с Ингеборгой")
print("Куда позовёте Ингеборгу?",
      "Пляж", 'ТЦ', "Центральная площадь", sep = "\n- ")

vybor = input(": ")
if vybor == "Пляж":
    print("В такое время года? Ну а почему бы и нет")
    print("Вы пришли на Пляж. Чем займётесь?")
    print("посмотреть на море","поискать камушки и ракушки", "пофотографироваться на фоне моря", sep = '\n')
    vybor = input(": ")
    if vybor == "посмотреть на море":
        pass
    elif vybor == "поискать камушки и ракушки":
        pass
    elif vybor == "пофотографироваться на фоне моря":
        ochki = ochki + 1
elif vybor == "ТЦ":
    ochki = ochki + 1
    print("Очки:", ochki)
    print("Здорово, люблю ходить в ТЦ!")
    print("Чем займёмся?")
    print("Что ответить:","-Пройдёмся по магазинам",
          "-Поучаствуем в новых аттракционах", "-Ничего", sep = "\n- ")
    vybor = input(: )
    if vybor == "Пройдёмся по магазинам":
        print("Ок")
        ochki = ochki + 1
    elif vybor == "Поучаствуем в новых аттракционах":
        pass
elif vybor == "Центральная площадь":
    print("Пойдём! Там будет что-то интересное?")
    print("Что ответить:","-Там будут танцы",
          "-Там будет ярмарка", "-Ничего", sep = "\n- ")
    vybor = input(": ")
    if vybor == "Там будут танцы":
        ochki = ochki + 1
        print("Здорово! Поучаствуем?")
        vybor == input("да или нет?")
        if vybor == "да":
            ochki = ochki + 1
        else:
            ochki = ochki - 1
    print("Вы пришли на площадь. Чем займётесь?")
    print("Посидеть на лавочке")