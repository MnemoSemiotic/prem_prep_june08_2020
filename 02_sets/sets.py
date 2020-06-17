# list/set trick "dedupe"

some_list = [1,2,3,7,8,4,4,4,9,8,4,5,6,4,8,9,1,3]

some_list_listset = list(set(some_list))

some_list_deduped_inorder = []
for element in some_list:
    if element not in some_list_deduped_inorder:
        some_list_deduped_inorder.append(element)

# print(some_list_listset)
# print(some_list_deduped_inorder)


