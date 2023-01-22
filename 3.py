s = input()
playfield = [['x','x','x','x'],['x','x','x','x'],['x','x','x','x'],['x','x','x','x']]

#looking for a space for horizontal block
def hf():
    global playfield
    vres = []
    checker = False
    i, j, counter= 0, 0, 0
    t = 1
    while checker != True:
        vres.append(playfield[i][j])
        vres.append(playfield[i][t])
        if vres[counter] == 'x' and vres[counter+1] == 'x':
            #the slots taken by blocks are just integer 0
            playfield[i][j] = 0
            playfield[i][t] = 0
            print(i+1, j+1)
            checker = True
        else:
            j += 1
            t += 1
        counter += 2
        if t == 4:
            j = 0
            t = 1
            i += 1
        if i == 4:
            checker = True
    return 0
#looking for a free space for vertical block
def vf():
    global playfield
    vres = []
    checker = False
    i, j, counter= 0, 0, 0
    t = 1
    while checker != True:
        if t == 4:
            checker = True
        vres.append(playfield[i][j])
        vres.append(playfield[t][j])
        if vres[counter] == 'x' and vres[counter+1] == 'x':
            playfield[i][j] = 0
            playfield[t][j] = 0
            print(i+1, j+1)
            checker = True
        else:
            j += 1
        counter += 2
        if j == 4:
            i += 1
            t += 1
            j = 0
    return 0

for i in s:
    if i == '0':
        vf()
    else: hf()
    #looking for rows or columns of blocks
    for j in range(len(playfield)):
        for t in range(len(playfield[j])):
            if playfield[j][t] == 'x':
                break
            elif t == 3:
                playfield[j] = ['x']*4
    for j in range(len(playfield)):
        for t in range(len(playfield[j])):
            if playfield[t][j] == 'x':
                break
            elif t == 3: 
                for h in range(len(playfield)):
                    playfield[h][j] = 'x'