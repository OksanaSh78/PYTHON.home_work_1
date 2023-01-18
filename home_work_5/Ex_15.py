
# Человек играет с человеком:

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите количество конфет  не более 28: "))
    return x


def p_print(name, k, counter, value):
    print(f"Последним ходил {name}, он взял {k}, теперь у него {counter} конфет. У Деда Мороза осталось {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет в мешке у Деда Мороза: "))
poslednii_hod = randint(0, 2)  # флаг очередности
if poslednii_hod:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if poslednii_hod:
        k = input_dat(player1)
        counter1 += k
        value -= k
        poslednii_hod = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        poslednii_hod = True
        p_print(player2, k, counter2, value)

if poslednii_hod:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")