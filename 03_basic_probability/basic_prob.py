from random import choice

'''Independence'''
bool_list = ['H', 'T']

def independent_trials(n=20):
    outcomes = []

    for _ in range(20):
        outcomes.append(choice(bool_list))
    
    return outcomes

outcomes_heads = []
for _ in range(500):
    outcomes_heads.append(independent_trials(n=20).count('H'))

avg_of_outcomes = sum(outcomes_heads) / len(outcomes_heads)


# prob of getting into a fight on Thanksgiving is 0.6
# prob of eating too much that night 0.4
# prob of going to sleep early is 0.38
# what is the probability of these events happening?
# --> P(fight)*p(overeat)*p(sleep) = 0.6 * 0.4 * 0.38

# what is the probability of getting 10 heads in a row when flipping a fair coin?
# --> 0.5**10

# what is the probability, when drawing from a deck of cards without replacement, of first drawing a king of clubs, then drawing a queen of diamonds, then drawing an ace? 
# --> 1/52 * 1/51 * 4/50



'''Dependence'''
num_range = list(range(52))

rand_val = choice(num_range)

num_range.remove(rand_val)

rand_val2 = choice(num_range)



list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel', 'cat', 'dog', 'cat']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion', 'elephant']

# P(cat|list1)? 3/8
# P(cat|list2)? 0/8

# t ----------->
# first, pick a list, then you pick an animal


'''
Breakout Stats 3 slide 18/19
'''

# What is the probability of flipping a coin five times in a row, and getting a heads on each flip? 

sides = ['T', 'H']
flips = []

for flip1 in sides:
    for flip2 in sides:
        for flip3 in sides:
            for flip4 in sides:
                for flip5 in sides:
                    flips.append([flip1,flip2,flip3,flip4,flip5,])

five_flips_proba = flips.count(['H', 'H', 'H', 'H', 'H']) / len(flips)


roll_possibilities = [1,2,3,4,5,6]
rolls = []

for roll1 in roll_possibilities:
    for roll2 in roll_possibilities:
        for roll3 in roll_possibilities:
            rolls.append([roll1, roll2, roll3])

