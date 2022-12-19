# %% Imports
import numpy as np
from scipy.spatial import distance_matrix

# %% Data
DEBUG = False

input_file = 'debug.txt' if DEBUG else 'input.txt'
with open(input_file) as file:
    input = np.loadtxt(file,delimiter=',')

input
# %% Part 1
d = distance_matrix(input, input)

input.shape[0]*6-np.count_nonzero(d==1)