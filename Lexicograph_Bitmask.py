def permutations():
    global running
    global characters
    global bitmask
    if len(running) == len(characters):
        print(''.join(running), end=' ')
    else:
        for i in range(len(characters)):
            if ((bitmask>>i)&1) == 0:
                bitmask |= 1<<i
                running.append(characters[i])
                permutations()
                bitmask ^= 1 << i
                running.pop()


'''raw = raw_input()'''
characters = list('cghmsuv')
running = []
bitmask = 0
permutations()