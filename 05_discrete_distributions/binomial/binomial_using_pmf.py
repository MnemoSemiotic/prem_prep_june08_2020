
def factorial(num):
    prod = 1

    for n in range(2, num+1):
        prod *= n

    return prod


def combinations(n, k):
    return int( factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))

# There are 8 components in parallel and at least 3 of those components need to operational for a circuit to function. The probability of any given component being operational is 0.7. What is the probability that 3 components are operational?

print(binomial_pmf(8, 3, p=0.7))