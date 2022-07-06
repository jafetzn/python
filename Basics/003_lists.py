"""
Lists allows you to store sets of information in one place
Its a collection of items in a particular order, you can make lists of every type of data/objects
In Python, [] indicates a list, and individual elements are separated by commas
Ex:
bicycles = ['trek','cannodale','bennoto','redline','specialized']
print(bicycles)
>>>['trek','cannodale','bennoto','redline','specialized']
Index positions starts at 0, not at 1
"""

def accessToElements(index):
    fruits = ['sandia','mango','fresa','papaya','melon']
    print(fruits[index].title())
    print(f"My favorite fruit is {fruits[index].title()}")

def modifyAList(biker_list):
    #To change the value of an item in a list, we need to specify both the index where is located inside the list and the new value that will be updated
    print(biker_list)
    biker_list[0] = 'ducati'
    print(biker_list)


def addElementToAList(biker_list):
    #The easiest way to add items to a list is using the append method,
    #The new item will be added at the end of the list (last position)
    biker_list.append('ducati')
    print(biker_list)

def insertMethod(biker_list):
    #You can also add an item to a list using the INSERT method, which allows you to insert an item in a specific index on the list
    #This operation shifts every other elementn in the list one position to the right
    biker_list.insert(1, 'ducati')
    print(biker_list)

def removeElementFromAList(biker_list):
    #To remove an element from a list we use the DEL statement, and indicating the index between square braquets that we want to delete []
    del biker_list[-1]
    print(biker_list)

def popMethodToRemove(biker_list):
    #The POP method removes the last item of a list, but it lets you to work and manipulate that element you just removed
    #
    popped_item = biker_list.pop()
    print(biker_list)
    print(f"The item that was removed, was: {popped_item}")

    #And we can specify the index for an element to pop it out from the lists
    popped_item2 = biker_list.pop(0)
    print(biker_list)
    print(f"The 2nd item that was removed, was: {popped_item2}")

def removeByValue(biker_list):
    #Sometimes you will not know the index of the element you want to remove/pop, so if you at least know the value of that element you can use the REMOVE methods
    #This will only remove the first occurrence of the value you specified, if there is more items with the same value you will need a loop to delete them all.
    biker_list.remove('yamaha')
    bike_to_remove = "pulsar"
    biker_list.remove(bike_to_remove)
    print(biker_list)

def sortingAList(biker_list):
    #We can sort alphabetically the elements of a list using the SORT method, this method wiil sort the list permanently
    biker_list.sort()
    print(biker_list)

    #And we can sort the list in reverse alphabetical order by passing the argument reverse=True to the method
    biker_list.sort(reverse=True)
    print(biker_list)

def sortedMethod(biker_list):
    #This SORTED method will present a list sorted alphabetically/reverse alphabetical order but will not change permanently the original sort
    print(f"This is the original list {biker_list}")
    print(f"This is the sorted list {sorted(biker_list)}")
    print(f"Printing again the original list {biker_list}")

def reverseMethod(biker_list):
    #The REVERSE method on a list will reverse the original order of the list permanently, but you can reverse a 2nd time to go back to the original sort
    biker_list.reverse()
    print(biker_list)

def lenMethod(biker_list):
    print(biker_list)
    print(f"The lenght of the list above is {len(biker_list)}")

def mapMethod():
    # Python program to demonstrate working of map.
    #map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    # We double all numbers using map()
    numbers = (1, 2, 3, 4)
    result = map(additionExample, numbers)
    print(list(result))

# Return double of n
def additionExample(n):
    return n + n


accessToElements(0)
accessToElements(1)
accessToElements(-1)
modifyAList(['honda','yamaha','pulsar'])
addElementToAList(['honda','yamaha','pulsar'])
insertMethod(['honda','yamaha','pulsar'])
removeElementFromAList(['honda','yamaha','pulsar'])
popMethodToRemove(['honda','yamaha','pulsar'])
removeByValue(['honda','yamaha','pulsar'])
sortingAList(['honda','yamaha','pulsar','ducati'])
sortedMethod(['honda','yamaha','pulsar','ducati'])
reverseMethod(['honda','yamaha','pulsar','ducati'])
lenMethod(['honda','yamaha','pulsar','ducati'])
mapMethod()
