def sale(op,sum,): 
    if op == 1: 
        if sum > 100: 
            return (sum * 20) / 100 
        else: 
            return (sum * 10) / 100 
    if op == 2: 
        if sum > 100: 
            return (sum * 15) / 100 
        else: 
            return (sum * 5) / 100 
    if op == 3: 
        if sum > 100: 
            return (sum * 5) / 100 
        else: 
            print("Скидки нет") 
 
print("""Выберите тип члентсва: 
1.Золото 
2.Серебро 
3.Обычный 
""") 
op = int(input("Выберите от 1 до 3: ")) 
if op in [1, 2, 3]: 
     sum = float(input("Сумма: ")) 
     result = sale(op,sum)