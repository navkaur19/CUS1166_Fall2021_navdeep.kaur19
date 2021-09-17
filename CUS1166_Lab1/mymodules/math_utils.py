def average_grade(roster):

    total = 0

    for student in roster:
        total= total + student.get_grade()

    avg = total/len(roster)
    return avg
