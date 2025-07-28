def mango(quantity, price):
    free_mangoes = quantity // 3
    paid_mangoes = quantity - free_mangoes
    total_cost = paid_mangoes * price
    return total_cost

def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


def get_planet_name(id):
    name = ""
    if id == 1:
        name = "Mercury"
    elif id == 2:
        name = "Venus"
    elif id == 3:
        name = "Earth"
    elif id == 4:
        name = "Mars"
    elif id == 5:
        name = "Jupiter"
    elif id == 6:
        name = "Saturn"
    elif id == 7:
        name = "Uranus"
    elif id == 8:
        name = "Neptune"
    return name

def problem(a):
    if type(a) == str:
        return "Error"
    else:
        return a * 50 + 6
    

def say_hello(name):
    return f"Hello, {name}"