class Student (object):

    def __init__(self, name, grade):
        self.student_name = name
        self.student_grade = grade

    def set_student_grade(self, grade):
        self.student_grade = grade

    def get_grade(self):
        return self.student_grade

    def print_student_info(self):
        print(f"Name of the student is {self.student_name}, and their grade is {self.student_grade}")
        
