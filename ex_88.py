row = int(input())
col = int(input())
character_spot = input()
barrier = input()

def make_map(row, col, character_spot, barrier):
    map = [[0 for i in range(row+2)] for i in range(col+2)]

    for i in range(row+2):
        for j in range(col+2):
            if i == 0 or i == row+1 or j == 0 or j == col+1:
                map[j][i] = 2
    
    
    map[int(int(character_spot[0])+1)][int(int(character_spot[1])+1)] = 1

    return map

make_map(row,col,character_spot,barrier)

