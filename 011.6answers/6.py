ochki = 0
print("Добро пожаловать в симулятор свиданий с Ингеборгой")
print("Куда позовёте Ингеборгу?",
      "1. Пляж", '2. ТЦ', "3. Центральная площадь", sep = "\n- ")

vybor = input(": ")
if vybor == "1":
    print("В такое время года? Ну а почему бы и нет")
    print("Вы пришли на Пляж. Чем займётесь?")
    print("посмотреть на море","поискать камушки и ракушки", "пофотографироваться на фоне моря", sep = '\n')
    vybor = input(": ")
    if vybor == "посмотреть на море":
        print("А какие условия будут?")
        print("Варианты ответа(введите 1, 2 или 3): ",
              "1:Просто посидим на песке",
              "2:Я прихватил плед и корзиночку с едой и напитками",
              "3:Я арендую беседку с шикарным видом, нам приготовят готовую еду",
              sep="\n")
        vybor = input(": ")
        if vybor == "1":
            ochki = ochki + 2
            print("Ого, ну пойдём")
        elif vybor == "2":
            ochki = ochki + 1
            print()
    elif vybor == "поискать камушки и ракушки":
        pass
    elif vybor == "пофотографироваться на фоне моря":
        ochki = ochki + 1
        print("А как именно фотографироваться будем?")
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
        ochki = ochki + 2
    elif vybor == "Поучаствуем в новых аттракционах":
        ochki = ochki + 1
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