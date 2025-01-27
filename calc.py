def calculate(num1, num2, operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        return "Ошибка: деление на ноль" if num2 == 0 else num1 / num2
    else:
        return "Неверный выбор"

print("""Выберите функцию:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
""")
op = int(input("Выберите 1, 2, 3 или 4: "))
n1, n2 = float(input("Введите первое число: ")), float(input("Введите второе число: "))   
result = calculate(n1, n2, op)
print(f"Результат: {result}")
