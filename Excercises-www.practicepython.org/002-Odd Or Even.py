"""
Exercise 2 (and Solution)
The exercise comes first (with a few extras if you want the extra challenge or
want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print
out an appropriate message to the user. Hint: how does an even / odd number react
differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number
to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message
"""

number = int(input("Please enter a number:\t"))

if number%2 == 0:
    print("Its a even number")
else:
    print("Its an odd number")

#if number%4 == 0:
