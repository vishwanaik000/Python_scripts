import math

count = 0
n = input ("eneter num")
def squarefree(n):
    for i in range (2,math.ceil(math.sqrt(math.sqrt(n)))):
        if n%(i**2)==0:
            return False
        count +=1
    return True

squarefree(20)




