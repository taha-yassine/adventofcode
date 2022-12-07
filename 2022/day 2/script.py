# %% Imports
import numpy as np
from itertools import product

# %% Data
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

input
# %% Part 1 - Solution 1
x = np.array([[ord(c) for c in i.split()] for i in input])
x[:,0] -= ord('A')-1
x[:,1] -= ord('X')-1
print(np.sum((((np.diff(x) + 1) % 3)*3).flatten() + x[:,1]))

# %% Part 1 - Solution 1 one-liner
print((lambda x: np.sum((((np.diff(x) + 1) % 3)*3).flatten() + x[:,1])) (np.array([[ord(c) for c in i.split()] for i in input]) - [ord('A')-1, ord('X')-1]))

# %% Part 1 - Solution 2
prod = np.array([x+' '+y for x,y in list(product('ABC','XYZ'))])
prod = dict(map(lambda i,j : (i,j) , np.array([np.roll(row, x) for row,x in zip(prod.reshape(-1,3), [0,-1,-2])]).flatten() ,np.tile([3,6,0],3)))
print(np.sum([prod[q] for q in input] + (np.array([ord(i[-1]) for i in input])-ord('X')+1)))

# %% Part 2
x = np.array([[ord(c) for c in i.split()] for i in input])
x[:,0] -= ord('A')
x[:,1] -= ord('X')+1
np.sum(np.sum(x,axis=1)%3+1 + (x[:,1]+1)*3)