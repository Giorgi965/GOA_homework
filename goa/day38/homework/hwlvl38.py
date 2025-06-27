def repeatguramvhiko(text, n=0):
    return text * n
result = repeatguramvhiko("guramchiko", 5)
print(result)


def goa(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return perimeter, area


import turtle

def draw_rectangle(length, width):
    t = turtle.Turtle()
    t.forward(length)
    t.left(90)
    t.forward(width) 
    t.left(90)
    t.forward(length)  
    t.left(90)
    t.forward(width)
    turtle.done()