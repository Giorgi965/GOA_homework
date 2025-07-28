def positive_sum(arr):
    total = 0
    for number in arr:
        if number > 0:
            total += number
    return total


def opposite(number):
    return -number


def even_or_odd(number):
    x= number % 2 == 0
    if x :
        return "Even"
    else:
        return "Odd"
    
def make_negative( number ):
    if number > 0:
        return -number
    else:
        return number
    

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 == 0:
            return "Error: Division by zero!"
        return value1 / value2
    else:
        return "Error: Invalid operator"
    

def sum_array(a):
    total = 0
    for number in a:
        total += number
    return total

def make_upper_case(s):
    return s.upper()

def simple_multiplication(number) :
        if number % 2 ==0:
            return number * 8
        else: 
            return number * 9

def invert(lst):
    result = []
    for num in lst:
        result.append(-num)
    return result