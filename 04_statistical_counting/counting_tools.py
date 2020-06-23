

def factorial(num):
    accum = 1

    for n in range(2, num+1):
        accum *= n

    return accum

# print(factorial(5))

def perm(n, k):
    return int(factorial(n) / factorial(n-k))

# print(perm(10, 3))


'''
Let's get all the permutations from a list of items
'''