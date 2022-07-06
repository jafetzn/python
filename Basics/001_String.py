

strsimple="IAmASrting"
strtomodify="I am a string with an eroor"


def modifySting(s):
    index = 0
    if "o" in s:
        index = s.index("o")
    newText = s[:index] + "r" +  s[index+1:]
    print(newText)

def indexAndNegativeIndex(s):
    print(s[1])
    print(s[-1])
    print(s.index("to"))

def slicingStrings(s):
    print(s[:5])
    print(s[5:])

def inMethod(s,word):
    if word in s:
        print("Word: " + word + " is in: " + s)
    else:
        print("Word: " + word + " is NOT: " + s)

def titleMethod():
    text = "harry potter deathly hollows"
    print(text.title())

def upperMethod(s):
    print(s.upper())

def lowerMethod(s):
    print(s.lower())

def stripMethod(s):
    print("Both left and right strip method:[" + s.strip() + "]")
    print("Left strip method:[" + s.lstrip() + "]")
    print("Right strip method:[" + s.rstrip() + "]")

def lenMethod(s):
    print(len(s))

def endsWithMethod():
    print("Viejo zorro".endswith("zorro"))
    print("Viejo cochino".endswith("zorro"))
    print("Viejo cochino".startswith("Viejo"))

def isnumericMethod(s):
    print("Is numeric? " + str(s.isnumeric()))

def joinMethod():

    print(" ".join(["this","is","a","string","method"]))
    print("...".join(["this","is","a","string","separated","by", "tripple", "dots"]))


def splitMethod():
    print("this is another example".split())
    print("this is another example, we use a comma to separate the text".split(","))
    print(len("this is another example, we use a comma to separate the text".split(",")))
    int_num = int(input("escribe un numero:\n"))
    print(f"Tu numero es: {int_num}")
    arr = "0 1 2 8 7 5".split()
    print(f"Printing array\n{arr}")
    arr.sort()
    print(f"Printing array\n{arr[-2]}")
######### Calling out the methods

def isAplhaMethod():
    #string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
    text1 = "Thistextcontainsonlyalphabeticcharcaters"
    text2 = "This text does not contains only alphabetic charcaters, 012984"
    print(text1.isalpha())
    print(text2.isalpha())


def replaceMethod():
    text1 = "original text, will replace commas, for dots,"
    print(text1)
    print(text1.replace(",","."))
    print(text1)
    text2 = text1.replace(",",".")
    print(text2)



print(strsimple)
print("A" in strsimple)
print("a" in strsimple)
modifySting(strtomodify)
slicingStrings("applejuice")
indexAndNegativeIndex("This is a text to try indexes")
inMethod("I am a good developer and tester", "tester")
inMethod("I am a good developer and tester", "Developer")
inMethod("I am a good developer and tester", "developer")
titleMethod()
upperMethod("A simple String to verify some methods!")
lowerMethod("A simple String to verify some methods!")
stripMethod(" Removing spaces at     both ends of the string   ")
lenMethod("How many characters do I have?")
endsWithMethod()
isnumericMethod("2")
isnumericMethod("k")
joinMethod()
splitMethod()
isAplhaMethod()
replaceMethod()
