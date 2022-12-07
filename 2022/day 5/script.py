# %% Imports
import numpy as np
import re

# %% Data
DEBUG = False

input_file = 'debug.txt' if DEBUG else 'input.txt'

with open(input_file) as file:
    text = file.read()

crates_txt = text[:text.find('1')].rstrip().split('\n')
n_stacks = (len(crates_txt[0])+1)//4
crates = [[] for _ in range(n_stacks)]
for l in crates_txt[::-1]:
    for i,char in enumerate(l[1::4]):
        if char!=' ': crates[i].append(char)

moves = [{'n':int(crate), 'start':int(start)-1, 'end':int(end)-1} for crate,start,end in [re.search(r'move (\d*) from (\d*) to (\d*)', line).groups() for line in text[text.find('m'):].rstrip().split('\n')]]


# %% Part 1
def resolve_9000(crates, move):
    for _ in range(move['n']):
        crates[move['end']].append(crates[move['start']].pop())

[resolve_9000(crates,move) for move in moves]

print(''.join([x[-1] for x in crates]))

# %% Part 2
def resolve_9001(crates, move):
    i = len(crates[move['start']]) - move['n']
    for _ in range(move['n']):
        crates[move['end']].append(crates[move['start']].pop(i))

[resolve_9001(crates,move) for move in moves]

print(''.join([x[-1] for x in crates]))
