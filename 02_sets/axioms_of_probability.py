from sets import union, union_mult_sets, intersection, intersection_mult, complement, difference


setA = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
setB = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
setC = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']

sample_space = union_mult_sets(setA, setB, setC)

print(sample_space)






