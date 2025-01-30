from random import randint

x = randint(1,50)
print(x)
num = 0

while True:
    print("Угадай загаданное число")
    num = int(input(" Ваше число "))
    if num == x:
        print("Угадал")
        break
    elif num > x:
        print(" Число меньше ")
    elif num < x:
        print(" Число больше 2")