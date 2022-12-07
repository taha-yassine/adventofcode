# %% Imports
import numpy as np

# %% Data
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

input
# %% Part 1
sum([(ord(y)-ord('A')+27 if y.isupper() else ord(y)-ord('a')+1) for y in [list(set(x[:len(x)//2]).intersection(set(x[len(x)//2:])))[0] for x in input]])

# %% Part 2
sum([(ord(y)-ord('A')+27 if y.isupper() else ord(y)-ord('a')+1) for y in [list(set(x).intersection(set(y),set(z)))[0] for (x,y,z) in np.array(input).reshape(-1,3)]])