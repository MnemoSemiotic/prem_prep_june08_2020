
from random import choice

def get_bit():
    return choice([1,0])

def get_binary(n=8):
    return_list = []
    for _ in range(n):
        return_list.append(get_bit())

    return return_list

# print(get_binary(n=8))

# --> [0, 1, 1, 0, 0, 1, 0, 1]

def get_float(n=8):
    bin_list = get_binary(n)

    float_accum = 0
    for idx, bit in enumerate(bin_list):
        float_accum += bit * .5**(idx+1)
    
    return float_accum

# print(get_float())

for _ in range(20):
    print(get_float())

# bit * .5**(idx+1)
# [0, 1, 1, 0, 0, 1, 0, 1]

# 0 * 0.5**1 + 1 * 0.5**2 + 1 * 0.5**3 ... 