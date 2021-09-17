from mymodules.models import Student
from mymodules.math_utils import average_grade

def main():

    roster = [Student("Aman", 97),
    Student("Jasmine", 78),
    Student("Valentine",91),
    Student("Rohan", 81),
    Student("Chandler",79),
    Student("Monica",92 ),
    Student("McCallister", 100),
    Student("Reggie",85),
    Student("Sahib", 82),
    Student("Navi",87)]



    for i in roster:
        i.print_student_info()

    print(f"Average score of the class is: " + str(average_grade(roster)))

if __name__ == "__main__":
     main()
