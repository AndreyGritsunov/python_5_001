
import random

def message(text):
    print(text)

def helloy():
    print("Добро пожаловать в игру с конфетами 'Sweet'!!!")

def terms():
    print("Условия игры. Данно 2021 шт конфет. Кто сделает последний ход, тому достанутся все конфеты. Против вас будет играть Вася. Удачи")

def first_move():
    print("Определим кто будет первым.")
    input("Нажмите ENTER для броска")
    i = 1
    while i < 2:
        user = throw()
        bot = throw()
        if user > bot:
            print("bot первый")
            return 1
        elif bot > user:
            print("Хорошее начало вы первый")
            return 0

def throw():
    throw_user = random.randint(1, 28)
    return throw_user

def sweet_col(sweet_kol_balance):
    if sweet_kol_balance < 0:
        return 0
    else:
        return sweet_kol_balance

def main():
    helloy()
    terms()
    name_user = input("Введите ваше имя: ")
    sweet_kol_balance = 2021
    first = first_move()
    
    while sweet_kol_balance > 0:
        if first == 1:
            kol = throw()
            sweet_kol_balance = sweet_kol_balance - kol 
            text = "Бот Вася бросил " + str(kol) + "шт. Осталось " + str(sweet_col(sweet_kol_balance)) + " конфет."
            message(text) 
            first = 0
        else:
            kol = throw()
            input("Нажмите ENTER для броска")
            sweet_kol_balance = sweet_kol_balance - kol 
            text = str(name_user) + " вы бросили " + str(kol) + "шт. Осталось " + str(sweet_col(sweet_kol_balance)) + " конфет."
            message(text)
            first = 1

        if sweet_kol_balance <= 0:
            if first == 0:
                text = "Победил бот Вася, все 2021 шт конфет достаются ему. GAME OVER"
                message(text)
                break
            else:
                text = str(name_user) + " поздравляю, вы победили все 2021 шт конфет достаются вам"
                message(text)
                break
main()