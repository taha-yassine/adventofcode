# %% Imports
import re
# %% Data
DEBUG = False

input_file = 'debug.txt' if DEBUG else 'input.txt'
with open(input_file) as file:
    input = [line.rstrip().replace(': ','=').replace(' ','') for line in file]

input
# %% Part 1
available = []
queue = input.copy()
program = []
while queue:
    l = queue[0]
    l_key, l_values = l.split('=')
    if l_values.isdigit():
        available.append(l_key)
        program.append(queue.pop(0))
        continue
    l_values = re.split(r'\W',l_values)
    for v in l_values:
        if v not in available:
            queue.pop(0)
            queue.append(l)
            break
    else:
        available.append(l_key)
        program.append(queue.pop(0))

exec('\n'.join(program))
print(int(root))
