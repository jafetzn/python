"""
examining a set of conditions and deciding which action to take based on thos conditions it is what we use the IF statement
we can check for equality == and inequality !=, or have one or multilple conditions using AND or OR keywords
"""

def ifsimple():
    cars = ['audi','bmw','mazda','kia','subaru','toyota']

    for car in cars:
        if car == "bmw" or car == "kia":
            print(car.upper())
        else:
            print(car.title())

def caseMatters(s):
    if "audi" == s:
        print("they match")
    else:
        print(f"they do not match audi!={s} , case matters. So we can use lower method to both strings and that would solve it")

def checkValueOnList(s):
    mylist = ["moy","tablo","pao","nati"]
    mylist2 = ["moy","pao","nati"]
    if s.lower() in mylist:
        print(f"{s} is in the list")

    if s.lower() not in mylist2:
        print(f"{s} is not in the second list")

def multipleif():
    #sometimes we will need to have multiple individual IF statements in order to do something in our code. For example:
    ingridients = ["peperoni","cheese","onions","beef"]

    if "peperoni" in ingridients:
        print("Adding peperoni")
    if "cheese" in ingridients:
        print("Adding cheese")
    if "onions" in ingridients:
        print("We do not have onions, sorry!")
    if "beef" in ingridients:
        print("Really? In the pizza?... ok, it´s your choise")

    print("Your pizza is ready!")

    #We could also had the same output using and & or in the conditionals and looping trhough the list

def elifMethod():
    numbers = [1,2, 3,5] #4 is missing
    if 1 not in numbers:
        print("1 is not in the list")
    elif    2 not in numbers:
        print("2 is not in the list")
    elif    3 not in numbers:
        print("3 is not in the list")
    elif    4 not in numbers:
        print("4 is not in the list")
    elif    5 not in numbers:
        print("5 is not in the list")

def checkListIsEmpty():
    mylist = []

    if mylist:
        print(f"Your list is not empty, {mylist}")
    else:
        print("Your list is empty!!!")

ifsimple()
caseMatters("Audi")
checkValueOnList("Tablo")
multipleif()
elifMethod()
checkListIsEmpty()
