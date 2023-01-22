from itertools import combinations
n = int(input())

temp = 0
maxNOD = 0
t = 0

while t != n:
    t += 1
    temp = t
    unique = []
    dividers = []
    while True:
        if temp == 1:
            NOD = 1
            break
        divider = 2
        while True:
            if temp % divider == 0:
                temp /= divider
                dividers.append(divider)
                break
            else: divider += 1

    for i in range(2, len(dividers)+1):
        comb = combinations(dividers, i)
        for i in list(comb):
            unique.append(i)
    NOD = len(set(unique)) + len(set(dividers)) + 1
    if NOD >= maxNOD:
        maxNOD = NOD
        result = t
print(result)
print(maxNOD)
