def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i is True:
            count += 1
    return count

def invert(lst):
    result = []
    for num in lst:
        result.append(-num)
    return result