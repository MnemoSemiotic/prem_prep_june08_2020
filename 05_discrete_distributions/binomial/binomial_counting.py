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
    bin_lst = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        for n in range(2):
                            for o in range(2):
                                for p in range(2):
                                    bin_lst.append([i,j,k,l,m,n,o,p])
    return bin_lst

list_of_binary =  gen_8_bit_binary_with_fors()

binom_dict_8_trials = {}

for bin_list in list_of_binary:
    print(bin_list)
    sum_of_bits = sum(bin_list)
    if sum_of_bits not in binom_dict_8_trials:
        binom_dict_8_trials[sum_of_bits] = 0
    binom_dict_8_trials[sum_of_bits] += 1

for k, v in binom_dict_8_trials.items():
    print(f'{k}: {v}')

