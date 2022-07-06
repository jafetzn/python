def studentFullName(fname, lname):
    return (fname + " " + lname).title()

def registerStudent(fname, lname, email, subject):
    student = {"student_id" : email,
            "student_info" : studentFullName(fname, lname), "subject" : subject}
    print("Student added to the course!\n")
    return student

def getStudentSubjects(students_list, email):
    registered_student = False
    for student in students_list:
        if email.lower() == student['student_id'].lower():
            print(f"This student is registered in\t [{student['subject']}]")
            registered_student = True

    if registered_student == False:
        print("This student is not registered on any subjects\n\n")
