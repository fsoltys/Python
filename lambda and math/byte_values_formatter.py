
def format(number):
    if not isinstance(number, int):
        raise TypeError("Enter an integer")
    if number < 0:
        raise ValueError("Number should be >= 0")
    if number > (1024 ** 4):
        raise ValueError("Biggest possible amount is 1023GB")
    
    units = ("B", "kB", "MB", "GB")
    results = []

    for unit in units:
        if number == 0:
            break
        remainder = number % 1024
        if remainder != 0:
            results.append(f'{remainder} {unit}')
        number = number // 1024
        
    return results

print(format(256321683216))
    
    