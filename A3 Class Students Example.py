#Learning Class 2nd Students RanaUniverse 🍌🍌🍌

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} has enrolled in the course: {course.title}")

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} has dropped the course: {course.title}")

class Course:
    def __init__(self, title, course_code):
        self.title = title
        self.course_code = course_code

# Creating students
students = [
    Student("Alice", "A123"),
    Student("Bob", "B456"),
    Student("Charlie", "C789"),
    Student("David", "D101"),
    Student("Eva", "E202"),
    Student("Frank", "F303"),
    Student("Grace", "G404"),
    Student("Helen", "H505"),
    Student("Ivy", "I606"),
    Student("Jack", "J707"),
]

# Creating courses
courses = [
    Course("Mathematics", "MATH101"),
    Course("History", "HIST202"),
    Course("Biology", "BIO303"),
    Course("Chemistry", "CHEM404"),
    Course("Physics", "PHYS505"),
    Course("Computer Science", "CS606"),
    Course("Literature", "LIT707"),
    Course("Art", "ART808"),
    Course("Music", "MUS909"),
    Course("Physical Education", "PE1010"),
]

# Enrolling students in random courses
import random

for student in students:
    num_courses_to_enroll = random.randint(1, 5)
    courses_to_enroll = random.sample(courses, num_courses_to_enroll)
    for course in courses_to_enroll:
        student.enroll(course)

# Dropping random courses
for student in students:
    num_courses_to_drop = random.randint(0, 2)
    courses_to_drop = random.sample(student.courses, num_courses_to_drop)
    for course in courses_to_drop:
        student.drop(course)
