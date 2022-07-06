def test():
    #n = int(input())
    arr = map(int, input("Enter scores").split())
    print(type(arr))
    print(arr)
    resultado =list(arr)
    print(resultado)
    resultado.sort()
    print(resultado)
    print(resultado[-2])

def scores():
    students_scores = {}
    for _ in range(int(input("how many students?"))):
        name = input("Name: ")
        score = float(input("Score:"))
        students_scores[name.lower()] = str(score)
    print({k: v for k, v in sorted(students_scores.items(), key=lambda item: item[0])})
    lowest = {k: v for k, v in sorted(students_scores.items(), key=lambda item: item[0])}
    print(lowest)
    values = list(lowest.values())
    names = list(lowest.keys())
    print(values)
    if values[0] == values[1]:
        print(f"{names[0]} and {names[1]} have the same score: {values[0]}")
    else:
        print(f"{names[0]} has the lowest score")

#test()
scores()
