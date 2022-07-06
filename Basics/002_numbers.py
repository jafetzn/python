"""
Arithmetic operators
Python can operate with numbers using the usual mathematical operators, and some special operators, too. These are all of them (we'll explore the last two in later videos).
a + b = Adds a and b
a - b = Subtracts b from a
a * b = Multiplies a and b
a / b = Divides a by b
a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a)
a // b = The integer part of the integer division of a by b
a % b = The remainder part of the integer division of a by b
"""

#Integers

def integerM():
    #not much to say
    #We can use underscores to make big numbers more understandable
    universeAge = 14_000_000_000
    print(universeAge)

def floatM():
    #If we use integers and floats, the result will be always be floatM
    #If we divide two numbers, will always get a floatM
    print(1*3.1)
    print(14/2)

def multiple():
    x, y, z = 1,2 ,3
    return x,y,z

def constants():
    #A constant is a variable whos value stays the same all the time, we use CAPITAL letters to indicate that a variable should be treated as a constant and never be changed
    MAX_CONECTIONS = 2000


integerM()
floatM()
x,y,z = multiple()
print(f"{x}, {y}, {z}")
