# %% Imports
import numpy as np

# %% Data
DEBUG = False

input_file = 'debug.txt' if DEBUG else 'input.txt'
with open(input_file) as file:
    input = np.array([list(l) for l in file.read().split('\n')])

char_to_val = lambda c: ord(c)-ord('a') if c not in ['S','E'] else 0 if c=='S' else ord('z')-ord('a')

start = np.argwhere(input=='S').flatten()
end = np.argwhere(input=='E').flatten()

height, width = input.shape

# %% Part 1
def neighboors(v):
    cond = [v[0]>0,v[0]<height-1,v[1]>0,v[1]<width-1]
    return (np.array([[-1,0],[1,0],[0,-1],[0,1]])+v)[cond].tolist()
def dijkstra(start):
    dist = {}
    prev = {}
    Q = set()
    for i in range(0,height):
        for j in range (0,width):
            dist[(i,j)] = float('inf')
            prev[(i,j)] = None
            Q.add((i,j))

    dist[tuple(start)] = 0

    while len(Q)>0:
        u = list(Q)[[dist[k] for k in Q].index(min([dist[k] for k in Q]))]
        Q.remove(u)

        for v in neighboors(list(u)):
            v = tuple(v)
            if v in Q:
                edge = char_to_val(input[v]) - char_to_val(input[u])
                if edge>1: continue
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    return dist

dijkstra(start)[tuple(end)]
# %% Part 2

def dijkstra_inverted(start):
    dist = {}
    prev = {}
    Q = set()
    for i in range(0,height):
        for j in range (0,width):
            dist[(i,j)] = float('inf')
            prev[(i,j)] = None
            Q.add((i,j))

    dist[tuple(start)] = 0

    while len(Q)>0:
        u = list(Q)[[dist[k] for k in Q].index(min([dist[k] for k in Q]))]
        Q.remove(u)

        for v in neighboors(list(u)):
            v = tuple(v)
            if v in Q:
                edge = char_to_val(input[v]) - char_to_val(input[u])
                if edge<-1: continue
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    return dist

dist = dijkstra_inverted(end)
min([dist[a] for a in [tuple(a) for a in np.argwhere(input=='a')]])