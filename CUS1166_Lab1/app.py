from mymodules.models import Student
from mymodules.math_utils import average_grade

def main():

    roster = [Student("John", 90),
    Student("Joe", 87),
    Student("Kt",91),
    Student("Paris", 90),
    Student("Lilly",89),
    Student("Kevin",92 ),
    Student("Michael", 94),
    Student("Reggie",90),
    Student("Justin", 82),
    Student("Navi",88)]



    for i in roster:
        i.print_student_info()

    print(f"Average score of the class is: " + str(average_grade(roster)))

if __name__ == "__main__":
     main()
