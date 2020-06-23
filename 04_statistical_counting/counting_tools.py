

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


# 20C3 ... think of this as we have 20 items in a bag, and we're wondering how many different combinations of these items can we make

def combinations_intuition():
    twenty_nums = list(range(1, 21))

    # find every arrangement of 3
    possible_three = []

    for i in twenty_nums:
        for j in twenty_nums:
            for k in twenty_nums:
                possible_three.append([i, j, k])

    # print(len(possible_three))

    # find permutations
    permutations = []

    for three in possible_three:
        permutation = True

        for num in three:
            if three.count(num) > 1:
                permutation = False
                break
        if permutation:
            permutations.append(three)

    # print(len(permutations))

    # let's remove perms that have the same same elements as other permutations
    combinations = []

    for three in permutations:
        sorted_three = sorted(three)
        if sorted_three not in combinations:
            combinations.append(sorted_three)


    # print(len(combinations))
    return combinations


# for comb in combinations_intuition():
#     print(comb)


# print(len(combinations_intuition()))



'''
Let's take a sampling approach to building permutations and combinations
'''
from random import choice

def get_permutations(vals=[0,1,2,3,4], length=5):
    output = []

    for _ in range(1000):
        if len(output) == length:
            break
    
        val = choice(vals)
        
        if val not in output:
            output.append(val)
        
    return output

for _ in range(10):
    print(get_permutations())