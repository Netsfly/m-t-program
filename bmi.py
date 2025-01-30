height = float(input("height"))
weight = float(input("weight"))
bmi = (weight) / height ** 2
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normalweight")
elif bmi >= 25 and bmi <= 29.9:
    print("Normalweight")
elif bmi >= 30 and bmi <= 34.9:
    print("Normalweight")
elif bmi >= 35 and bmi <= 39.9:
    print("Normalweight")
elif bmi >= 40:
    print("Obesity class III")