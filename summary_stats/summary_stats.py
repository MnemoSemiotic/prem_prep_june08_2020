

def mean(lst):
    return sum(lst) / len(lst)


def median(lst):
    lst_sorted = sorted(lst)

    if len(lst) % 2 == 1:
        median_idx = int(len(lst) / 2 - 0.5)
        return lst_sorted[median_idx]
    else:
        return mean([lst_sorted[int(len(lst)/2 - 1)], lst_sorted[int(len(lst)/2)]])

def mode(lst):
    most_occurring = lst[0]

    for item in lst[1:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item

    return most_occurring



def five_number_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)

    Q1 = median(sorted(lst)[0:int(len(lst)/2)])
    Q3 = median(sorted(lst)[int(len(lst)/2):])

    return min_, Q1, med, Q3, max_

def iqr(lst):
    _, Q1, _, Q3, _ = five_number_summary(lst)
    return Q3 - Q1

def detect_outliers(lst):
    _, Q1, _, Q3, _ = five_number_summary(lst)
    IQR = iqr(lst)
    
    outliers = []

    for item in lst:
        if item < Q1 - 1.5*IQR:
            outliers.append(item)
        if item > Q3 + 1.5*IQR:
            outliers.append(item)

    return outliers



def variance(lst, population=False):
    total = 0
    mean_ = mean(lst)

    for item in lst:
        total += (item - mean_)**2

    if population==True:
        return total / len(lst)
    else:
        return total / (len(lst)-1)


def stdev(lst, population=False):
    if population==True:
        return variance(lst, True)**(1/2)
    else:
        return variance(lst, False)**(1/2)



print(stdev([1,2,3,4,5], True))
print(stdev([1,2,3,4,5], False))