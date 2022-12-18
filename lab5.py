
def factorial(n):
    k = 1
    acc = 1

    while k != (n+1):
        acc*=k
        k+=1

    return acc