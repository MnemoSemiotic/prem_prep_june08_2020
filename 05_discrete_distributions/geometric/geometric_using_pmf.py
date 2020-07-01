def geom_pmf(p, k, inclusive=False):
    if inclusive:
        return p*(1-p)**(k-1)
    else:
        return p*(1-p)**k

'''
You are flipping a fair coin. What is the probability that you get a heads on the 7th flip?
'''
# print(geom_pmf(0.5, 7, inclusive=True))
# print(geom_pmf(0.5, 6, inclusive=False))