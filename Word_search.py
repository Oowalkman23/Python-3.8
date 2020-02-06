def test_case():
    # setting up the grid board and answer
    # word = answer we're looking for
    # strings and row to make the grid board

    word = list('racecar')
    strings = word.copy()
    row = 7    
    grid = []

    for i in range(row):
        grid.append(strings)

    # lets start the searching
    main(grid, word)

     
def scan(i, j, v):
    # set up the coordinate to start scan
    x = grid_board[i][j]

    # start scanning 
    for r in range(1,len(answer)):        
        # limit the boundary
        if i+v[0]*r not in range(0,len(grid_board)) or j+v[1]*r not in range(0,len(grid_board[0])):
            x += ''
        else:
            x += grid_board[i+v[0]*r][j+v[1]*r]
    return x
    
def direction(i, j):
    # v_direction = list for the direction of further scan in coordinate
    v_direction = []

    # scan in all direction start
    for p in d_vertical:
        for q in d_horizontal:
            # limit the coordinate if out of bound (grid_board), next iteration
            if i+d_vertical[p] in (-1,len(grid_board)) or j+d_horizontal[q] in (-1,len(grid_board[0])):
                continue            
            # if match with 2nd word of the answer, we record the direction to the list
            if grid_board[i+d_vertical[p]][j+d_horizontal[q]] == answer[1]:
                v_direction.append([d_vertical[p], d_horizontal[q]])

    # set up the counter
    total = 0 
    # check all the direction   
    if v_direction:
        for v in v_direction:
            # call function scan() to check the number of matched, for each scan direction
            if scan(i, j, v) == ''.join(answer):
                total += 1   
        return total
    else:
        return total  

def main(grid, word):
    # set up variable for global use
    # grid_board = grid board
    # answer = the word we're looking for
    # d_vertical = dictionary for vertical movement
    # d_horizontal = dictionary for horizontal movement
    # results = the counter for each word found that matched our objective 
    global grid_board, answer, d_vertical, d_horizontal
    grid_board = grid
    answer = word
    d_vertical = {'up':-1, 'mid':0, 'down':+1}
    d_horizontal = {'left':-1, 'mid':0, 'right':+1}
    results = 0

    # start the scan for first word
    for i in range(len(grid_board)):
        for j in range(len(grid_board[0])):
            # if matched, call function direction()
            if grid_board[i][j] == answer[0]:
                c = direction(i, j)
                results += c
    
    # print results
    for i in grid_board:
        print(i)
    print(f'The total number of your word in the grid is = {results}')

test_case()