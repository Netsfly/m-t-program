import math

def calculate(num1, num2, operation):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        return "Ошибка: деление на ноль" if num2 == 0 else num1 / num2
    elif operation == 5:
        return num1 ** num2
    elif operation == 6:
        return "Ошибка: корень из отрицательного числа" if num1 < 0 else math.sqrt(num1)
    elif operation == 7:
        return (num1 * num2) / 100
    else:
        return "Неверный выбор"

print("""Выберите функцию:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Возведение в степень (num1^num2)
6. Извлечение корня из первого числа (√num1)
7. Процент (num1% от num2)
""")


op = int(input("Выберите от 1 до 7: "))
if op in [1, 2, 3, 4, 5, 7]:
        n1 = float(input("Введите первое число: "))
        n2 = float(input("Введите второе число: "))
        result = calculate(n1, n2, op)
elif op == 6:
        n1 = float(input("Введите число для извлечения корня: "))
        result = calculate(n1, None, op)
else:
        result = "Неверный выбор"
print(f"Результат: {result}")
