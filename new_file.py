import pyttsx3
engine =pyttsx3.init()
engine.setProperty("rate", 300)
engine.setProperty("volume", 0.5)
pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}
menu =   "Наполеон, enter 1." \
                "Медовик - enter 2." \
                "Киевский - enter 3."\
                "Если вам ничего не подходит нажмите 4."
engine.say(menu)
engine.runAndWait()
choice_cake = int(input("Какой торт Вы хотели бы приобрести: "))
if choice_cake == 1:
    cake = "наполеон"
elif choice_cake == 2:
    cake = "медовик"
elif choice_cake == 3:
    cake = "киевский"
elif choice_cake == 4:
    voice10 = "приходите еще"
    engine.say(voice10)
    engine.runAndWait()
    breakpoint()
choice = "If you want to see a description, enter 1." \
         "View price - enter 2." \
         "View quantity - enter 3. " \
         "View all information - enter 4." \
         "If you want to buy a cake, enter 5." \
         "To exit the program, enter 0"
engine.say(choice)
engine.runAndWait()
# choice1 = int(input("rrrrr "))
wish = int(input("Что Вы хотели бы уточнить: "))
for k, v in pastry.items():
    if k == cake:
        if wish == 1:
            voice = f"Торт {k} состоит из {v[0]}"
            engine.say(voice)
            engine.runAndWait()
        elif wish == 2:
            voice2 =f"Торт {k} стоит {v[1]} рублей"
            engine.say(voice2)
            engine.runAndWait()
        elif wish == 3:
            voice3 =f"Торт {k} осталось {v[-1]} грамм"
            engine.say(voice3)
            engine.runAndWait()
        elif wish == 4:
            voice4 = f"Торт {k} состоит из {v[0]} , стоит {v[1]} руб, осталось {v[-1]} грамм"
            engine.say(voice4)
            engine.runAndWait()
        elif wish == 5:
            voice5 = "Сколько торта Вам положить"
            engine.say(voice5)
            engine.runAndWait()
            weight = int(input(" Сколько торта Вам положить: "))
            voice6 = f"к оплате {pastry[k][1] * weight / 100}"
            engine.say(voice6)
            engine.runAndWait()
            voice7 = f"торта {k} осталось {v[2] - weight} грамм"
            engine.say(voice7)
            engine.runAndWait()