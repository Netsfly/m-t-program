mark=int(input("Введите оценку за тест:"))

if mark >= 90:
    homework=str(input("Сдали ли студент все домашние задания?(да/нет):"))
    if homework=="да":
      print ("Отлично!Оценка A+")
    elif homework=="нет":
        print ("Хорошая работа,но сдайте все задания!Оценка:А")
        

elif mark >= 80 and mark < 90:
    attendance=str(input("Посещал ли ты более 75% занятий?(да/нет):"))
    if attendance=="да":
      print ("Хорошо!Оценка B")
    elif attendance=="нет":
        print ("Нужно посещать занятия!Оценка С")
    
else: 
        print ("Старайтесь лучше!")