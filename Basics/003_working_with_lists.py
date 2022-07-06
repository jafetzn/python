

def loopingAListFOR():
    #We can use t the FOR loop to go through an entire list and do certain action on each element of the list
    soccer_teams = ['america','real madrid','manchester united','juventus','milan','newcastle']
    for team in soccer_teams:
        print(f"Team: {team.title()}")

def numericalList():
    #Lists are ideal for storing numbers, and we can use the RANGE() method to print a series of numbers
    #(start, end-1)
    #(only one parameter, from 0 to the number given)
    #(start, end-1, jumps from number to next number)
    for value in range(1,5):
        print(value)
    print("\n")
    for  value in range(5):
        print(value)

    numbers = list(range(10))
    print(numbers)

def skipNumbersInRange():
    even_numbers = list(range(2,11,2))
    print(even_numbers)

def findMinimum():
    numbers = [ '10','20','30','30','20','10']
    mini = min(numbers)
    print(mini)

def findMaximum():
    numbers = [ '10','20','30','30','20','10']
    print(max(numbers))


def sumOfList():
    numbers = [ 10,20,30,30,20,10]
    print(sum(numbers))

def sliceOfList():
    #By using : inside [], we can specify 2 parameter, on the left of the colon put the start index wthat you want to slice and to the right the index(-1) that will be the end of the slice
    list = ['one','two','three','four']
    print(list[0:2]) #start:end
    print(list[2:]) #start:     this will take all of the elements after the index you specify to the right
    print(list[:2]) #end:     this will take all of the elements after the index you specify to the left

def copyAList(list):
    #If we just put the = sign to a list, what we are doing here is indicate Python that both variables are referring to the same lists
    #In order to copy all the content of a list into another list we should use [:], that will tell Python to copy the lists
    new_list = list
    new_list.append('php')
    print(list)
    print(new_list)
    #on the output, both list will contain the same elements eventhough we just added an element to the new_list
    separate_list = list[:]
    separate_list.append('c#')
    print(list)
    print(separate_list)

def list3():
    number_one = 7
    number_two = 0
    number_three =1

    my_list = [number_one, number_two, number_three]
    print(my_list)

def listcomprehension():
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, .
Please use list comprehensions rather than multiple loops, as a learning exercise.

Example
x   1
y   1
z   1
n   3

All permutations of [i,j,k] are:

Print an array of the elements that do not sum to n= 3.

Input Format
Four integers  and , each on a separate line.

Constraints
Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""


loopingAListFOR()
numericalList()
skipNumbersInRange()
findMinimum()
findMaximum()
sumOfList()
sliceOfList()
copyAList(['java','ruby','python','c++','.Net','JS'])
list3()
listcomprehension()
