from random import random

def bernoulli(p_success=0.5):
    return random() < p_success

num_trials = 100000
trials_success = 0
for _ in range(num_trials):
    if bernoulli(p_success=0.62):
        trials_success += 1

print(trials_success/num_trials)