DivByThreeAndFive = lambda dividend: True if (dividend % 3 == 0 or dividend % 5 == 0) and dividend != 0 else False

results = []
for number in filter(DivByThreeAndFive, range(50)):
    results.append(number)

print(results)