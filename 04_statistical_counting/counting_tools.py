

def factorial(num):
    accum = 1

    for n in range(2, num+1):
        accum *= n

    return accum

print(factorial(5))