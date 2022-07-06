class Person:
    """This will be the PARENT class, which will be inherited by Student class"""
    # The first line when we declare the class, we should put the parent class
    # between brackets as follow "class ClassName(parentClass):"

    def __init__(self, firstname, lastname, sex, country, midname = ''):
        super(Person, self).__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.country = country
        self.midname = midname

    def getFullName(self):
        if self.midname != '':
            return f"{self.firstname} {self.midname} {self.lastname}".title()
        else:
            print("mid name esta vacio")
            return (f"{self.firstname} {self.lastname}".title())

    def setSex(self, new_sex):
        self.sex = new_sex

    def getSex(self):
        return self.sex.title()

    def setCountry(self, new_country):
        pass

    def getCountry(self):
        return self.country.title()

    def run(self, miles):
        print(f"{self.firstname.title()} is running in the park now, he's run {miles} miles.")

    def study(self, subject):
        print(f"{self.firstname.title()} is studying for {subject} exam.")

    def sleep(self, hours):
        print(f"{self.firstname.title()} has been sleeping for {hours} hrs.")

class Student(Person):
    """A class example to understand the capabilities of a class, this class is child of PERSON"""

    def __init__(self, firstname, lastname, sex, country, midname = "", email = "", subjectList = []):
        # Super() is a special function that allows you to call a method from
        # the PARENT class. This line tells Python to call the __init()__
        # method from Person
        super().__init__(firstname, lastname, sex, country, midname)
        self.email = email
        self.subjectList = subjectList
        # This is an attribute that has a value by default
        # Can be definded in the init and without being passed as patrameters
        self.classroom = "A"

    def setEMail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def addSubject(self, subject):
        self.subjectList.append(subject)

    def removeSubjcet(self, subject):
        self.subjectList.remove(subject)

    def getSubjectList(self):
        return self.subjectList

student1 = Student("moises","zarate naranjo","Male", "Mexico", "jafet")
print(f"My name is {student1.getFullName()}")
print(f"I am from {student1.getCountry()}")
student1.setEMail("jafetzarate@outlook.com")
print(f"My email is: {student1.getEmail()}")
print(f"I have been assigned to the classroom {student1.classroom}\n")
student1.addSubject("Programming")
student1.addSubject("English")
student1.addSubject("Economy")
print(f"I have the following subjects this year {student1.getSubjectList()}")
student1.removeSubjcet("Economy")
print(f"Next year I will have only these ones: {student1.getSubjectList()}")
######
student1.study("Programming")
student1.sleep(3)
student1.run(20)
