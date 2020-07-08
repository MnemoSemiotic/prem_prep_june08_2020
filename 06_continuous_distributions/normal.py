from math import e, pi


def normal_pdf(x, mu, sigma):
    return (1 / (sigma * (2*pi)**(1/2))) * e**((-(1/2)*((x-mu) / sigma)**2))


def normal_cdf(x, mu, sigma):
    vals = [num*0.001 for num in range(-10000, int(x*1000)+1)]

    accum = 0
    for val in vals:
        res = normal_pdf(val, mu, sigma)
        accum += res

        if val > x:
            break

    return accum*0.001

# print(1-normal_cdf(100, 90, 10))