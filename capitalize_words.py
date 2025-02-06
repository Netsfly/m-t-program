text = input(" Ваш текст ")

print("The original string is : " + text)

words = text.split()
for i in range(len(words)):
    if i % 2 == 0:  
        words[i] = words[i].capitalize()

cap = " ".join(words)

print("The alternate word capitalized string is : " + cap)
