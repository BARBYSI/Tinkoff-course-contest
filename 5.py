n = int(input())

numbers = [i for i in range(n, 0, -1)]
total = sum(numbers)
if total % 3 == 0 and n > 3:
  setsum = total // 3
  sets = [[],[],[]]
  
  for num in numbers:
    if sum(sets[0]) + num <= setsum: sets[0].append(num)
    elif sum(sets[1]) + num <= setsum: sets[1].append(num)
    else: sets[2].append(num)
    
  for i in range(3):
    print(len(sets[i]))
    print(*sets[i])
    print("")
      
else: print(-1)