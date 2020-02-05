from queue import Queue
import random
import sys
sys.setrecursionlimit(2000)

def test_case():
    # factions of abcde, # as mountain, and '.' as land
    # connected land would be dominated by faction if alone
    # if there's more than one faction, counted as 'contested' area
     
    factions_and_symbols = list('abcde#.')
    # Setting maps
    grid = []
    for i in range(20):
        grid_row = []
        for j in range(20):
            spot = random.choice(factions_and_symbols)
            grid_row.append(spot)
        grid.append(grid_row)
    
    main(grid)

def main(grid):

    # setting up variables for global use
    # gridx = game board
    # list_coordinate = list of visited coordinate (row, column)
    # list_faction = dictionary of faction list
    # v_arah = dictionary of direction vector on the game board
    # list_tree = queue of coordinates, for recursion purpose
    # contested = if more than one faction, marked as contested

    global gridx, list_coordinate, list_faction, v_arah
    gridx = grid
    list_tree = Queue()
    list_coordinate = []
    list_faction = {}
    v_arah = {'up':(-1,0), 'down':(1,0), 'left':(0,-1), 'right':(0,1)}
    contested = 0
    
    # initial search process, starts from row=0,column=0
    for i in range(len(gridx)):
        for j in range(len(gridx[0])):
            
            data = gridx[i][j]

            # if meets mountain #, continue to next iteration
            if data == '#':
                continue
            # else, set up list_tree and counter (for counting contested area)
            list_tree = Queue()
            counter = {}
            # if result of function which would be counter, > 1, contested area
            if scan(i,j,list_tree, counter) > 1:
                contested += 1
    
    # print results for faction list, number of each, and contested area in the map.
    for x in list_faction:
        print(f'{x} {len(list_faction[x])}')
    print(f'contested {contested}')

def check_spot(next_spot, coord, list_tree, counter):
    # checking next spot as stated with other given parameters
    if next_spot == '#':
        pass
    # storing visited coordinate, and enqueue it for next scan()    
    list_coordinate.append(coord)
    list_tree.put(coord)
    
    # if found '.' or factions, call function check_faction()
    if next_spot != '.':
        check_faction(next_spot, coord, counter)
    return counter


def scan(i,j,list_tree,counter):
    # scanning in 4 vector of direction
    for v in v_arah:
        # if next coordinate is out of index range, next iteration
        if i+v_arah[v][0] in (-1,len(gridx)) or j+v_arah[v][1] in (-1, len(gridx[0])):
            continue

        next_spot = gridx[i+v_arah[v][0]][j+v_arah[v][1]]
        coord = (i+v_arah[v][0], j+v_arah[v][1])
        
        if coord in list_coordinate:
            continue
        if next_spot == '#':
            continue        
        # check the next spot
        counter = check_spot(next_spot, coord, list_tree, counter)

    # check queue, if empty, then exit function
    if list_tree.empty():
        return len(counter)
    # else, scan for next coordinate as queued
    coord_next = list_tree.get()    
    scan(coord_next[0], coord_next[1], list_tree, counter)
    return len(counter)

def check_faction(next_spot, coord, counter):
    # check faction in dictionary, if there's new, add the list, and the counter
    if next_spot not in list_faction:
        list_faction[next_spot] = [coord]
        counter[next_spot] = [coord]
    else:
        list_faction[next_spot].append([coord])

    return counter

test_case()
