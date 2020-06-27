# 00
# 01
# 02
# 03
# 04
# 05
# 06
# 07
# 08
# 09
# 10 = 1 * 10 + 0 * 1
# 11 = 1 * 10 + 1 * 1
# ...

# 000 = 0
# 001 = 1
# 010 = 2
# 011 = 0 * 4 + 1 * 2 + 1 * 1 = 3 
# 100 = 4
# 101 = 5
# 110 = 6
# 111 = 7


def gen_8_bit_binary_with_fors():
    bin_lst = {}
    counter = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        for n in range(2):
                            for o in range(2):
                                for p in range(2):
                                    bin_lst[counter] = [i,j,k,l,m,n,o,p]
                                    counter += 1
    return bin_lst


# demo of dec to bin algorithm
# 10
# [0,]
# 5
# [0,1]
# 2
# [0,1,0]
# 1
# [0,1,0,1]
# 0
# ...
# [0,1,0,1,0,0,0,0] -> [0,0,0,0,1,0,1,0]

def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1]

def get_binary(n_bits=8):
    bins_d = {}
    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)
    return bins_d


def binomial_distr(binary_dict):
    binomial_dict = {}

    for _, v in binary_dict.items():
        sum_ = sum(v)
        if sum_ not in binomial_dict:
            binomial_dict[sum_] = 0
        binomial_dict[sum_] += 1

    return binomial_dict


d = get_binary(n_bits=6)

# for k, v in d.items():
#     print(f'{k}: {v}')

binomial_dict = binomial_distr(d)

for k, v in binomial_dict.items():
    print(f'{k}: {"*"*v}')


# for_loop_binary =  gen_8_bit_binary_with_fors()

# binom_dict_8_trials = binomial_distr(for_loop_binary)


# for k, v in binom_dict_8_trials.items():
#     print(f'{k}: {v}')




