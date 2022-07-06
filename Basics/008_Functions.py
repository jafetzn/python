def helloWorld():
    print("Hello fckng World!")

#We can comment on one line using #
"""
Or we can comment in multi line using x3 " to open and the same to close
and it would be the same as if we were using # in the start of each line
"""
#we can return values using return keyword
def area_triangle(base, height):
    return base * height / 2

"""

these 2 loines below are the same, because we are telling python which value is what when passing arguments to the function
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
"""

#Any parameter with a default name needs to be listed after all the parameters that dont have default values
def defaultValues(username,type="student"):
    print(f"My username is {username} and I am a {type}")


#Passing an arbitrary number of arguments
#By puttin * in the parameter of the function we specify that the function can receive as many arguments as the user sends
def hobbies(*hobbies):
    print(hobbies)

helloWorld()
print(area_triangle(10,20))
defaultValues("jafetzn")
defaultValues("jafetzn", "programmer")
defaultValues(username="paola")
hobbies("dance")
hobbies("dance","run","climb","fuck")
