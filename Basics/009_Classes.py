# We write classes to represent real world objects and situations, and we create objects based on these classes
# When we create an object from a class, that object automatically has the attributes and methods of that class
# Making an object form a class is called INSTANTATION and you work with instances of a class
# We can store our CLASSES in MODULES
#

class Dog:
    # We always have to put some notation, comments to indicate this class what is it for
    """ A simple class to show how it works """

    # The init method will always start with __ and will end with other 2 __
    # Each method in a class will receive the SELF parameter,it must come before the other parameters
    # and means that when Python calls this method to crate an instance of the class
    # the method call will automatically pass the self argument which is a reference to
    # the instance itself, and it gives the individual instance access to the
    # attributes and methods of the class
    def __init__(self, name, color, age):
        #Initialazing attributes of the instance
        self.name = name
        self. color = color
        self.age = age

    # __str__ special method works when we create an instance of a class and we want to print that object
    # what this method return, will be printed in the output.
    def __str__(self):
        return f"Name:\t{self.name}\nColor:\t{self.color}\nAge:\t{self.age}"

    def sit(self):
        """ This is called DOCSTRING and its a brief description of the method itself, and must be on the same level of indentation as the method's body """
        print(f"The dog {self.name} is now sitting!")

    def roll(self):
        print(f"The dog {self.name} rolled over!")

# We create an instance of a class by oput the instance name , = , and call the init method or a Constructor of the class.
# note that we do not need to pass anuthing on the self argument, because python
# does that automatically
my_dog = Dog("jack","brown and white",7)
# I can create as many instances of the class I want
my_other_dog = Dog("plata","brown",8)
# We can access attributes and methods using the DOT notation
my_dog.sit()
my_dog.roll()
print(f"My dog's age is {my_dog.age}")
print(f"My other dog's name is {my_other_dog.name}")
print("\n\n")
print(my_dog)

"""
check out the file Person.py, which is an example of a parent class and a child class which has inheritance.
"""
