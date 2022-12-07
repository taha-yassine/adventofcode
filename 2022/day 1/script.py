# %% Imports
import numpy as np

# %% Data
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

input
# %% Part 1
accum = []
t=0
for x in input:
    if x=='': 
        accum.append(t)
        t=0
        continue
    t+=int(x)
    
max(accum)

# %% Part 2
accum = np.array(accum)
np.sum(np.partition(accum,len(accum)-3)[-3:])