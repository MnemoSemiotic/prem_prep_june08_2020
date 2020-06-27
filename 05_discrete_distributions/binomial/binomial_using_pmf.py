
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
    for k in range(k_high):
        cumulative += binomial_pmf(n, k, p=p)
    return cumulative

'''There are 8 components in parallel and at least 3 of those components need to operational for a circuit to function. The probability of any given component being operational is 0.7. What is the probability that 3 components are operational?'''

# print(binomial_pmf(8, 3, p=0.7))

'''What is the probability that at least 3 components are operational?'''
# print(binomial_pmf(8, 3, p=0.7) + binomial_pmf(8, 4, p=0.7) + binomial_pmf(8, 5, p=0.7) + binomial_pmf(8, 6, p=0.7) + binomial_pmf(8, 7, p=0.7) + binomial_pmf(8, 8, p=0.7))
# or
# print(1 - (binomial_pmf(8, 2, p=0.7) + binomial_pmf(8, 1, p=0.7 + binomial_pmf(8, 0, p=0.7)))
print(1- binomial_cdf(8, 2, p=0.7))
