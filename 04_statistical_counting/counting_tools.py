

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
# Consider a base 5 number system: 0, 1, 2, 3, 4
# How many ways can you rearrange those numbers, using each number only once?

def permutations_nP3(base=5):
    base_5_list = []

    for i in range(base):
        for j in range(base):
            for k in range(base):
                base_5_list.append([i, j, k])

    permutations = []

    for arrangement in base_5_list:
        is_permutation = True

        for num in arrangement:
            if arrangement.count(num) > 1:
                is_permutation = False
                break

        if is_permutation:
            permutations.append(arrangement)

    return permutations


# print(len(permutations_nP3(base=5)))
# print(perm(n=5, k=3))


'''
Breakout slide 15
'''

# n = 10
# k = 3
# print(perm(10, 3))
# print(perm(9, 2))



def comb(n, k):
    return int(factorial(n) / factorial(n-k) * factorial(k))