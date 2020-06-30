
def factorial(n):
    if n < 0:
        return None

    prod = 1

    for i in range(2, n+1):
        prod *= i

    return prod

# print(factorial(5))

from math import e
def poisson_pmf(lmbda, k):
    return (lmbda**k * e**(lmbda * -1))/ factorial(k)

print(poisson_pmf(10, 10))