students = [
 {
     "name": "Alice",
     "subjects": ("Math", "Physics", "English"),
     "scores": {"Math": 85, "Physics": 78, "English": 92}},
 {
     "name": "Bob",
     "subjects": ("Math", "Biology", "English"),
     "scores": {"Math": 72, "Biology": 88, "English": 80}},
 {
     "name": "Charlie",
     "subjects": ("Math", "Physics", "Chemistry"),
     "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]

def display_students(data):
    for student in data:
        name = student["name"]
        subjects = ", ".join(student["subjects"])
        print(f"{name} is enrolled in: {subjects}")

display_students(students)

def get_average_score(name, students,):
    for student in students:
        if student['name'] == name:
            scores = student['scores'].values()
            if len(scores)>0:
                return  sum(scores) / len(scores)

print(get_average_score("Charlie", students), "average score")

def find_top_student(students):
    for student in students:
         top_s = None
         highScore = 0

         scores = student['scores'].values()
         if len(scores)>0:
            average =  sum(scores) / len(scores)
            if average > highScore:
                highScore = average
                top_s = student["name"]

    return top_s

print(find_top_student(students))


def failed_students(students, passing_score=50):
    for student in students:
        failed = []
        for score in student['scores'].values():
            if score < passing_score:
                failed.append(student["name"])

            return failed    
        
print(failed_students(students))

def unique_subjects(students):
    subjects = set()
    for student in students:
        subjects.update(student["subjects"].keys())
    return subjects

print(unique_subjects(students))