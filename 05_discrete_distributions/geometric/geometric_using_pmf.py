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


def geom_cdf_closed(p, k, inclusive=False):
    if inclusive:
        return 1 - (1-p)**k
    else:
        return 1 - (1-p)**(k+1)

def geom_cdf_accum(p, k, inclusive=False):
    proba_ = 0
    if inclusive:
        for r in range(1, k+1):
            proba_ += geom_pmf(p, r, inclusive=inclusive)
    else:
        for r in range(0, k+1):
            proba_ += geom_pmf(p, r, inclusive=inclusive)
    return proba_

'''
You are flipping a fair coin. What is the probability that you will need to flip the coin less than 7 times before getting a heads?
0000001
000001
00001
0001
...
'''

# print(geom_cdf_closed(p=0.5, k=7, inclusive=True))
# print(geom_cdf_closed(p=0.5, k=6, inclusive=False))
# print(geom_cdf_accum(p=0.5, k=7, inclusive=True))
# print(geom_cdf_accum(p=0.5, k=6, inclusive=False))


def geometric_pmf_dict(p, k, inclusive=False):
    d = {}

    if inclusive:
        for r in range(1, k+1):
            d[r] = geom_pmf(p, r, inclusive=inclusive)
    else:
        for r in range(0, k+1):
            d[r] = geom_pmf(p, r, inclusive=inclusive)
    return d

# for k, v in geometric_pmf_dict(p=0.5, k=10, inclusive=False).items():
#     print(f'{k}: {v}')

# print('\n')

# for k, v in geometric_pmf_dict(p=0.5, k=10, inclusive=True).items():
#     print(f'{k}: {v}')


def geometric_cdf_dict(p, k, inclusive=False):
    d = {}

    if inclusive:
        for r in range(1, k+1):
            d[r] = geom_cdf_closed(p, r, inclusive=inclusive)
    else:
        for r in range(0, k+1):
            d[r] = geom_cdf_closed(p, r, inclusive=inclusive)
    return d

# k = 30
# for k, v in geometric_cdf_dict(p=0.5, k=k, inclusive=False).items():
#     print(f'{k}: {v}')

# print('\n')

# for k, v in geometric_cdf_dict(p=0.5, k=k, inclusive=True).items():
#     print(f'{k}: {v}')