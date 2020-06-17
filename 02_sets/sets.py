'''list/set trick "dedupe"'''

some_list = [1,2,3,7,8,4,4,4,9,8,4,5,6,4,8,9,1,3]

some_list_listset = list(set(some_list))

some_list_deduped_inorder = []
for element in some_list:
    if element not in some_list_deduped_inorder:
        some_list_deduped_inorder.append(element)

# print(some_list_listset)
# print(some_list_deduped_inorder)

''' Brief intro to *args '''
def demo_star_args(*args):
    for item in args:
        print(item)
    return None

var1 = True
var2 = 'I\'m a string'
var3 = [8,9,7,2,3,4,7,8,9]
var4 = ['some', 'words', 'innit']

# demo_star_args(var1, var2, var3, var4, some_list)

'''Create Sample Space for the roll of 2 6 sided dice'''

sample_space = []
sums = []

for i in range(1, 6+1):
    for j in range(1, 6+1):
        sample_space.append([i,j])
        sums.append(i+j)

for lst in sample_space:
    # print(f'{lst}: {lst[0]+lst[1]}')
    pass

'''What is the probability of rolling an 8?'''
# print(sums.count(8) / len(sums))




'''Simple Union function for sets'''
list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']

def union(set1, set2):
    set_union = []
    for item in set1:
        set_union.append(item)
    for item in set2:
        if item not in set_union:
            set_union.append(item)
    return set_union

# print(union(list1, list2))

def union_mult_sets(*args):
    set_union = []
    for lst in args:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    return set_union

# print(union_mult_sets(list1, list2, list3))



'''Slide 8 Breakout'''

four_sided = [1,2,3,4]
coin_flip = ['H', 'T']

samp_space = []
for roll in four_sided:
    for flip1 in coin_flip:
        for flip2 in coin_flip:
            samp_space.append([roll, flip1, flip2])

for outcome in samp_space:
    # print(outcome)
    pass

A = []
for outcome in samp_space:
    if outcome[0] == 1:
        A.append(outcome)

# print(A)

B = []

for outcome in samp_space:
    if outcome.count('H') >= 1:
        B.append(outcome)

# print(B)


# print(union(A, B))


''' Intersection'''
def intersection(set1, set2):
    set_intersect = []
    for item in set1:
        if item in set2:
            set_intersect.append(item)
    
    return set_intersect

# print(intersection(list1, list2))


def intersection_mult(*args):
    set_intersect = []
    
    for item in args[0]:
        flag = True
        for set_ in args:
            if item not in set_:
                flag = False
        if flag == True:
            set_intersect.append(item)
    
    return set_intersect

# print(intersection_mult(list1, list2, list3))


''' Complement Function '''
sample_space = union_mult_sets(list1, list2, list3)
# print(sample_space)
# print(list3)
def complement(samp_space, set_):
    comp = []
    for item in samp_space:
        if item not in set_:
            comp.append(item)
    return comp

# print(complement(sample_space, list3))


''' Breakout Solution '''
coin_flip = ['H', 'T']

samp_space = []

for flip1 in coin_flip:
    for flip2 in coin_flip:
        for flip3 in coin_flip:
            for flip4 in coin_flip:
                samp_space.append(f'{flip1}{flip2}{flip3}{flip4}')

# print(samp_space)
# print()
A = []
B = []
C = []
for outcome in samp_space:
    if outcome.count('H') >= 3:
        A.append(outcome)
    if outcome.count('T') <= 2:
        B.append(outcome)
    if outcome.count('H') == 4 or outcome.count('T') == 4:
        C.append(outcome)

# print('A',A)
# print('B',B)
# print('C',C)

# print(intersection(A, complement(samp_space, C)))

# print(complement(samp_space, intersection(A, C)))

'''Set Difference'''
def difference(set1, set2):
    set_diff = []
    for item in set1:
        if item not in set2:
            set_diff.append(item)
    return set_diff

# print(difference(list1, list2))
# print(difference(list2, list1))
