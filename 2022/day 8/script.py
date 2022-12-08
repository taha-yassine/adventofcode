# %% Imports
import numpy as np

# %% Data
DEBUG = False

input_file = 'debug.txt' if DEBUG else 'input.txt'
with open(input_file) as file:
    trees = np.array([list(l) for l in file.read().split('\n')]).astype(int)

# %% Part 1
left = trees
right = trees[:,::-1]
bottom = trees.T
top = (trees.T)[:,::-1]

x_left = np.concatenate((np.zeros_like(left)-1,left),axis=1)[:,np.arange(left.shape[0])+1 + np.expand_dims(np.arange(left.shape[0]),axis=1)]

y_left = np.all((x_left < np.repeat(x_left[:,:,-1,...,np.newaxis],left.shape[0],axis=2))[...,:-1],axis=2)

x_right = np.concatenate((np.zeros_like(right)-1,right),axis=1)[:,np.arange(right.shape[0])+1 + np.expand_dims(np.arange(right.shape[0]),axis=1)]

y_right = np.all((x_right < np.repeat(x_right[:,:,-1,...,np.newaxis],right.shape[0],axis=2))[...,:-1],axis=2)[:,::-1]

x_bottom = np.concatenate((np.zeros_like(bottom)-1,bottom),axis=1)[:,np.arange(bottom.shape[0])+1 + np.expand_dims(np.arange(bottom.shape[0]),axis=1)]

y_bottom = np.all((x_bottom < np.repeat(x_bottom[:,:,-1,...,np.newaxis],bottom.shape[0],axis=2))[...,:-1],axis=2).T

x_top = np.concatenate((np.zeros_like(top)-1,top),axis=1)[:,np.arange(top.shape[0])+1 + np.expand_dims(np.arange(top.shape[0]),axis=1)]

y_top = np.all((x_top < np.repeat(x_top[:,:,-1,...,np.newaxis],top.shape[0],axis=2))[...,:-1],axis=2)[:,::-1].T

np.sum(np.any(np.stack([y_left,y_right,y_bottom,y_top]),axis=0))

# %% Part 1 - one-liner
np.sum(np.any(np.stack([np.all((np.concatenate((np.zeros_like(trees)-1,trees),axis=1)[:,np.arange(trees.shape[0])+1 + np.expand_dims(np.arange(trees.shape[0]),axis=1)] < np.repeat(np.concatenate((np.zeros_like(trees)-1,trees),axis=1)[:,np.arange(trees.shape[0])+1 + np.expand_dims(np.arange(trees.shape[0]),axis=1)][:,:,-1,...,np.newaxis],trees.shape[0],axis=2))[...,:-1],axis=2),np.all((np.concatenate((np.zeros_like(trees[:,::-1])-1,trees[:,::-1]),axis=1)[:,np.arange(trees[:,::-1].shape[0])+1 + np.expand_dims(np.arange(trees[:,::-1].shape[0]),axis=1)] < np.repeat(np.concatenate((np.zeros_like(trees[:,::-1])-1,trees[:,::-1]),axis=1)[:,np.arange(trees[:,::-1].shape[0])+1 + np.expand_dims(np.arange(trees[:,::-1].shape[0]),axis=1)][:,:,-1,...,np.newaxis],trees[:,::-1].shape[0],axis=2))[...,:-1],axis=2)[:,::-1],np.all((np.concatenate((np.zeros_like(trees.T)-1,trees.T),axis=1)[:,np.arange(trees.T.shape[0])+1 + np.expand_dims(np.arange(trees.T.shape[0]),axis=1)] < np.repeat(np.concatenate((np.zeros_like(trees.T)-1,trees.T),axis=1)[:,np.arange(trees.T.shape[0])+1 + np.expand_dims(np.arange(trees.T.shape[0]),axis=1)][:,:,-1,...,np.newaxis],trees.T.shape[0],axis=2))[...,:-1],axis=2).T,np.all((np.concatenate((np.zeros_like((trees.T)[:,::-1])-1,(trees.T)[:,::-1]),axis=1)[:,np.arange((trees.T)[:,::-1].shape[0])+1 + np.expand_dims(np.arange((trees.T)[:,::-1].shape[0]),axis=1)] < np.repeat(np.concatenate((np.zeros_like((trees.T)[:,::-1])-1,(trees.T)[:,::-1]),axis=1)[:,np.arange((trees.T)[:,::-1].shape[0])+1 + np.expand_dims(np.arange((trees.T)[:,::-1].shape[0]),axis=1)][:,:,-1,...,np.newaxis],(trees.T)[:,::-1].shape[0],axis=2))[...,:-1],axis=2)[:,::-1].T]),axis=0))

# %% Part 2
