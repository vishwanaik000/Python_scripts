n = input("eneter number")

def squarefrees(maximum):
    maximum += 1
    temp = [True]*maximum
    yield 1
    temp[0] = False
    temp[1] = False
    for i,squarefree in enumerate(temp):
        if squarefree:
            yield i
            for j in range(2*i, maximum, i):
                temp[j] = not temp[j]
        
print(list(squarefrees(n)))

