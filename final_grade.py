#calculates final grade of a student

def final_grade():
    no_of_students = int(input("Enter the total number of students in your class: "))
    score_board = {}
    sum_score = (0)                     
    for name in range(no_of_students):
        student_name = input("Enter the name of student: ")
        cat_marks = int(input("Enter the cat marks obtained: "))
        end_term_marks = int(input("Enter the end term grade: "))
        final_grade = cat_marks + end_term_marks

        sum_score += final_grade
        average_score = sum_score/no_of_students
        average_score = round(average_score, 2)
        if student_name not in score_board:
            #word_freq.update({key: value})
            score_board.update({student_name : final_grade})
    print(f"The class score board is as shown: {score_board}")
    print(f"The class average score is : {average_score}")

final_grade()
        
