from collections import Counter

mylist = ["hello","lhelo","pao","ohell","apo"]
print(f"Original list\n{mylist}\n")
auxList = []
results = []
lastword = ""
auxlen = 0
auxcount = 0

arrlen = len(mylist)

for word in mylist:
    print(f"\nnew iteration {auxcount}")

    if auxcount == len(mylist)-1:
        auxcount -= 1
    print(f"auxcount tiene valor de {auxcount} y buscare ese index en mylist con longitud de {len(mylist)} ")

    if sorted(list(word)) == sorted(list(mylist[auxcount+1])):
        print(f"Prev word>{word} has the same characters than {mylist[auxcount+1]}")
        mylist.remove(mylist[auxcount+1])
        auxcount -= 1
    auxcount += 1

print(f"\nFinal list\n{mylist}\n")


"""

while mylist:
    for word in mylist:
        #este if es para que solo se ejecute el codigo en la segunda iteracion
        #porque en la primera no hay con que comparar
        if lastword!="":
            #
            if len(word) == len(lastword):
                #print("match lenghts")
                print(f"Prev word>{lastword} has the same characters than {word}")
                #auxList = list(lastword)
                #print(sorted(auxList))
                if sorted(list(lastword)) == sorted(list(word)):
                    print(f"remuevo {word}")
                    results.append(lastword)
                    mylist.remove(word)
        else:
            lastword = word
        auxlen = len(word)
        auxcount += 1
    if len(mylist) == len(results):
        break

print(f"\nFinal list>\n{mylist}")
"""
