scores=list(map(int,input("Введите список оценок через пробел").split()))
even_numbers = 0
odd_numbers = 0
result=[]
for score in scores:
    if score >= 90:
        grade="A"
        result = "Pass"
    elif score >= 80:
        grade="B"
        result ="Pass"
    elif score >= 70:
        grade="C"
        result = "Pass"
    elif score >= 60:
        grade="D"
        result = "Pass"
    else:
        grade="F"
        result ="Fail"

    print(f"Балл:{score}, Оценка:{grade}, Результат: {result}")
    
    if score % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
        
    print(f"Четных оценок:{even_numbers}")
    print(f"Нечетных оценок:{odd_numbers}")