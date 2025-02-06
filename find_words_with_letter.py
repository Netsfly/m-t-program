words = ["banana", "apple", "cherry", "grape"] 
letter = "a"

if words:  
    found = False  
    for w in words:
        if letter in w:
            print(w)
            found = True  
    if not found:  
        print("not found")
