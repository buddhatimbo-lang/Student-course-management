class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []

    def display_info(self):
        print("Student_id:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)

        print("course:")
        for course in self.courses:
            print(course.course_code, "-", course.course_name)

        print()

    def add_course(self, course):
        self.courses.append(course)

    def add_courses(self, course):
        self.courses.append(course)

    @classmethod
    def create_student(cls, student_id, pseudonym):
        return cls (student_id, pseudonym, "N/A")




class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)

    print()

# create student objects
student1 = Student.create_student("ST6001", "student_A")
student2 = Student.create_student("ST6002","student_B")

# create course object
course1 = Course("DIT1201", "Object-oriented Programming")
course2 = Course("BIT1202","Database")

# list
students = []
courses = []

def add_record(records, record):
    records.append(record)

def display_records(records):
    for record in records:
        record.display_info()

# add to students list
add_record(students, student1)
add_record(students, student2)

# add to courses list
add_record(courses, course1)
add_record(courses, course2)

#assign courses to student
student1.add_course(course1)
student1.add_course(course2)

student2.add_course(course1)

# display
display_records(students)

# display
display_records(courses)

#search for student
search_id = input("Enter student ID: ")

print()

found = False

for student in students:
    if student.student_id == search_id:
        student.display_info()
        found = True

if not found:
    print("student not found.")

# search for course_code
search_code = input("Enter course code: ")

found = False

for course in courses:
    if course.course_code == search_code:
        course.display_info()
        found = True

if not found:
        print("course not found.")




