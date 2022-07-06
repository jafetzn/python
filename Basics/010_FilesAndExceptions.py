"""

"""


def readingEntireFile():
    """ Using this method will let us read data from a TXT file, this will read the entire file  """
    # In windows, we may need to use \ instead /, and use double \\ because just using one
    # will cause some errors and not detect the file
    with open("C:\\atom\\python-basics\\Basics\\text_files\\file_example.txt") as file_object:
        contents = file_object.read()
        print(contents.rstrip())

def readUsingVariables():
    filename = "C:\\atom\\python-basics\\Basics\\text_files\\file_example.txt"
    with open(filename) as file_object:
        for line in file_object:
            print(line)
            #print(line.rstrip())

"""
When using WITH, the file object returned by open, is only available inside the
WITH block. if you want to retain access to a file's contents outside the block,
you should store the file's lines in a list inside the block and then work with
that list outside of it. Next method will show that
"""

def storeFileData():
    lines_list = []
    filename = "C:\\atom\\python-basics\\Basics\\text_files\\file_example.txt"

    with open(filename) as file_object:
        for line in file_object:
            lines_list.append(line)

    print(f"The list saves all the lines containing even the \\n at the end of the line:\n\n {lines_list}")


def storeFileData2():
    lines_list = []
    filename = "C:\\atom\\python-basics\\Basics\\text_files\\file_example.txt"

    with open(filename) as file_object:
        lines_list = file_object.readlines()

    print("fileobject.readlines() is useful to get all the lines \n")
    for line in lines_list:
        print(line.rstrip())

readingEntireFile()
print()
readUsingVariables()
storeFileData()
print()
storeFileData2()
