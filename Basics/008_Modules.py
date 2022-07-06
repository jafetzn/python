"""
One advantage of functions is the way to separate block of code from your main program. By using descriptive names for your functions, your main program will be much easier
to follow. You can go a step further tby stroring your functions in a separate file called module and importing that module inot your main program.
An import statement tells Python to make the code in a module available in the currently running program file.

There are sevral ways to import a module
"""

# Import an ENTIRE MODULE
# First we will need to create a MODULE
# we can do a module that registers students into a course
# and make the main program import that module to call methods in the module
# we can have the modules in a separate directory, but in this example the main program and module will be on the same
# to use a method from the module, you will need to specify the name of the module followed for a dot and then the function name and arguments
# Example> ModuleName.functionName(*args)

# Or we can import SPECIFIC FUNCTIONS
# from ModuleName import FunctionName
# and you can import as many functions as you want separating them by a comma
# from ModuleName import FunctionName1, FunctionName2, FunctionName3
# With this syntax you do not need to use the dot notation when you call the function, just use the functionName as it were on the same file

# Using as to Give a Function or even the module an ALIAS
# from ModuleName import functionName as ALIAS
# import ModuleName as ALIAS

# Or you can just import all module functions using an *
# The asterisk in the import tells Python to copy every function from the module into this program file and you do not need to use the dor notation

# NOTE: All imports should be declared at the beggining of the file, only after the comments if there are Any

import ModuleExample

students_list = []
register_flag = True
welcome_message = "\tWelcome to a new school year!\n\n"
print(welcome_message)
while register_flag:
    response = input("Would you like to register a subject? (yes/no): ")
    if response.lower() != "no":
        if response.lower() != "yes":
            print("\nThis is not a valid answer, please try again!\n\n")
        else:
            fname = input("Please enter your Firstname: ")
            lname = input("Please enter your Lastname: ")
            email = input("Please enter your Email: ")
            subject = input("What subject do you want to take?: ")
            students_list.append(ModuleExample.registerStudent(fname, lname,
             email, subject))
    else:
        response = input("Would you like to see a student subject? (yes/no): ")
        if response.lower() != "no":
            if response.lower() != "yes":
                print("\nThis is not a valid answer, please try again!\n\n")
            else:
                email = input("Enter an email to look in the database"
                + "the subjects: ")
                print("\n\n")
                ModuleExample.getStudentSubjects(students_list, email)
        else:
            print("Thanks for using my program, see you next time!")
            register_flag = False
