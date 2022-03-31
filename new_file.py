import pyttsx3
engine =pyttsx3.init()

engine.setProperty("rate", 400)
engine.setProperty("volume", 0.5)

pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}

dic_cake = {1:"наполеон", 2:"медовик", 3:"киевский"}

while True:
    try:
            menu = "Наполеон - 1" \
                   "Медовик - 2" \
                   "Киевский - 3" \
                   "Если вам ничего не подходит - 4."
            engine.say(menu)
            engine.runAndWait()
            choice_cake = int(input("Какой торт Вы хотели бы приобрести: "))
            while choice_cake > 4 or choice_cake < 1:
                print("повторите попытку, выберите из предложенного диапозона")
                menu = "Наполеон - 1" \
                       "Медовик - 2" \
                       "Киевский - 3"
                engine.say(menu)
                engine.runAndWait()
                choice_cake = int(input("Какой торт Вы хотели бы приобрести: "))

            if choice_cake == 4:
                print("приходите ещё")
                voice10 = "приходите ещё"
                engine.say(voice10)
                engine.runAndWait()
                break
            for k, v in dic_cake.items():
                if k == choice_cake:
                    cake = v

            choice = "Состав -  1." \
                     "Цена - 2" \
                     "Остаток - 3" \
                     "вся информация - 4" \
                     "Купить - 5" \
                     "Выход  0"
            engine.say(choice)
            engine.runAndWait()
            wish = int(input("Что Вы хотели бы уточнить: "))
            while wish > 5 or choice_cake < 1:
                print("повторите попытку, выберите из предложенного диапозона")
                choice = "Состав -  1." \
                         "Цена - 2" \
                         "Остаток - 3" \
                         "вся информация - 4" \
                         "Купить - 5" \
                         "Выход  0"
                engine.say(choice)
                engine.runAndWait()
                wish = int(input("Что Вы хотели бы уточнить: "))

            for k, v in pastry.items():
                if k == cake:
                    if wish == 1:
                        print(f"Торт {k} состоит из {v[0]}")
                        voice = f"Торт {k} состоит из {v[0]}"
                        engine.say(voice)
                        engine.runAndWait()
                    elif wish == 2:
                        print(f"Торт {k} стоит {v[1]} рублей")
                        voice2 = f"Торт {k} стоит {v[1]} рублей"
                        engine.say(voice2)
                        engine.runAndWait()
                    elif wish == 3:
                        print(f"Торт {k} осталось {v[-1]} грамм")
                        voice3 = f"Торт {k} осталось {v[-1]} грамм"
                        engine.say(voice3)
                        engine.runAndWait()
                    elif wish == 4:
                        print(f"Торт {k} состоит из {v[0]} , стоит {v[1]} руб, осталось {v[-1]} грамм")
                        voice4 = f"Торт {k} состоит из {v[0]} , стоит {v[1]} руб, осталось {v[-1]} грамм"
                        engine.say(voice4)
                        engine.runAndWait()
                    elif wish == 5:
                        voice5 = "Сколько торта Вам положить"
                        engine.say(voice5)
                        engine.runAndWait()
                        weight = int(input(" Сколько торта Вам положить: "))
                        sale = input("Промокод: ")
                        if weight > v[2]:
                            print(f"торта {k} осталось всего {v[2]} грамм на сумму {pastry[k][1] * v[2] / 100} рублей")
                            voice14 = f"торта {k} осталось {v[2]} грамм на сумму {pastry[k][1] * v[2] / 100} рублей"
                            engine.say(voice14)
                            engine.runAndWait()
                            break
                        elif weight <= v[2] and sale != "sale":
                            print(f"к оплате {pastry[k][1] * weight / 100}")
                            voice6 = f"к оплате {pastry[k][1] * weight / 100}"
                            engine.say(voice6)
                            engine.runAndWait()
                            print(f"торта {k} осталось {v[2] - weight} грамм")
                            voice7 = f"торта {k} осталось {v[2] - weight} грамм"
                            engine.say(voice7)
                            engine.runAndWait()
                        elif weight <= v[2] and sale == "sale":
                            print(f"к оплате {round((pastry[k][1] * weight / 100 * 0.7), 2)}")
                            voice6 = f"к оплате {round((pastry[k][1] * weight / 100 * 0.7), 2)}"
                            engine.say(voice6)
                            engine.runAndWait()
                            print(f"торта {k} осталось {v[2] - weight} грамм")
                            voice7 = f"торта {k} осталось {v[2] - weight} грамм"
                            engine.say(voice7)
                            engine.runAndWait()
                    elif wish == 0:
                        print("приходите ещё")
                        voice10 = "приходите ещё"
                        engine.say(voice10)
                        engine.runAndWait()
                        exit()

    except ValueError:
        print("Повторите попытку, Нужно выбрать число")
        voice12 = "Нужно выбрать число"
        engine.say(voice12)
        engine.runAndWait()
