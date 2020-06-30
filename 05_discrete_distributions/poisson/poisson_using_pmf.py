
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

# print(poisson_pmf(10, 10))

def poisson_pmf_dict(lmbda, low_k, high_k):
    d = {}

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lmbda, k)

    return d

# for k, v in poisson_pmf_dict(10, 0, 50).items():
#     print(f'{k}: {v}')


def poisson_cdf_dict(lmbda, low_k, high_k):
    d = {}
    accum = 0.0
    for k in range(low_k, high_k+1):
         accum += poisson_pmf(lmbda, k)
         d[k] = accum

    return d

# for k, v in poisson_cdf_dict(10, 0, 50).items():
#     print(f'{k}: {v}')


'''
You are observing a phenomenon that follows perfectly a poisson process. Given a certain number of observations (10,000), how many events would you expect for each value of k, given a lmbda of 10, low_k=0, to high_k=30?
'''

def poisson_counts(lmbda, low_k, high_k, num_samples=10000):
    d = {}

    for k in range(low_k, high_k+1):
        d[k] = int(poisson_pmf(lmbda, k) * 10000)

    return d


for k, v in poisson_counts(10, 0, 30, 10000).items():
    print(f'{k}: {v}')

'''
There's a busy intersection in Denver, where 30 cars pass by every 10 minutes. What is the probability that 40 cars will pass by if observing a new ten minute time period?
'''
# print(poisson_pmf(lmbda=30, k=40)) # 0.0139


'''
You have a data set from observing a stream where salmon swim by at a rate of 10 fish every 15 minutes. What is the probability that 15 fish swim by in 30 minutes?

lmbda = 20
'''
# print(poisson_pmf(lmbda=20, k=15)) # 0.0516


'''
In a volume of a certain compressed gas that is resampled daily, on average you would expect to observe 20 nitrogenous molecules. What is the probability that you would observe 25 of these molecules?
'''
# print(poisson_pmf(lmbda=20, k=25)) # 0.0446


'''
There a doorway where we expect 10 people to walk through every 5 minutes. What is the probability that 10 people will walk through in 5 minutes?
'''
# print(poisson_pmf(lmbda=10, k=10)) # 0.125


