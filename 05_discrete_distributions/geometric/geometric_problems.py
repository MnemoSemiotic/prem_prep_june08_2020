from geometric_using_pmf import *

'''
Geometric Breakout 1
Suppose you have an unfair coin, with a 68% chance of getting tails. 
What is the probability that the first head will be on the 3rd trial?
'''

# print(geom_pmf(p=0.32, k=2, inclusive=False))
# print(geom_pmf(p=0.32, k=3, inclusive=True))

'''
Geometric Breakout 2
According to the article “Characterizing the Severity and Risk of Drought in the Poudre River, Colorado” taken from a water conservation journal, the drought length Y is the number of consecutive time intervals in which the water supply remains below a critical value y0 (a deficit), preceded by and followed by periods in which the supply exceeds this critical value (a surplus). The journal proposes a geometric distribution with  p = 0.409 for this random variable.
(hint: consider the probability p to represent the “success” of breaking a drought)
What is the probability that the drought lasts exactly three intervals?
'''

p = 0.409

# print(geom_pmf(p, k=3, inclusive=False))
# print(geom_pmf(p, k=4, inclusive=True))

'''
Given that there is a drought, what is the probability that the drought lasts at most three intervals?
'''
print(geom_pmf(p, k=3, inclusive=False) + geom_pmf(p, k=2, inclusive=False) + geom_pmf(p, k=1, inclusive=False))