ochki = 0
print("Добро пожаловать в симулятор свиданий с Ингеборгой")
print("Куда позовёте Ингеборгу?",
      "1. Пляж", '2. ТЦ', "3. Центральная площадь", sep = "\n- ")

vybor = input(": ")
if vybor == "1":
    print("В такое время года? Ну а почему бы и нет")
    print("Вы пришли на Пляж. Чем займётесь?")
    print("1: посмотреть на море","2: поискать камушки и ракушки", "3: пофотографироваться на фоне моря", sep = '\n')
    vybor = input(": ")
    if vybor == "1":
        print("Ингеборга: А какие условия будут?")
        print("Варианты ответа(введите 1, 2 или 3): ",
              "1:Просто посидим на песке",
              "2:Я прихватил плед и корзиночку с едой и напитками",
              "3:Я арендую беседку с шикарным видом, нам приготовят готовую еду",
              sep="\n")
        vybor = input(": ")
        if vybor == "1":
            print("Ингеборга: Ок, ну пойдём")
            ochki = ochki - 1
            print("Очки:", ochki)
            print("Вы приходите на пляж")
            print("Смотрите на море")
            print("Проходит полчаса")
            print("Ингеборга: Хочу есть")
            print("Варианты ответа(введите 1 или 2): ",
              "1: А, ну тогда давай прощаться",
              "2: Пойдём, перекусим в кафешке тут рядом",
              sep="\n")
            vybor = input(":")
            if vybor == "1":
                print("Ингеборга: Ну пока")
                ochki = ochki - 1
                print("Очки:", ochki)
            elif vybor == "2":
                print("Ингеборга: Пошли")
                print("Вы приходите в кафе и едите")
                print("Ингеборга: Ладно, пока, мне пора")
            
        elif vybor == "2":
            ochki = ochki + 1
            print("Очки:", ochki)
            print("Ингеборга: Миленько!")
            print("Вы пришли на пляж, и мило сидите, глядя на море")
            print("Ингеборга: слушай, смотри, какое облако красивое!")
            print("Варианты ответа(введите 1, 2 или 3): ",
              "1: Да облако и облако...",
              "2: Похоже на бабочку!",
              "3: Красивое, но ты лучше",   
              sep="\n")
            vybor = input(":")
            if vybor == "1":
                ochki = ochki - 1
                print("Ингеборга: ...")
            elif vybor == "2":
                ochki = ochki + 1
                print("Ингеборга: И правда похоже!")
            elif vybor == "3":
                ochki = ochki + 2
                print("Ингеборга: Ох, прекрати, ты меня смущаешь :-)")
            print("Прошло полчаса")
            print("Ингеборга: Слушай, а сфотографируй меня на фоне моря")
            print("Варианты ответа(введите 1, 2 или 3): ",
              "1: Давай!",
              "2: Не люблю я это всё",
              "3: Давай, а потом покажу тебе рядом тут отличную скалу для фото",   
              sep="\n")
            if vybor == "1":
                ochki = ochki + 1
            elif vybor == "2":
                print("Ингеборга: ладно...")
            elif vybor == "3":
                ochki = ochki + 2
            #здесь
        elif vybor == "3":
            print("Ингеборга: Ого! Давай, здорово!")
            ochki = ochki + 2
            print("Очки:", ochki)
    elif vybor == "2":
        print("Ингеборга: А если мы так устанем?")
    elif vybor == "3":
        ochki = ochki + 1
        print("Очки:", ochki)
        print("Ингеборга: А как именно фотографироваться будем?")
elif vybor == "2":
    ochki = ochki + 1
    print("Очки:", ochki)
    print("Здорово, люблю ходить в ТЦ!")
    print("Чем займёмся?")
    print("Что ответить:","1: Пройдёмся по магазинам",
          "2: Поучаствуем в новых аттракционах", "3: Ничем", sep = "\n- ")
    vybor = input(": ")
    if vybor == "1":
        print("Ок")
        ochki = ochki + 2
    elif vybor == "2":
        ochki = ochki + 1
    elif vybor == "3":
        pass
elif vybor == "3":
    print("Пойдём! Там будет что-то интересное?")
    print("Что ответить:","1: Там будут танцы",
          "2: Там будет ярмарка", "3: Ничего", sep = "\n- ")
    vybor = input(": ")
    if vybor == "1":
        ochki = ochki + 1
        print("Здорово! Поучаствуем?")
        vybor == input("да или нет?")
        if vybor == "да":
            ochki = ochki + 1
        else:
            ochki = ochki - 1
    print("Вы пришли на площадь. Чем займётесь?")
    print("Посидеть на лавочке")
    
    
print("Итак, ваше свидание закончилось.")
print("Сколько очков вы набрали?")