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