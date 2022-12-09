# %% Imports
import numpy as np

# %% Data
DEBUG = False
VERBOSE = False

input_file = 'debug.txt' if DEBUG else 'input.txt'
with open(input_file) as file:
    input = file.read().split('\n')

height = 1000
width = 1000

# %% Part 1
def print_state(head, tail):
    bl_to_tl = lambda x,y: (x,height-y-1)
    matrix = [list('.'*width) for _ in range(height)]
    head_x, head_y = bl_to_tl(*head)
    tail_x, tail_y = bl_to_tl(*tail)
    matrix[tail_y][tail_x] = 'T'
    matrix[head_y][head_x] = 'H'
    [print(''.join(l)) for l in matrix]

def move(h,t,m):
    v = (lambda s,x,y: [(s*2-1)*n for n in [x,y]])(*[int(n) for n in f'{" DL  UR".find(m):03b}'])
    h_new = [x + y for x, y in zip(h, v)]
    return h_new, t if max([abs(x-y) for x,y in zip(t,h_new)])<=2 else h

h = [0,0]
t = [0,0]

if VERBOSE: print_state(h,t) # Initial state
if VERBOSE: print('')

visitations = np.zeros((height,width))

for inst in input:
    if VERBOSE: print(f'== {inst} ==')
    m,n = (lambda x,y: (x,int(y)))(*inst.split(' '))
    for _ in range(n):
        h,t = move(h,t,m)
        if VERBOSE: print_state(h,t)
        if VERBOSE: print('')
        # visitations[t[0],height-t[1]-1] = 1
        visitations[t[0],t[1]] = 1

int(np.sum(visitations))

# %% Part 2
