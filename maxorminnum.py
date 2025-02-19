numbers=[22,45,67,12,89,34,55,90,10]
max_number=0
min_number=0

for num in numbers:
     if num> max_number:
         max_number=num  
     if num< min_number:
         min_number=num

print("Максимальное число",max_number)
print("Минимальное число",min_number)