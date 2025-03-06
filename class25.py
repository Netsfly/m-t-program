class Student:
    def init(self, name: str, student_id: int, grades: list):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        average = sum(self.grades) / len(self.grades)
        return average
    def get_best_grade(self): 
        return self.get_best_grade 
       
    def get_worst_grade(self): 
        return self.get_worst_grade
        
    def display_info(self):
        print(
            f"Student: {self.name}, Student Id: {self.student_id}, Grade: {self.calculate_average()}")

std = Student("Alice", 101, 85)
std1 = Student("Bob", 102, 78.5)
std2 = Student("Nick", 103, 60)
std.add_grade(80)
std.add_grade(50)
std.add_grade(40)
std.calculate_average()
std.display_info()

std1.add_grade(78.5)
std1.add_grade(52)
std1.add_grade(33)
std1.calculate_average()
std1.display_info()

std2.add_grade(60)
std2.add_grade(69)
std2.add_grade(12)
std2.calculate_average()
std2.display_info()



class StudentManager:
    def init(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def calculate_average(self):
        total_a = sum(student.calculate_average() 
        for student in self.students) / len(self.students) 
        return total_a
    def get_top_student(self): 
        top_s = max(self.students, key=lambda student: student.calculate_average())
        return top_s
    def get_lowest_student(self): 
        los_s = min(self.students, key=lambda student: student.calculate_average())
        return los_s
    def display_all_students(self  ): 
        for student in self.students:
            student.display_info()
            
manager = StudentManager()
manager.add_student(std)
manager.add_student(std1)
manager.add_student(std2)
top_student = manager.get_top_student()
lowest_student = manager.get_lowest_student()
manager.display_all_students()
average_grade = manager.calculate_average()


print(f"Average Grade of All: {average_grade}")
print(f"Top Student: {top_student.name} with Average Grade: {top_student.calculate_average()}")
print(f"Lowest Student: {lowest_student.name} with Average Grade: {lowest_student.calculate_average()}")