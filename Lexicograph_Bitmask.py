def permutations():
    # call variables
    global running
    global characters
    global bitmask
    if len(running) == len(characters):
        print(''.join(running), end=' ')
    else:
        for i in range(len(characters)):
            # basically telling if there is a string hasn't been added to the list yet then..
            if ((bitmask>>i)&1) == 0:
                bitmask |= 1<<i
                running.append(characters[i])
                permutations()
                # reassign bitmask to 0
                bitmask ^= 1 << i
                running.pop()

# initial input
string = input('Input your strings = ')
characters = list(string)
# storage for words
running = []
bitmask = 0
permutations()
