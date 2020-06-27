
def factorial(num):
    prod = 1

    for n in range(2, num+1):
        prod *= n

    return prod


def combinations(n, k):
    return int( factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):