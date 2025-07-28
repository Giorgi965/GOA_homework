def count_by(x, n):
    return[x * i for i in range(1,n+1)]

def reverse_words(s):
    words = s.split(' ')
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def reverse_seq(n):
    return list(range(n, 0, -1))


def grow(arr):
    product = 1
    for number in arr:
        product *= number
    return product

def smash(words):
    return " ".join(words)