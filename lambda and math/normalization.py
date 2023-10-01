import math


def normalize(floattable):
    squaresum = 0
    result = []
    
    for x in floattable:
        squaresum += x**2
    
    for x in floattable:
        x /= (math.sqrt(squaresum))
        result.append(x)
        
    return result


print(normalize((2.4, 1.4, 0.8)))
