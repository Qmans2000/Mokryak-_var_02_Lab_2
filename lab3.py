import math
from random import random

print("Натуральне число було загадано. Число знаходиться в діапазоні від 1 до 100.")
target = math.ceil(random() * 100)
#print("Загадане число:", target)  

print("Введіть кількість спроб, за яку ви хочете відгадати число.")
try:
    tries = int(input())
except ValueError:
    print("Помилка: введіть тільки цілі числа.")
    exit(1)

if tries <= 0:
    print("Помилка: кількість спроб повинна бути додатною.")
    exit(1)

false_tries = []
success_tries = []

attempt = 1

while attempt <= tries:
    print("Спроба #%d: Введіть ваші числа або 'HELP' для допомоги." % attempt)
    command = input().strip()

    switch = {
        "exit": lambda: exit(0),
        "HELP": lambda: print(
            "Ось ваші невдалі спроби: %s" % ", ".join(map(str, false_tries)) +
            " Та вдалі: " + ", ".join(map(str, success_tries))
        ) if false_tries or success_tries else print("У вас ще не було спроб.")
    }

    if command in switch:
        switch[command]()
        continue

    try:
        guess = list(map(int, command.split()))
    except ValueError:
        print("Помилка: введіть тільки цілі числа або 'HELP'")
        continue
    if len(guess) == 1 and guess[0] == target:
        print("Вітаємо! Ви відгадали число %d!" % target)
        exit(0)

    found = False
    for num in guess:
        if num == target:
            success_tries.append(num)
            found = True
            break

    if found:
        print("Yes")
        success_tries.append(target)
    else:
        print("No")
        false_tries.append(guess)

    attempt += 1
print("На жаль, ви не відгадали число %d за %d спроб." % (target, tries))
print("Ваші невдалі спроби: %s" % ", ".join(map(str, false_tries)) + " Та вдалі: " + ", ".join(map(str, success_tries)) + " Загадане число було: %d" % target)