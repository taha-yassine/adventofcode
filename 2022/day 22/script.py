# %% Imports
import re
import numpy as np
# %% Data
DEBUG = False

input_file = 'debug.txt' if DEBUG else 'input.txt'
with open(input_file) as file:
    input = [line.rstrip() for line in file]

map = input[:-2]
code = re.findall(r'[a-zA-Z]{1}|\d+', input[-1])

height = len(map)
width = max([len(l) for l in map])
map = [l+' '*(width-len(l)) for l in map]
map = [list(l) for l in map]

# %% Part 1
map_2 = np.array(map, copy=True)
coord = np.argwhere(map_2=='.')[0]
coord = np.concatenate((coord,[0])) # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
map_2[coord[0],coord[1]]=['>','v','<','^'][coord[2]]

moves=[[0,1],[1,0],[0,-1],[-1,0]]

def move(coord):
    v=[[0,1],[1,0],[0,-1],[-1,0]][coord[2]]
    next_coord = np.array([(coord[0]+v[0])%height,(coord[1]+v[1])%width,coord[2]])
    if map_2[next_coord[0]][next_coord[1]] == ' ':
        if coord[2] == 0:
            next_coord[1] = np.argwhere(map_2[coord[0]]!=' ')[0,0]
        elif coord[2] == 1:
            next_coord[0] = np.argwhere(map_2[:,coord[1]]!=' ')[0,0]
        elif coord[2] == 2:
            next_coord[1] = width-1-np.argwhere(map_2[coord[0],::-1]!=' ')[0,0]
        elif coord[2] == 3:
            next_coord[0] = height-1-np.argwhere(map_2[::-1,coord[1]]!=' ')[0,0]

    if map_2[next_coord[0]][next_coord[1]] in ['.','>','v','<','^']:
        map_2[next_coord[0]][next_coord[1]] = ['>','v','<','^'][coord[2]]
        return next_coord
    elif map_2[next_coord[0]][next_coord[1]] == '#':
        return coord
for c in code:
    if c.isdigit():
        for i in range(int(c)):
            coord = move(coord)
            # print('\n'.join([''.join(l) for l in map_2]))
            # print('--------------------------------------')
    else:
        coord[2] = (coord[2]+1)%4 if c=='R' else (coord[2]-1)%4
        map_2[coord[0]][coord[1]]=['>','v','<','^'][coord[2]]
        # print('\n'.join([''.join(l) for l in map_2]))
        # print('--------------------------------------')

print(sum((coord+[1,1,0])*[1000,4,1]))
# %%
