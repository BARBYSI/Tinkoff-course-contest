n = int(input())
a = int(input())
highspeed = a
cars = []
cars.append(a)
for i in range (n-1):
    a = int(input())
    if highspeed > a or highspeed == a:
        highspeed = a
        cars.append(a)
    elif highspeed < a:
        cars.append(highspeed)
        
print(*cars)
    