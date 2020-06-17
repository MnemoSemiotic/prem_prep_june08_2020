# list/set trick "dedupe"

some_list = [1,2,3,7,8,4,4,4,9,8,4,5,6,4,8,9,1,3]

some_list_listset = list(set(some_list))

some_list_deduped_inorder = []
for element in some_list:
    if element not in some_list_deduped_inorder:
        some_list_deduped_inorder.append(element)

# print(some_list_listset)
# print(some_list_deduped_inorder)




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
list1 = ['bear', 'cat', 'dog', 'dolphin']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'weasel', 'mink', 'eagle']

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

print(union_mult_sets(list1, list2, list3))