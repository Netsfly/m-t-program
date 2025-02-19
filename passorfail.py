studentsmark=[65,90,45,80,50,56,88,92,59,30]
results = []
for mark in studentsmark:
    if mark >=60:
     results.append((mark,"pass"))
else:
    results.append((mark,"fail"))
for result in results:
    print("Mark",result[0],result)