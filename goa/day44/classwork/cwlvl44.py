def string_to_array(s):
    return s.split(" ")


def digitize(n):
    numbers = []
    for i in str(n)[::-1]:
        numbers.append(int(i))
    return numbers

def is_palindrome(s):
    return s.lower()[::-1] == s.lower()


def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)
    

def past(h, m, s):
    h = h *60*60*1000
    m = m * 60 * 1000
    s = s * 1000
    return h + m + s


def smash(words):
    st=""
    for i in words:
        st += i + " "
    return st[0:-1]