"""
In order to read something coming from the users, we will need to use the INPUT method input()
This function pauses the program and waits for the user to enter some text. Once python has received the nuser Input
it assigns that input to a variable so you can work with.
The function takes one argument, the text we want to display to the user so they can now what to do
"""

message = input("Enter some text: ")
print(f"\nThe text you entered is: {message}")

#we can also accept numerical Input

age = int(input("How old are you?: "))
print(type(age))

response = ''
while response != 'quit':
    response = input("This will only stop if you enter 'quit', otherwise I will appear forever!")
    if response == 'quit':
        print("Thanks for using my program")
        break

"""
We can use the break keyword to let the program know that we want to exit the while loop
Also we can use a boolean flag in the while loop to let the program know when to exit
"""
active = True
while active:
    response = input("This will only stop if you enter 'quit', otherwise I will appear forever!")
    if response == 'quit':
        print("Thanks for using my program")
        active = False


"""
The CONTINUE keyword in a While loop, is used to indicate the loop to return to the beggining of the loop and this might be useful
when you want to skip some code to be executed. For example, you want to print only odd numbers
"""

counter = 0
while counter < 10:
    counter += 1
    if counter%2 == 0:
        continue
        # Here if the counter is ODD, then we want to continue with the iteration
    print(counter)
