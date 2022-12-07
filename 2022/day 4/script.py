# %% Imports
import numpy as np

# %% Data
with open('input.txt') as file:
    input = np.array([[x.split('-'),y.split('-')] for x,y in [line.rstrip().split(',') for line in file]]).reshape(-1,4).astype(int)

input

# %% Part 1
input[(input[:,0]>=input[:,2])*(input[:,1]<=input[:,3])+(input[:,0]<=input[:,2])*(input[:,1]>=input[:,3])].shape[0]

# %% Part 2
input[(input[:,0]<=input[:,3])*(input[:,1]>=input[:,2])].shape[0]