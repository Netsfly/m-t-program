word=input("Введите слово:") 
vowels = "aioue"
vowels_count = 0
consonant = 0
for char in word:
    if char in vowels:
        vowels_count+=1
    else:
        consonant+=1
print(vowels_count)
print(consonant)