"""
Tuples are similar to list but the main difference that these are immutable, Meaning that the value of the elements in a tuples cannot change
Other difference from the list, is that instead of using square brackets to declare them, we use brackets ()
"""
dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

#if we want to modify the value of any item, it will throw an error

#dimensions[0] = 250

#if we want to create a tuplem with only one element, we will need to do something like This

my_tuple = (10,)
print(type(my_tuple))

#we can asisng the variable name of the tuple to another tuple values in order to change the content of the tuple
