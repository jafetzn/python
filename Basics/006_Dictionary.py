"""
used to organize elements into collections. data inside a dict take the form of pair of elements KEY and VALUE
a dictionary is defined by {}
Empty dictionary dictionary_name = {}
dictionary_name = {"key1":value1,"key2":value2,"key3":value3,"key4":value4}
A dictionary is mutable, add, edit, remove elements from the dict



"""
def simpledict():
    person = {"name" : "jafet", "age" : 32, "sex" : "male" }
    print(person['name'])
    print(person['sex'])

def keyInDictionary(k):
    dict = {'name':'moy'}
    if k in dict:
        print("name is a key in the dictionary")
    else:
        print("name is NOT a key in the dictionary")

def addKeyValue():
    #To add a key-value pair you would have to put the name of the dictionary = and between square brackets the name of the key = the value of that key
    dict = {'name':'moy'}
    dict["age"] = 32
    print(dict)

def modifyValuesInDictionary():
    person = {"name" : "jafet", "age" : 32, "sex" : "male" }
    print(person)
    person['name'] = "Tablo"
    print(person)

def removePairElements():
    person = {"name" : "jafet", "age" : 32, "sex" : "male" }
    del person['age']
    print(person)

def getDictionary():
    #If we want to retrieve a value indicating a key that does not exist in our dictionary it will throw an error
    #So, in order to avoid that, we can use a second parameter in the get method to specify what to print if the key does not exist
    #if there is a chance that the key you are looking for does not exist, consider use the GET method instead the square brackets notation
    person = {"name" : "jafet", "age" : 32, "sex" : "male" }
    print(person.get("hobby","He has no hobby"))
    print(person.get("name","He has no name").title())

def loopingDictionary():
    # items() is used to get both the keys and the values of the dictionary
    users = {"username":"jafetzn","firstname":"Jafet","lastname":"Zarate","language":"python","profession":"qa engineer", "age": 32}
    print("\n")
    for key, value in users.items():
        print(f"Key: [{key}], Value:[{value}]")

def loopingKeys():
    #This method is useful when you do not need the values of each key in the dictionary but only the keys on it
    print("Unsorted")
    users = {"username":"jafetzn","firstname":"Jafet","lastname":"Zarate","language":"python","profession":"qa engineer", "age": 32}
    for key in users.keys():
        print(f"Key:\t{key}")

    print("Sorted")
    #we can also sort the reults using sorted() method
    for key in sorted(users.keys()):
        print(f"Key:\t{key}")

    print("Sorted-reverse order")
    #we can also sort the reults using sorted() method
    for key in sorted(users.keys(), reverse=True):
        print(f"Key:\t{key}")

def loopingValues():
    #This method is useful when you do not need the keys in the dictionary but only the values on it
    print("")
    users = {"username":"jafetzn","firstname":"Jafet","lastname":"Zarate","language":"python","profession":"qa engineer", "age": 32}
    for value in users.values():
        print(f"Value:\t{value}")

def setInDictionary():
    #values() is useful when you do not mind the values of the keys are duplicated, but if you want to get only unique values, you must use a set.
    #a set is a collection which every item must be unique

    print("")
    languages = {"moy":"python","jafet":"java","pao":"C","tablo":"python","nati":"ruby"}
    for value in languages.values():
        print(f"Value:\t{value}")
    print("")
    print("Unique values")
    for value in set(languages.values()):
        print(f"Unique Value:\t{value}")


simpledict()
keyInDictionary("name")
keyInDictionary("age")
addKeyValue()
modifyValuesInDictionary()
removePairElements()
getDictionary()
loopingDictionary()
loopingKeys()
loopingValues()
setInDictionary()
