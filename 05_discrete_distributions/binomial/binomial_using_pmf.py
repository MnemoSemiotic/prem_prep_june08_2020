
def factorial(num):
    prod = 1

    for n in range(2, num+1):
        prod *= n

    return prod


def combinations(n, k):
    return int( factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))

def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0
    for k in range(k_high+1):
        cumulative += binomial_pmf(n, k, p=p)
    return cumulative

def binomial_dict(n, k_low, k_high, p=0.5):
    d = {}

    for k in range(k_low, k_high+1):
        d[k] = binomial_pmf(n, k, p=p)
    
    return d

'''There are 8 components in parallel and at least 3 of those components need to operational for a circuit to function. The probability of any given component being operational is 0.7. What is the probability that 3 components are operational?'''

# print(binomial_pmf(8, 3, p=0.7))

'''What is the probability that at least 3 components are operational?'''
# print(binomial_pmf(8, 3, p=0.7) + binomial_pmf(8, 4, p=0.7) + binomial_pmf(8, 5, p=0.7) + binomial_pmf(8, 6, p=0.7) + binomial_pmf(8, 7, p=0.7) + binomial_pmf(8, 8, p=0.7))
# or
# print(1 - (binomial_pmf(8, 2, p=0.7) + binomial_pmf(8, 1, p=0.7 + binomial_pmf(8, 0, p=0.7)))
# print(1- binomial_cdf(8, 2, p=0.7))



'''
You have a fair coin. You flip that coin 20 times. What is the probability that you will get 7 heads?
'''

# print(binomial_pmf(20, 7, 0.5))

'''
What is the probability that you get 10 or less heads in 20 flips of a fair coin?
'''
# binomial_pmf(20, 0, 0.5) + binomial_pmf(20, 1, 0.5) ...
print(binomial_cdf(20, 10, 0.5))


'''
In a high speed boat race, there are 30 boats. The probability that any given boat will complete the race is 0.6. What is the probability that at least 20 boats (20 or more) finish the race?

20 boats, 21 boats, 22 boats, 23 boats ... 30 boats
'''
# binomial_pmf(30, 20, 0.6) + binomial_pmf(30, 21, 0.6) ...
proba = 0
for k in range(20, 30+1):
    proba += binomial_pmf(30, k, 0.6)

print(proba)
print(1 - binomial_cdf(30, 19, 0.6))

# pmf
# for k, v in binomial_dict(30, k_low=0, k_high=30, p=0.6).items():
#     print(f'{k}: {v}')

# cdf
accum = 0
for k, v in binomial_dict(30, k_low=0, k_high=30, p=0.6).items():
    accum += v
    print(f'{k}: {accum}')